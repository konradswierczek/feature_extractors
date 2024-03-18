from mir_extractors import *
len(librosa.chromagram("tests/test.wav")) == 12
len(mirtoolbox.chromagram("tests/test.wav")) == 12
len(essentia.chromagram("tests/test.wav")) == 12

isinstance(essentia.spectral_centroid("tests/test.wav"), (float))
isinstance(essentia.spectral_centroid("tests/test.wav"), (float))
isinstance(essentia.spectral_centroid("tests/test.wav"), (float))

isinstance(essentia.tempo("tests/test.wav"), (int, float))
isinstance(essentia.tempo("tests/test.wav"), (int, float))
isinstance(essentia.tempo("tests/test.wav"), (int, float))

isinstance(essentia.onsets("tests/test.wav"), (int))
isinstance(librosa.onsets("tests/test.wav"), (int))
isinstance(mirtoolbox.onsets("tests/test.wav"), (int))