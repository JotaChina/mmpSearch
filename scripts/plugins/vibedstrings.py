import xml.etree.ElementTree as ET

def parse_instrument(instrumenttrack_element):
    try:
        instrument_info = {}

        # Extraindo os atributos do <instrumenttrack>
        instrument_info['instrumenttrack'] = {
            'pitch': instrumenttrack_element.attrib.get('pitch', 'N/A'),
            'pan': instrumenttrack_element.attrib.get('pan', 'N/A'),
            'pitchrange': instrumenttrack_element.attrib.get('pitchrange', 'N/A'),
            'basenote': instrumenttrack_element.attrib.get('basenote', 'N/A'),
            'vol': instrumenttrack_element.attrib.get('vol', 'N/A'),
            'fxch': instrumenttrack_element.attrib.get('fxch', 'N/A'),
            'usemasterpitch': instrumenttrack_element.attrib.get('usemasterpitch', 'N/A')
        }

        # Extraindo o instrumento e verificando se é o plugin "vibedstrings" ou "tripleoscillator"
        instrument = instrumenttrack_element.find('.//instrument')
        if instrument is not None:
            instrument_name = instrument.attrib.get('name', 'N/A')
            instrument_info['instrument_name'] = instrument_name
            
            # Verificar se é o "vibedstrings" e extrair os atributos
            if instrument_name.lower() == "vibedstrings":
                vibedstrings = instrument.find('.//vibedstrings')  # Buscando pelo plugin "vibedstrings"
                if vibedstrings is not None:
                    instrument_info['vibedstrings'] = {}
                    for key, value in vibedstrings.attrib.items():
                        instrument_info['vibedstrings'][key] = value

        # Extraindo os dados do <eldata>
        eldata = instrumenttrack_element.find('.//eldata')
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
            tag_element = instrumenttrack_element.find('.//' + tag_name)
            if tag_element is not None:
                instrument_info[tag_name] = {}
                for key, value in tag_element.attrib.items():
                    instrument_info[tag_name][key] = value

        return instrument_info

    except ET.ParseError as e:
        print(f'Erro ao analisar o arquivo XML: {e}')
        return None
