#!/usr/bin/env python3
from PIL import Image, ImageStat
import colorsys
import os

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def clamp(v):
    return max(0, min(255, int(v)))

def darker(rgb, pct=0.2):
    r, g, b = rgb
    return (clamp(r * (1 - pct)), clamp(g * (1 - pct)), clamp(b * (1 - pct)))

def luminance(rgb):
    r, g, b = [c / 255.0 for c in rgb]
    def srgb(c):
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    R, G, B = srgb(r), srgb(g), srgb(b)
    return 0.2126 * R + 0.7152 * G + 0.0722 * B

def extract_dominant(image_path):
    im = Image.open(image_path).convert('RGBA')
    im = im.resize((120, int(120 * im.height / im.width)), Image.LANCZOS)
    pal = im.convert('P', palette=Image.ADAPTIVE, colors=8)
    palette = pal.getpalette()
    color_counts = sorted(pal.getcolors(), reverse=True)
    for count, idx in color_counts:
        r = palette[idx * 3]
        g = palette[idx * 3 + 1]
        b = palette[idx * 3 + 2]
        return (r, g, b)
    return (10, 107, 83)

if __name__ == '__main__':
    img = 'assets/hero-photo.jpg'
    if not os.path.exists(img):
        print('Please upload assets/hero-photo.jpg and re-run this script.')
        exit(1)
    
    dom = extract_dominant(img)
    dark = darker(dom, 0.18)
    L = luminance(dom)
    hero_text = '#111' if L > 0.5 else '#fff'
    accent = rgb_to_hex(*dom)
    accent_dark = rgb_to_hex(*dark)
    overlay = f'linear-gradient(rgba({dom[0]},{dom[1]},{dom[2]},0.18), rgba(0,0,0,0.12))'
    
    css_block = f"""/* AUTO-GENERATED THEME VARIABLES - run scripts/extract_palette.py to update */
:root {{
  --accent: {accent};
  --accent-dark: {accent_dark};
  --hero-overlay: {overlay};
  --hero-text: {hero_text};
}}
/* END AUTO-GENERATED THEME VARIABLES */

"""
    
    css_path = 'css/styles.css'
    if os.path.exists(css_path):
        with open(css_path, 'r', encoding='utf-8') as f:
            content = f.read()
        start = content.find('/* AUTO-GENERATED THEME VARIABLES')
        if start != -1:
            end = content.find('/* END AUTO-GENERATED THEME VARIABLES */', start)
            if end != -1:
                content = content[:start] + content[end + len('/* END AUTO-GENERATED THEME VARIABLES */') + 1:]
    else:
        content = ''
    
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_block + content)
    
    print(f'✓ Wrote theme variables to {css_path}')
    print(f'  Dominant color: {accent}')
    print(f'  Accent dark: {accent_dark}')
    print(f'  Hero text: {hero_text}')
    print(f'  Luminance: {L:.2f}')
