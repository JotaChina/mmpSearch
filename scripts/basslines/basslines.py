def parse_basslines(track):
    track_name = track.attrib.get('name', 'N/A')
    bbtrack = track.find('./bbtrack')
    instruments = []

    if bbtrack is not None:
        for container in bbtrack.findall('./trackcontainer'):
            for instrument_track in container.findall('./track'):
                instrument_info = {}
                instrument_info['instrument_name'] = instrument_track.attrib.get('name', 'N/A')

                # <instrumenttrack>
                instrumenttrack = instrument_track.find('./instrumenttrack')
                if instrumenttrack is not None:
                    instrument_info.update({
                        'pitch': instrumenttrack.attrib.get('pitch', ''),
                        'pan': instrumenttrack.attrib.get('pan', ''),
                        'vol': instrumenttrack.attrib.get('vol', ''),
                        'pitchrange': instrumenttrack.attrib.get('pitchrange', ''),
                        'basenote': instrumenttrack.attrib.get('basenote', ''),
                        'fxch': instrumenttrack.attrib.get('fxch', ''),
                        'usemasterpitch': instrumenttrack.attrib.get('usemasterpitch', '')
                    })

                # <audiofileprocessor>
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

                # <eldata>
                eldata = instrument_track.find('./eldata')
                if eldata is not None:
                    eldata_info = {
                        'fwet': eldata.attrib.get('fwet', ''),
                        'ftype': eldata.attrib.get('ftype', ''),
                        'fcut': eldata.attrib.get('fcut', ''),
                        'fres': eldata.attrib.get('fres', '')
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

                    elcut = eldata.find('./elcut')
                    if elcut is not None:
                        eldata_info['elcut'] = {
                            'cutoff': elcut.attrib.get('cutoff', ''),
                            'q': elcut.attrib.get('q', '')
                        }

                    elres = eldata.find('./elres')
                    if elres is not None:
                        eldata_info['elres'] = {
                            'res': elres.attrib.get('res', '')
                        }

                    instrument_info['eldata'] = eldata_info

                # <chordcreator>
                chordcreator = instrument_track.find('./chordcreator')
                if chordcreator is not None:
                    instrument_info['chordcreator'] = {
                        'chord_enabled': chordcreator.attrib.get('chord-enabled', ''),
                        'chordrange': chordcreator.attrib.get('chordrange', ''),
                        'chord': chordcreator.attrib.get('chord', '')
                    }

                # <arpeggiator>
                arpeggiator = instrument_track.find('./arpeggiator')
                if arpeggiator is not None:
                    instrument_info['arpeggiator'] = {
                        'arptime': arpeggiator.attrib.get('arptime', ''),
                        'arpmode': arpeggiator.attrib.get('arpmode', ''),
                        'arp': arpeggiator.attrib.get('arp', ''),
                        'arprange': arpeggiator.attrib.get('arprange', '')
                    }

                # <midiport>
                midiport = instrument_track.find('./midiport')
                if midiport is not None:
                    instrument_info['midiport'] = {
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

                instruments.append(instrument_info)

    return {
        'track_name': track_name,
        'type': 'bassline',
        'instruments': instruments
    }
