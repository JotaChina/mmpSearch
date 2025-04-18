import xml.etree.ElementTree as ET

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

            # Verificando se o track é do tipo 'Automation' (track_type == '5' ou '6')
            if track_type in ['5', '6']:  # Faixas de automação
                automation_info = {
                    'track_name': track_name,
                    'type': 'automation',
                    'automation_patterns': []
                }

                # Lendo a tag <automationtrack>
                automationtrack = track.find('./automationtrack')
                if automationtrack is not None:
                    automation_info['automationtrack'] = 'Present'

                # Lendo as tags de automationpattern (caso existam)
                for automationpattern in track.findall('./automationpattern'):
                    automation_pattern_info = {
                        'name': automationpattern.attrib.get('name', 'N/A'),
                        'mute': automationpattern.attrib.get('mute', '0'),
                        'len': automationpattern.attrib.get('len', 'N/A'),
                        'pos': automationpattern.attrib.get('pos', '0'),
                        'prog': automationpattern.attrib.get('prog', '0'),
                        'tens': automationpattern.attrib.get('tens', '1'),
                        'times': []  # Inicializando uma lista para os tempos
                    }

                    # Extraindo os tempos dentro do <automationpattern>
                    for time in automationpattern.findall('./time'):
                        time_info = {
                            'value': time.attrib.get('value', 'N/A'),
                            'pos': time.attrib.get('pos', 'N/A')
                        }
                        automation_pattern_info['times'].append(time_info)

                    # Adicionando os padrões de automação ao track
                    automation_info['automation_patterns'].append(automation_pattern_info)

                track_info.append(automation_info)

        return {
            'file': file_path,
            'bpm': bpm,
            'tracks': track_info
        }

    except ET.ParseError as e:
        print(f'Erro ao analisar o arquivo XML {file_path}: {e}')
        return None
