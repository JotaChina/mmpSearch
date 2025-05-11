import os
import zipfile
import json
import sys

# Adiciona o diretório onde está o file_parser.py ao sys.path para que possamos importar de lá
sys.path.append('/home/jotachina/Área de Trabalho/mmpSearch/scripts/handler')

# Agora podemos importar a função corretamente
from file_parser import parse_mmp_file

def gerar_metadados(mmp_data, destino_metadata):
    metadata = {
        "arquivo": mmp_data['file'],
        "caminho_origem": mmp_data['src'],
        "bpm": mmp_data['bpm'],
        "tags": mmp_data['tags'],
        "tracks": mmp_data['tracks'],
        "criado_em": "2025-05-10T15:05:00",  # Data fictícia; pode ser gerada automaticamente
        "versao_projeto": "1.0"
    }

    # Salva os metadados em formato JSON
    with open(destino_metadata, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=4)
    
    print(f'Metadados salvos em {destino_metadata}')


def empacotar_projeto_com_metadados(diretorio_projeto, destino_pacote, mmp_data):
    # Caminho para o arquivo de metadados
    destino_metadata = os.path.join(diretorio_projeto, f"{mmp_data['file']}.json")

    # Gera os metadados
    gerar_metadados(mmp_data, destino_metadata)

    # Empacota o projeto (incluindo o arquivo de metadados)
    with zipfile.ZipFile(destino_pacote, 'w', zipfile.ZIP_DEFLATED) as pacote:
        for pasta_raiz, _, arquivos in os.walk(diretorio_projeto):
            for arquivo in arquivos:
                caminho_completo = os.path.join(pasta_raiz, arquivo)
                caminho_relativo = os.path.relpath(caminho_completo, diretorio_projeto)
                pacote.write(caminho_completo, caminho_relativo)

    print(f'Projeto empacotado com sucesso: {destino_pacote}')


# Função principal para rodar o empacotamento
def empacotar():
    # Caminho para o arquivo MMP
    arquivo_mmp = '/home/jotachina/Área de Trabalho/mmpSearch/mmp/beatJulioCesardeSousa.mmp'
    
    # Chama o parse do arquivo MMP  
    mmp_data = parse_mmp_file(arquivo_mmp)
    
    if mmp_data is None:
        print("Erro ao processar o arquivo MMP")
        return  
    
    # Diretório do projeto
    diretorio_projeto = os.path.dirname(arquivo_mmp)

    # Caminho para o arquivo ZIP de destino
    destino_pacote = f"{mmp_data['file']}.mmpkg"

    # Empacotamento
    empacotar_projeto_com_metadados(diretorio_projeto, destino_pacote, mmp_data)


if __name__ == '__main__':
    empacotar()
