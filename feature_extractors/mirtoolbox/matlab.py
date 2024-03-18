from subprocess import run
from matlab.engine import start_matlab, find_matlab
# matlab engine
eng = start_matlab()
# Import MIRtoolbox

eng.addpath(eng.genpath('feature_extractors/mirtoolbox/mirtoolbox'), nargout= 0)