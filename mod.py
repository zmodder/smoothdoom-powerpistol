#!/usr/bin/python3

import os
import re

os.rename('build/DECO/PLAYER/Pistol.txt', 'build/DECO/PLAYER/Pistol.txt.orig')
a_firepistol_pattern = re.compile(r'(\s*)(\w+) (\w+) (\d+) A_FirePistol')
with open('build/DECO/PLAYER/Pistol.txt.orig') as in_file:
    with open('build/DECO/PLAYER/Pistol.txt', 'w') as out_file:
        for line_terminated in in_file:
            line = line_terminated.rstrip('\n')
            m = a_firepistol_pattern.match(line)
            if m != None:
                indent = m.group(1)
                sprite = m.group(2)
                frame = m.group(3)
                tick = int(m.group(4))
                # Based on the original equivalent of A_FirePistol,
                # with damage increased from 5 to 7.
                # Numeric arguments: spread_horz, spread_vert, numbullets, damage
                # A_FireBullets (5.6, 0, 1, 5, "BulletPuff")
                out_file.write('%s%s %s %d %s\n' % (
                    indent, sprite, frame, tick,
                    'A_FireBullets (5.6, 0, 1, 7, "BulletPuff")'))
                out_file.write('%s%s %s %d %s\n' % (
                    indent, sprite, frame, 0,
                    'A_PlaySound ("weapons/ppstol", CHAN_WEAPON)'))
                out_file.write('%s%s %s %d %s\n' % (indent, sprite, frame, 0,
                    'A_GunFlash'))
            else:
                out_file.write(line)
                out_file.write('\n')

os.rename('build/DECO/MONSTERS/Zombieman.txt', 'build/DECO/MONSTERS/Zombieman.txt.orig')
a_posattack_pattern = re.compile(r'(.*)A_PosAttack')
with open('build/DECO/MONSTERS/Zombieman.txt.orig') as in_file:
    with open('build/DECO/MONSTERS/Zombieman.txt', 'w') as out_file:
        for line_terminated in in_file:
            line = line_terminated.rstrip('\n')
            m = a_posattack_pattern.match(line)
            if m != None:
                prefix = m.group(1)
                # Based on the original equivalent of A_PosAttack
                # with damage increased from [3, 15] to [3, 21], and the pistol sound
                out_file.write(
                    prefix + 'A_CustomBulletAttack (22.5, 0, 1, random(1,7) * 3, "BulletPuff", 0, CBAF_NORANDOM)\n')
            else:
                out_file.write(line)
                out_file.write('\n')

with open('build/SNDINFO', 'a') as f:
    f.write('\n')
    f.write('weapons/ppstol          SOUNDS/D3PISTOL\n')
    f.write('grunt/attack            SOUNDS/DSGNFIRE\n')
    f.write('chainguy/attack         DSPISTOL\n')
    f.write('wolfss/attack           DSPISTOL\n')
    f.write('spider/attack           SOUNDS/D3CHNGUN\n')
