"""
"""
###############################################################################
# Third Party Imports
from numpy import array
from . matlab import eng
###############################################################################
def onsets(filename):
    """
    """
    eng.eval("mirevents_val = mirgetdata(mirevents('" +
             filename +
             "'))", nargout = 0)
    return len(eng.workspace['mirevents_val'])

###############################################################################
def chromagram(filename, output: str = "proportion"):
    """
    """
    outputs = ['proportion', 'original']
    if output not in outputs:
        raise ValueError("Invalid output argument. Expected one of: %s" % outputs)
    eng.eval("mirchromagram_val = mirgetdata(mirchromagram('" +
             filename +
             "'))", nargout = 0)
    out = array(eng.workspace['mirchromagram_val']).tolist()
    hpcp = [i for sublist in out for i in sublist]
    if output == "original":
        return hpcp
    elif output == "proportion":
        return [pc/sum(hpcp) for pc in hpcp]

###############################################################################
def spectral_centroid(filename: str):
    """"""
    eng.eval("mircentroid_val = mirgetdata(mircentroid('" +
    filename +
    "'))", nargout = 0)
    return eng.workspace['mircentroid_val']

###############################################################################
def tempo(filename: str, method: str = "Classical"):
    """
    """
    methods = ['Classical', 'Metre']
    if method not in methods:
        raise ValueError("Invalid method argument. \
                          Expected one of: %s" % methods)
    if method == 'Classical':
        eng.eval("mirtempo_val = mirgetdata(mirtempo('" +
                 filename +
                 "'))", nargout = 0)
    else:
        eng.eval("mirtempo_val = mean(mirgetdata(mirtempo('" +
                 filename +
                 "', 'Metre')))", nargout = 0)
    return eng.workspace['mirtempo_val']

###############################################################################