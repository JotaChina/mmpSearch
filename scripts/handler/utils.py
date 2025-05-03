# utils.py

import os

SUPPORTED_PLUGINS = [
    'audiofileprocessor', 'bitinvader', 'freeboy', 'papu', 'gigplayer', 'kicker', 'lb302', 'malletsstk',
    'monstro', 'nes', 'opl2', 'organic', 'patman', 'sf2player', 'sfxr', 'sid',
    'tripleoscillator', 'vibedstrings', 'watsyn', 'zynaddsubfx'
]

tags = {}
tags['TAG'] = []
tags['plugin'] = []
tags['sample'] = []
tags['bassline'] = []
tags['automation'] = []

def create_folders_if_not_exist(folders):
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
