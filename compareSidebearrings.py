# MenuTitle: Compare All Source Sidebearings
# -*- coding: utf-8 -*-
# Written it based on Rainer Erich Scheichelbauer's Compare Sidebearings script. 
from __future__ import division, print_function, unicode_literals

font = Glyphs.font
tolerance = 2.0

Glyphs.clearLog()
Glyphs.showMacroWindow()

count = 0

for i, m1 in enumerate(font.masters):
    for m2 in font.masters[i+1:]:
        print(f"\n{m1.name} ↔ {m2.name}:")
        
        for glyph in font.glyphs:
            l1, l2 = glyph.layers[m1.id], glyph.layers[m2.id]
            if abs(l1.LSB - l2.LSB) > tolerance or abs(l1.RSB - l2.RSB) > tolerance:
                print(f"  /{glyph.name}: LSB {l1.LSB}↔{l2.LSB}, RSB {l1.RSB}↔{l2.RSB}")
                glyph.color = 0  # 0 = red color index in Glyphs
                count += 1

print(f"\nMarked {count} glyphs in red")