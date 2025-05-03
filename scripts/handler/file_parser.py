import os
import xml.etree.ElementTree as ET
import importlib

from automations.automations import parse_automation
from basslines.basslines import parse_basslines
from samples.samples import parse_samples
from utils import SUPPORTED_PLUGINS

# Lista dos plugins suportados

def parse_mmp_file(file_path):
    if not os.path.exists(file_path):
        print(f"O arquivo {file_path} não existe!")
        return None

    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        bpm = root.find('./head').attrib.get('bpm', 'N/A')
        tracks = root.findall('./song/trackcontainer/track')
        track_info = []
        tags = {}
        tags['TAG'] = []
        tags['plugin'] = []
        tags['sample'] = []
        tags['bassline'] = []
        tags['automation'] = []

        for track in tracks:
            track_name = track.attrib.get('name', 'N/A')
            track_type = track.attrib.get('type')

            if track_type == '0':
                # Faixas de instrumento
                # Tem que verificar o sf2, verificar caminhos dos samples.
                instruments = track.findall('./instrumenttrack')
                for instrumenttrack in instruments:
                    instrument = instrumenttrack.find('.//instrument')
                    if instrument is not None:
                        plugin_name = instrument.attrib.get('name')
                        if plugin_name:
                            plugin_info = parse_plugin_track(instrumenttrack, plugin_name)
                            if plugin_info:
                                # Adiciona metadados da faixa também
                                plugin_info['track_name'] = track_name
                                plugin_info['type'] = 'plugin'
                                track_info.append(plugin_info)
                                # Marcando os nomes dos plugins presentes
                                if 'plugin' not in tags['TAG']:                                    
                                    tags['TAG'].append('plugin')
                                # Se algum plugin estiver com o nome diferente do original
                                if track_name not in tags:
                                    if (track_name not in SUPPORTED_PLUGINS and
                                        plugin_name not in tags['plugin']):                         
                                        tags['plugin'].append(plugin_name)                                    

            elif track_type == '1':  # Bassline (aparentemente, correto)
                bassline_info = parse_basslines(track)
                if bassline_info:
                    track_info.append(bassline_info)
                    if bassline_info['tags'] is not None:
                        if 'bassline' not in tags['TAG']: #certo
                            tags['TAG'].append('bassline')
                        if track_name not in tags['TAG']: #certo
                            tags['bassline'].append(track_name) 
                        if 'audiofileprocessor' not in tags['plugin']: #certo
                            tags['plugin'].append(bassline_info['tags'])                                                
                        if 'tripleoscillator' not in tags['plugin']:
                            if bassline_info['tags'] == 'tripleoscillator':
                                tags['plugin'].append(bassline_info['tags'])  
                            
                                                                        
            elif track_type == '2':  # Sample (aparentemente, correto)
                sample_info = parse_samples(file_path, track)
                if sample_info:
                    track_info.append(sample_info)
                    if 'sample' not in tags['TAG']:                    
                        tags['TAG'].append('sample')
                    sample_name = sample_info['sample_name']
                    if sample_name == None:
                        sample_name = track_name
                    tags['sample'].append(sample_name)

            elif track_type in ['5', '6']:  # Automation (aparentemente, correto)
                automation_info = parse_automation(file_path)
                if automation_info:
                    track_info.append(automation_info)
                    if 'automation' not in tags['TAG']:
                        tags['TAG'].append('automation')
                    tags['automation'].append(track_name)

            else:
                print('\n\n\n\n\n\nERRO\n\n\n\n\n\n')
                return                   
        
        file_name_with_extension = os.path.basename(file_path)
        file_name, _ = os.path.splitext(file_name_with_extension)

        return {
            'file': file_name,
            'src': file_path,
            'bpm': bpm,
            'tags': tags,
            'tracks': track_info
        }

    except ET.ParseError as e:
        print(f'Erro ao analisar o arquivo XML {file_path}: {e}')
        return None


def parse_generic_track(track):
    track_name = track.attrib.get('name', 'N/A')
    track_type = track.attrib.get('type')

    return {
        'track_name': track_name,
        'type': track_type,
        'instruments': []
    }


def parse_plugin_track(instrumenttrack_element, plugin_name):
    plugin_name = plugin_name.lower()

    if plugin_name not in SUPPORTED_PLUGINS:
        return {'error': f"Plugin '{plugin_name}' não está na lista de suportados"}

    try:
        module_path = f"plugins.{plugin_name}"
        plugin_module = importlib.import_module(module_path)

        if hasattr(plugin_module, 'parse_instrument'):
            return plugin_module.parse_instrument(instrumenttrack_element)
        else:
            return {'error': f"O plugin '{plugin_name}' não possui a função 'parse_instrument'"}

    except ModuleNotFoundError:
        return {'error': f"Módulo do plugin '{plugin_name}' não encontrado"}
    except Exception as e:
        return {'error': f"Erro ao carregar plugin '{plugin_name}': {e}"}
