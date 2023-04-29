# from upload.metrics import correctness
# from upload.metrics import metric_busfactor
# from upload.metrics import metric_license
# from upload.metrics import responsive
# from upload.metrics import rampup

from .metrics import correctness
from .metrics import metric_busfactor
from .metrics import metric_license
from .metrics import responsive
from .metrics import rampup


def rate_func(url):
    #cleaning URL
    ##TODO##
    #rating URL
    try : correct = correctness.getCorrectnessScore(url)
    except: return -1
    try: busfactor = metric_busfactor.bus_factor_score(url)
    except: return -1
    try: licenseScore = metric_license.license_score(url)
    except: return -1
    try: responsiveMaintainers = responsive.getResponsiveScore(url)
    except: return -1
    try: ramp = rampup.getRampUpScore(url)
    except: return -1
    scores = [
        correct, busfactor, licenseScore, responsiveMaintainers, ramp
    ]

    return(sum(scores)/len(scores))


    