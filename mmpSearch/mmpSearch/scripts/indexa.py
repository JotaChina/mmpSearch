import os
import json
import yaml  
import subprocess
import xml.etree.ElementTree as ET
import shutil

def parse_mmp_file(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        bpm = root.find('./head').attrib.get('bpm', 'N/A')

        tracks = root.findall('./song/trackcontainer/track')
        track_info = []

        for track in tracks:
            track_name = track.attrib.get('name', 'N/A')
            track_type = track.attrib.get('type')

            if track_name:
                instruments = []

                if track_type == '0':  # Faixa do tipo plugin
                    track_info.append({
                        'track_name': track_name,
                        'type': 'plugin',
                        'instruments': [],
                    })

                elif track_type == '2':  # Faixa do tipo Sample Track
                    track_info.append({
                        'track_name': track_name,
                        'type': 'sample',
                        'instruments': [],
                    })

                elif track_type == '1':  # Faixa do tipo Beat/Bassline
                    bbtrack = track.find('./bbtrack')
                    if bbtrack is not None:
                        trackcontainers = bbtrack.findall('./trackcontainer')
                        for container in trackcontainers:
                            instrument_tracks = container.findall('./track')
                            for instrument_track in instrument_tracks:
                                instrument_name = instrument_track.attrib.get('name', 'N/A')
                                instruments.append({
                                    'instrument_name': instrument_name,
                                })

                        track_info.append({
                            'track_name': track_name,
                            'type': 'bassline',
                            'instruments': instruments,
                        })

        return {
            'file': file_path,
            'bpm': bpm,
            'tracks': track_info
        }

    except ET.ParseError as e:
        print(f'Erro ao analisar o arquivo XML {file_path}: {e}')
        return None

def process_mmps_in_folder(folder_path):
    mmp_files = [f for f in os.listdir(folder_path) if f.endswith('.mmp') or f.endswith('.mmpz')]
    all_data = []

    mmpz_folder = os.path.join(folder_path, 'mmpz')
    if not os.path.exists(mmpz_folder):
        os.makedirs(mmpz_folder)

    for file in mmp_files:
        file_path = os.path.join(folder_path, file)
        print(f'Processando arquivo: {file_path}')

        if file.endswith('.mmpz'):
            destination_path = os.path.join(mmpz_folder, file)
            shutil.move(file_path, destination_path)
            print(f'Arquivo {file} movido para {destination_path}')

            file_name = os.path.basename(destination_path)
            file_name = os.path.splitext(file_name)[0] + ".mmp"
            output_file_path = os.path.join(folder_path, file_name)
            comando = f'lmms --dump "{destination_path}" > "{output_file_path}"'
            try:
                os.environ['QT_DEBUG_PLUGINS'] = '1'
                os.environ['QT_QPA_PLATFORM'] = 'offscreen'
                subprocess.run(comando, shell=True, check=True)
                print("Comando executado com sucesso!")
            except subprocess.CalledProcessError as e:
                print(f"Ocorreu um erro ao executar o comando: {e}")

            mmp_data = parse_mmp_file(output_file_path)  
        elif file.endswith('.mmp'):
            mmp_data = parse_mmp_file(file_path)  

        if mmp_data:
            all_data.append(mmp_data)

            json_file_name = os.path.splitext(file)[0] + ".json"
            json_file_path = os.path.join('metadata', json_file_name)
            save_to_json(mmp_data, json_file_path)

            yaml_file_name = os.path.splitext(file)[0] + ".yml"
            yaml_file_path = os.path.join('_data', yaml_file_name)
            save_to_yaml(mmp_data, yaml_file_path)

    return all_data

def save_to_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def save_to_yaml(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(data, f)

mmp_folder_path = 'mmp'
processed_data = process_mmps_in_folder(mmp_folder_path)
print("Processamento concluído.")
