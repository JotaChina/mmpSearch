import os
import yaml
import json
from collections import defaultdict

current_dir = os.path.dirname(__file__)
data_dir = os.path.abspath(os.path.join(current_dir, '..', '_data'))
if not os.path.exists(data_dir):
    raise FileNotFoundError(f'O diretório {data_dir} não foi encontrado.')

instruments_count = defaultdict(int)
similar_files = defaultdict(list) 

def load_yaml(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

for filename in os.listdir(data_dir):
    if filename.endswith('.yml') or filename.endswith('.yaml'):
        file_path = os.path.join(data_dir, filename)
        data = load_yaml(file_path)
        
        bpm = data.get('bpm', 'N/A')
        file_name = data.get('file', 'N/A')
        tracks = data.get('tracks', [])
        
        for track in tracks:
            track_name = track.get('track_name', 'N/A')
            instruments = track.get('instruments', [])
            
            for instrument in instruments:
                instrument_name = instrument.get('instrument_name', 'N/A')
                instruments_count[instrument_name] += 1
                if file_name not in similar_files[instrument_name]:
                    similar_files[instrument_name].append(file_name)
output_data = []
for instrument_name, count in instruments_count.items():
    output_data.append({
        'instrument_name': instrument_name,
        'count': count,
        'files': similar_files[instrument_name]
    })

current_dir = os.path.dirname(__file__)
data_dir = os.path.abspath(os.path.join(current_dir, '..', '_data'))
output_file = os.path.join(data_dir, 'processed_data.json')

with open(output_file, 'w') as outfile:
    json.dump(output_data, outfile, indent=4)
print(f"Dados processados e salvos em {output_file}")