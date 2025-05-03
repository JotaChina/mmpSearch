# main.py

import os
import shutil
import subprocess
from file_parser import parse_mmp_file
from file_saver import save_to_json, save_to_yaml
from utils import create_folders_if_not_exist

def process_mmps_in_folder(folder_path):
    mmp_files = [f for f in os.listdir(folder_path) if f.endswith('.mmp') or f.endswith('.mmpz')]
    all_data = []

    mmpz_folder = os.path.join(folder_path, '/nethome/jotachina/projetos/mmpSearch/mmp/mmpz')
    wav_folder = os.path.join(folder_path, '/nethome/jotachina/projetos/mmpSearch/mmp/wav')
    metadata_folder = os.path.join(folder_path, '/nethome/jotachina/projetos/mmpSearch/metadata')
    data_folder = os.path.join(folder_path, '/nethome/jotachina/projetos/mmpSearch/_data')

    create_folders_if_not_exist([mmpz_folder, wav_folder, metadata_folder, data_folder])

    for file in mmp_files:
        file_path = os.path.join(folder_path, file)
        print(f'Processando arquivo: {file_path}')

        if file.endswith('.mmpz'):
            destination_path = os.path.join(mmpz_folder, file)
            shutil.move(file_path, destination_path)
            print(f'Movido para: {destination_path}')

            mmp_name = os.path.splitext(file)[0] + ".mmp"
            output_mmp_path = os.path.join(folder_path, mmp_name)
            convert_cmd = f'lmms --dump "{destination_path}" > "{output_mmp_path}"'

            try:
                os.environ['QT_QPA_PLATFORM'] = 'offscreen'
                subprocess.run(convert_cmd, shell=True, check=True)
                print("Convertido para .mmp com sucesso!")
            except subprocess.CalledProcessError as e:
                print(f"Erro ao converter .mmpz para .mmp: {e}")

            wav_output_path = os.path.join(wav_folder, os.path.splitext(file)[0])
            wav_convert_cmd = f'lmms -r "{destination_path}" -o "{wav_output_path}" -f wav'

            try:
                subprocess.run(wav_convert_cmd, shell=True, check=True)
                print("Convertido para .wav com sucesso!")
            except subprocess.CalledProcessError as e:
                print(f"Erro ao converter .wav: {e}")

            mmp_data = parse_mmp_file(output_mmp_path)

        elif file.endswith('.mmp'):
            mmp_data = parse_mmp_file(file_path)

        if mmp_data:
            all_data.append(mmp_data)

            json_file_path = os.path.join(metadata_folder, os.path.splitext(file)[0] + ".json")
            yaml_file_path = os.path.join(data_folder, os.path.splitext(file)[0] + ".yml")

            save_to_yaml(mmp_data, yaml_file_path)
            save_to_json(mmp_data, json_file_path)

            print(f"Dados salvos: {json_file_path}, {yaml_file_path}")

    return all_data

mmp_folder_path = '/nethome/jotachina/projetos/mmpSearch/mmp'
processed_data = process_mmps_in_folder(mmp_folder_path)
save_to_json(processed_data, '/nethome/jotachina/projetos/mmpSearch/metadata/all.json')
save_to_yaml(processed_data, '/nethome/jotachina/projetos/mmpSearch/_data/all.yml')

print("Processamento concluído.")