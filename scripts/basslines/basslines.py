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

            # Verificando se o track é do tipo 'Beat/Bassline' (track_type == '1')
            if track_type == '1':  # Beat/Bassline
                bbtrack = track.find('./bbtrack')
                if bbtrack is not None:
                    bbtrack_info = []

                    # Iterando sobre cada container dentro de bbtrack
                    for container in bbtrack.findall('./trackcontainer'):
                        # Cada track dentro de trackcontainer
                        for instrument_track in container.findall('./track'):
                            instrument_info = {}
                            instrument_info['instrument_name'] = instrument_track.attrib.get('name', 'N/A')

                            # Extraindo informações do <instrumenttrack>
                            instrumenttrack = instrument_track.find('./instrumenttrack')
                            if instrumenttrack is not None:
                                instrument_info['pitch'] = instrumenttrack.attrib.get('pitch', '')
                                instrument_info['pan'] = instrumenttrack.attrib.get('pan', '')
                                instrument_info['vol'] = instrumenttrack.attrib.get('vol', '')
                                instrument_info['pitchrange'] = instrumenttrack.attrib.get('pitchrange', '')
                                instrument_info['basenote'] = instrumenttrack.attrib.get('basenote', '')
                                instrument_info['fxch'] = instrumenttrack.attrib.get('fxch', '')
                                instrument_info['usemasterpitch'] = instrumenttrack.attrib.get('usemasterpitch', '')

                            # Extraindo dados de audiofileprocessor
                            audiofileprocessor = instrument_track.find('.//audiofileprocessor')
                            if audiofileprocessor is not None:
                                instrument_info['audiofileprocessor'] = {
                                    'amp': audiofileprocessor.attrib.get('amp', ''),
                                    'src': audiofileprocessor.attrib.get('src', ''),
                                    'lframe': audiofileprocessor.attrib.get('lframe', ''),
                                    'stutter': audiofileprocessor.attrib.get('stutter', ''),
                                    'interp': audiofileprocessor.attrib.get('interp', ''),
                                    'sframe': audiofileprocessor.attrib.get('sframe', ''),
                                    'looped': audiofileprocessor.attrib.get('looped', ''),
                                    'eframe': audiofileprocessor.attrib.get('eframe', ''),
                                    'reversed': audiofileprocessor.attrib.get('reversed', ''),
                                }

                            # Extraindo dados de eldata
                            eldata = instrument_track.find('./eldata')
                            if eldata is not None:
                                eldata_info = {
                                    'fwet': eldata.attrib.get('fwet', ''),
                                    'ftype': eldata.attrib.get('ftype', ''),
                                    'fcut': eldata.attrib.get('fcut', ''),
                                    'fres': eldata.attrib.get('fres', ''),
                                }
                                elvol = eldata.find('./elvol')
                                if elvol is not None:
                                    eldata_info['elvol'] = {
                                        'sustain': elvol.attrib.get('sustain', ''),
                                        'lamt': elvol.attrib.get('lamt', ''),
                                        'lshp': elvol.attrib.get('lshp', ''),
                                        'amt': elvol.attrib.get('amt', ''),
                                        'pdel': elvol.attrib.get('pdel', ''),
                                        'lpdel': elvol.attrib.get('lpdel', ''),
                                        'lspd_numerator': elvol.attrib.get('lspd_numerator', ''),
                                        'lspd_syncmode': elvol.attrib.get('lspd_syncmode', ''),
                                        'latt': elvol.attrib.get('latt', ''),
                                        'ctlenvamt': elvol.attrib.get('ctlenvamt', ''),
                                        'x100': elvol.attrib.get('x100', ''),
                                        'dec': elvol.attrib.get('dec', ''),
                                        'hold': elvol.attrib.get('hold', ''),
                                        'rel': elvol.attrib.get('rel', ''),
                                        'lspd_denominator': elvol.attrib.get('lspd_denominator', ''),
                                        'userwavefile': elvol.attrib.get('userwavefile', ''),
                                        'att': elvol.attrib.get('att', ''),
                                        'lspd': elvol.attrib.get('lspd', '')
                                    }
                                # Extraindo elcut e elres de forma similar
                                elcut = eldata.find('./elcut')
                                if elcut is not None:
                                    eldata_info['elcut'] = {
                                        'cutoff': elcut.attrib.get('cutoff', ''),
                                        'q': elcut.attrib.get('q', ''),
                                    }

                                elres = eldata.find('./elres')
                                if elres is not None:
                                    eldata_info['elres'] = {
                                        'res': elres.attrib.get('res', ''),
                                    }

                                instrument_info['eldata'] = eldata_info

                            # Extraindo dados de chordcreator
                            chordcreator = instrument_track.find('./chordcreator')
                            if chordcreator is not None:
                                chordcreator_info = {
                                    'chord_enabled': chordcreator.attrib.get('chord-enabled', ''),
                                    'chordrange': chordcreator.attrib.get('chordrange', ''),
                                    'chord': chordcreator.attrib.get('chord', '')
                                }
                                instrument_info['chordcreator'] = chordcreator_info

                            # Extraindo dados de arpeggiator
                            arpeggiator = instrument_track.find('./arpeggiator')
                            if arpeggiator is not None:
                                arpeggiator_info = {
                                    'arptime': arpeggiator.attrib.get('arptime', ''),
                                    'arpmode': arpeggiator.attrib.get('arpmode', ''),
                                    'arp': arpeggiator.attrib.get('arp', ''),
                                    'arprange': arpeggiator.attrib.get('arprange', '')
                                }
                                instrument_info['arpeggiator'] = arpeggiator_info

                            # Extraindo dados de midiport
                            midiport = instrument_track.find('./midiport')
                            if midiport is not None:
                                midiport_info = {
                                    'outputprogram': midiport.attrib.get('outputprogram', ''),
                                    'inputchannel': midiport.attrib.get('inputchannel', ''),
                                    'outputcontroller': midiport.attrib.get('outputcontroller', ''),
                                    'inputcontroller': midiport.attrib.get('inputcontroller', ''),
                                    'outputchannel': midiport.attrib.get('outputchannel', ''),
                                    'writable': midiport.attrib.get('writable', ''),
                                    'fixedinputvelocity': midiport.attrib.get('fixedinputvelocity', ''),
                                    'basevelocity': midiport.attrib.get('basevelocity', ''),
                                    'readable': midiport.attrib.get('readable', ''),
                                    'fixedoutputvelocity': midiport.attrib.get('fixedoutputvelocity', ''),
                                    'fixedoutputnote': midiport.attrib.get('fixedoutputnote', '')
                                }
                                instrument_info['midiport'] = midiport_info

                            # Adicionando o instrumento ao bbtrack_info
                            bbtrack_info.append(instrument_info)

                    # Se não encontrar instrumentos, ainda adicionamos a track vazia
                    track_info.append({
                        'track_name': track_name,
                        'type': 'bassline',
                        'instruments': bbtrack_info if bbtrack_info else [],
                    })

            else:
                # Adiciona os outros tipos de track (caso necessário)
                instruments.append({
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
