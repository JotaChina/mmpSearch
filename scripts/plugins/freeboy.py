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
            instruments = []

            # Para cada faixa, processar seus instrumenttracks
            for instrumenttrack in track.findall('./instrumenttrack'):
                instrument_info = {}

                # Extraindo os atributos do <instrumenttrack>
                instrument_info['instrumenttrack'] = {
                    'pitch': instrumenttrack.attrib.get('pitch', 'N/A'),
                    'pan': instrumenttrack.attrib.get('pan', 'N/A'),
                    'pitchrange': instrumenttrack.attrib.get('pitchrange', 'N/A'),
                    'basenote': instrumenttrack.attrib.get('basenote', 'N/A'),
                    'vol': instrumenttrack.attrib.get('vol', 'N/A'),
                    'fxch': instrumenttrack.attrib.get('fxch', 'N/A'),
                    'usemasterpitch': instrumenttrack.attrib.get('usemasterpitch', 'N/A')
                }

                # Adicionando suporte para o plugin "papu" (FreeBoy)
                instrument = instrumenttrack.find('.//instrument')
                if instrument is not None:
                    instrument_name = instrument.attrib.get('name', 'N/A')
                    instrument_info['instrument_name'] = instrument_name
                    
                    # Verificar se é o "papu" (FreeBoy) e extrair os atributos
                    if instrument_name.lower() == "papu":
                        papu = instrument.find('.//papu')  # Buscando pelo plugin "papu"
                        if papu is not None:
                            instrument_info['papu'] = {}
                            for key, value in papu.attrib.items():
                                instrument_info['papu'][key] = value

                # Extraindo os dados do <eldata>
                eldata = instrumenttrack.find('.//eldata')
                if eldata is not None:
                    instrument_info['eldata'] = {
                        'fwet': eldata.attrib.get('fwet', 'N/A'),
                        'ftype': eldata.attrib.get('ftype', 'N/A'),
                        'fcut': eldata.attrib.get('fcut', 'N/A'),
                        'fres': eldata.attrib.get('fres', 'N/A')
                    }

                    # Extraindo os elementos <elvol>, <elcut>, <elres>
                    for el in ['elvol', 'elcut', 'elres']:
                        el_element = eldata.find('.//' + el)
                        if el_element is not None:
                            instrument_info[el] = {}
                            for key, value in el_element.attrib.items():
                                instrument_info[el][key] = value

                # Extraindo dados do <chordcreator>, <arpeggiator>, <midiport>, <fxchain>
                for tag_name in ['chordcreator', 'arpeggiator', 'midiport', 'fxchain']:
                    tag_element = instrumenttrack.find('.//' + tag_name)
                    if tag_element is not None:
                        instrument_info[tag_name] = {}
                        for key, value in tag_element.attrib.items():
                            instrument_info[tag_name][key] = value

                instruments.append(instrument_info)

            # Adiciona a faixa com os instrumentos
            track_info.append({
                'track_name': track_name,
                'type': track_type,
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
