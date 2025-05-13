import os
import zipfile
import json
import sys
import datetime
import xml.etree.ElementTree as ET

# Adiciona o diretório onde está o file_parser.py ao sys.path para que possamos importar de lá
sys.path.append('/home/jotachina/Projetos/mmpSearch/scripts/handler')

# Agora podemos importar a função corretamente
from file_parser import parse_mmp_file

def gerar_metadados(mmp_path, destino_metadata):
    import os

    # Parse do arquivo XML .mmp
    tree = ET.parse(mmp_path)
    root = tree.getroot()

    # Data e hora atual
    hoje = datetime.datetime.now()
    fhoje = hoje.strftime("%Y-%m-%dT%H:%M:%S")

    # Versão do LMMS
    versao_lmms = root.attrib.get('creatorversion', 'desconhecida')

    # BPM e faixas
    head = root.find('head')
    bpm = int(head.attrib.get('bpm', 0)) if head is not None else 0

    track_names = []
    for track in root.findall('.//track'):
        name = track.attrib.get('name')
        if name:
            track_names.append(name)

    # Metadados em <projectnotes> #tenho que salvar o projeto0 no arquivo mmp sendo processado
    projectnotes = root.find('.//projectnotes')
    texto_notes = (projectnotes.text or "").lower() if projectnotes is not None else ""

    autor = "autor:" if "autor" in texto_notes else "não encontrado"
    nome_faixa = "nome da faixa:" if "nome da faixa" in texto_notes else "não encontrado"
    genero = "gênero:" if "gênero" in texto_notes else "não encontrado"

    # Projeto0: verificar presença e versão
    if "projeto0" in texto_notes:

        # Tenta incrementar versão
        versao_str = root.attrib.get("version", "1.0")
        try:
            nova_versao = f"{float(versao_str) + 0.1:.1f}" #na verdade, a versão deve verificar o all.json, projeto0 = projeto0atual. 
        except ValueError:                                 #sendo assim, pode atualizar a versão_projeto0
            nova_versao = "1.1"
    else:
        projeto0_status = mmp_path
        nova_versao = root.attrib.get("version", "1.0")

    # Construção do JSON
    metadata = {
        "tags_track": {
            "autor": autor,
            "nome_da_faixa": nome_faixa,
            "genero": genero,
            "projeto0": projeto0_status,
            "criado_em": fhoje,
            "versao_projeto": nova_versao,
            "versao_lmms": versao_lmms
        },
        
    }

    # Salva JSON
    with open(destino_metadata, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=4)

    print(f'Metadados salvos em {destino_metadata}')


def empacotar_projeto_com_metadados(diretorio_projeto, destino_pacote, mmp_data):
    # Caminhos dos arquivos
    mmp_path = mmp_data['src']
    destino_metadata = os.path.join(diretorio_projeto, f"{mmp_data['file']}.json")

    # Gera os metadados
    gerar_metadados(mmp_path, destino_metadata)

    # Empacota apenas o .mmp e o .json
    with zipfile.ZipFile(destino_pacote, 'w', zipfile.ZIP_DEFLATED) as pacote:
        pacote.write(mmp_path, os.path.basename(mmp_path))
        pacote.write(destino_metadata, os.path.basename(destino_metadata))

    print(f'Projeto empacotado com sucesso: {destino_pacote}')

import shutil

def empacotar():
    # Pasta onde estão os arquivos .mmp
    pasta_mmp = '/home/jotachina/Projetos/mmpSearch/mmp'

    # Itera sobre todos os arquivos .mmp
    for nome_arquivo in os.listdir(pasta_mmp):
        if nome_arquivo.endswith('.mmp'):
            caminho_mmp_original = os.path.join(pasta_mmp, nome_arquivo)

            # Parse do arquivo MMP
            mmp_data = parse_mmp_file(caminho_mmp_original)
            if mmp_data is None:
                print(f"Erro ao processar o arquivo MMP: {caminho_mmp_original}")
                continue

            # Cria uma subpasta com o nome do arquivo (sem extensão)
            nome_base = os.path.splitext(nome_arquivo)[0]
            subpasta_projeto = os.path.join(pasta_mmp, nome_base)
            os.makedirs(subpasta_projeto, exist_ok=True)

            # Copia o arquivo .mmp para a nova pasta
            caminho_mmp_novo = os.path.join(subpasta_projeto, nome_arquivo)
            shutil.copy2(caminho_mmp_original, caminho_mmp_novo)

            # Atualiza caminho no dicionário mmp_data
            mmp_data['src'] = caminho_mmp_novo
            mmp_data['file'] = nome_arquivo

            # Caminho do arquivo .mmpkg dentro da subpasta
            destino_pacote = os.path.join(subpasta_projeto, f"{nome_base}.mmpkg")

            # Empacota o projeto com os metadados
            empacotar_projeto_com_metadados(subpasta_projeto, destino_pacote, mmp_data)

if __name__ == '__main__':
    empacotar()
