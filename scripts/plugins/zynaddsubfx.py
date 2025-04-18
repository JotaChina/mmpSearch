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

        # Buscando o nome do plugin
        instrument = instrumenttrack_element.find('.//instrument')
        if instrument is not None:
            instrument_name = instrument.attrib.get('name', 'N/A')
            instrument_info['instrument_name'] = instrument_name
            
            # Caso seja o plugin "watsyn", extraímos informações específicas
            if instrument_name.lower() == "watsyn":
                watsyn = instrument.find('.//watsyn')  # Buscando pelo plugin "watsyn"
                if watsyn is not None:
                    instrument_info['watsyn'] = {}
                    for key, value in watsyn.attrib.items():
                        instrument_info['watsyn'][key] = value

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

        # Extraindo dados do <INSTRUMENT_EFFECTS>, <SYSTEM_EFFECTS>, <INSERTION_EFFECTS>
        instrument_effects = instrumenttrack_element.findall('.//INSTRUMENT_EFFECTS/INSTRUMENT_EFFECT')
        if instrument_effects:
            instrument_info['instrument_effects'] = []
            for effect in instrument_effects:
                effect_info = {}
                for param in effect.findall('.//par'):
                    effect_info[param.attrib['name']] = param.attrib['value']
                instrument_info['instrument_effects'].append(effect_info)

        system_effects = instrumenttrack_element.findall('.//SYSTEM_EFFECTS/SYSTEM_EFFECT')
        if system_effects:
            instrument_info['system_effects'] = []
            for effect in system_effects:
                effect_info = {}
                for param in effect.findall('.//par'):
                    effect_info[param.attrib['name']] = param.attrib['value']
                instrument_info['system_effects'].append(effect_info)

        insertion_effects = instrumenttrack_element.findall('.//INSERTION_EFFECTS/INSERTION_EFFECT')
        if insertion_effects:
            instrument_info['insertion_effects'] = []
            for effect in insertion_effects:
                effect_info = {}
                for param in effect.findall('.//par'):
                    effect_info[param.attrib['name']] = param.attrib['value']
                instrument_info['insertion_effects'].append(effect_info)

        # Extraindo dados do <CONTROLLER>
        controller = instrumenttrack_element.find('.//CONTROLLER')
        if controller is not None:
            instrument_info['controller'] = {}
            for param in controller.findall('.//par'):
                instrument_info['controller'][param.attrib['name']] = param.attrib['value']

        return instrument_info

    except Exception as e:
        print(f'Erro ao processar o instrumento: {e}')
        return {'error': f"Erro ao processar o instrumento: {e}"}
