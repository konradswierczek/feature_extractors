"""
"""
###############################################################################
from librosa import feature, load, get_samplerate
from librosa.feature import spectral_centroid
from librosa.onset import onset_detect
from statistics import mean
###############################################################################
def chromagram(audio_file: str, output: str = "proportion", method: str = "cqt"):
    """
    """
    outputs = ['proportion', 'original']
    methods = ['cqt', 'stft', 'cens', 'vqt']
    if output not in outputs:
        raise ValueError("Invalid output argument. Expected one of: %s" % outputs)
    if method not in methods:
        raise ValueError("Invalid method argument. Expected one of: %s" % methods)
    y, sr = load(audio_file, sr = get_samplerate(audio_file))
    if method == 'vqt':
        chromagram = feature.chroma_vqt(y = y, sr = sr, intervals = 'equal', norm = None)
    else:
        chromagram = eval("feature.chroma_" +
                        method +
                        "(y = y, sr = sr, n_chroma = 12)")
    chromagram = [sum(pc) for pc in chromagram]
    if output == "original":
        return chromagram
    elif output == "proportion":
        return [pc/sum(chromagram) for pc in chromagram]
    
###############################################################################
def onsets(filename):
    """"""
    y, sr = load(filename, sr = get_samplerate(filename))
    return len(onset_detect(y = y, sr = sr))

###############################################################################
def tempo(filename: str, method: str = "beat_track"):
    """"""
    methods = ["beat_track", "onsets"]
    if method not in methods:
        raise ValueError("Invalid method argument. \
                          Expected one of: %s" % methods)
    y, sr = librosa.load(filename, sr = librosa.get_samplerate(filename))
    if method == "beat_track":
        return librosa.beat.beat_track(y=y, sr=sr)[0]
    else:
        onset_env = librosa.onset.onset_strength(y=y, sr=sr)
        return librosa.feature.tempo(onset_envelope=onset_env, sr=sr)[0]

###############################################################################
def spectral_centroid(filename: str):
    """"""
    y, sr = load(filename, sr = get_samplerate(filename))
    return mean(spectral_centroid(y=y, sr=sr)[0])

###############################################################################