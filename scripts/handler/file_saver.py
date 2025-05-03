# file_saver.py

import json
import yaml

def save_to_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def save_to_yaml(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(data, f)
