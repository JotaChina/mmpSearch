import os

def parse_samples(file_path, track):
    track_name = track.attrib.get('name', 'N/A')

    sample_info = {}
    sample_name = None

    sampletrack = track.find('./sampletrack')
    if sampletrack is not None:
        sample_info['pan'] = sampletrack.attrib.get('pan', '')
        sample_info['vol'] = sampletrack.attrib.get('vol', '')

    sampletco = track.find('./sampletco')
    if sampletco is not None:
        sample_info['src'] = sampletco.attrib.get('src', '')
        sample_info['len'] = sampletco.attrib.get('len', '')
        sample_info['sample_rate'] = sampletco.attrib.get('sample_rate', '')
        sample_info['pos'] = sampletco.attrib.get('pos', '')
        sample_info['muted'] = sampletco.attrib.get('muted', '')
        sample_name = os.path.basename(sample_info['src'])        

    return {
        'track_name': track_name,
        'sample_name': sample_name,
        'type': 'sample',
        'sample_info': sample_info,
    }
