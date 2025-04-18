import xml.etree.ElementTree as ET

def parse_instrument(instrumenttrack_element):
    instrument_info = {}

    # Atributos básicos do <instrumenttrack>
    instrument_info['instrumenttrack'] = {
        'pitch': instrumenttrack_element.attrib.get('pitch', 'N/A'),
        'pan': instrumenttrack_element.attrib.get('pan', 'N/A'),
        'pitchrange': instrumenttrack_element.attrib.get('pitchrange', 'N/A'),
        'basenote': instrumenttrack_element.attrib.get('basenote', 'N/A'),
        'vol': instrumenttrack_element.attrib.get('vol', 'N/A'),
        'fxch': instrumenttrack_element.attrib.get('fxch', 'N/A'),
        'usemasterpitch': instrumenttrack_element.attrib.get('usemasterpitch', 'N/A')
    }

    # Verifica se o instrumento contém o nome
    instrument = instrumenttrack_element.find('.//instrument')
    if instrument is not None:
        instrument_name = instrument.attrib.get('name', 'N/A')
        instrument_info['instrument_name'] = instrument_name

        # Verifica o plugin "tripleoscillator"
        tripleoscillator = instrument.find('.//tripleoscillator')
        if tripleoscillator is not None:
            instrument_info['tripleoscillator'] = {}
            for key, value in tripleoscillator.attrib.items():
                instrument_info['tripleoscillator'][key] = value

    # Extraindo os dados do <eldata>
    eldata = instrumenttrack_element.find('.//eldata')
    if eldata is not None:
        instrument_info['eldata'] = {
            'fwet': eldata.attrib.get('fwet', 'N/A'),
            'ftype': eldata.attrib.get('ftype', 'N/A'),
            'fcut': eldata.attrib.get('fcut', 'N/A'),
            'fres': eldata.attrib.get('fres', 'N/A')
        }

        for el in ['elvol', 'elcut', 'elres']:
            el_element = eldata.find(f'.//{el}')
            if el_element is not None:
                instrument_info[el] = {
                    key: value for key, value in el_element.attrib.items()
                }

    # Componentes auxiliares
    for tag in ['chordcreator', 'arpeggiator', 'midiport', 'fxchain']:
        tag_element = instrumenttrack_element.find(f'.//{tag}')
        if tag_element is not None:
            instrument_info[tag] = {
                key: value for key, value in tag_element.attrib.items()
            }

    return instrument_info
