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
from .metrics import pr_fraction


def rate_func(url):
    #cleaning URL
    ##TODO##
    #rating URL
    try : correct = correctness.getCorrectnessScore(url) #working
    except: correct = -1
    try: busfactor = metric_busfactor.bus_factor_score(url)
    except: busfactor = -1
    try: licenseScore = metric_license.license_score(url)
    except: licenseScore = -1
    try: responsiveMaintainers = responsive.getResponsiveScore(url) #Working
    except: responsiveMaintainers = -1
    try: ramp = rampup.getRampUpScore(url)
    except: ramp = -1
    try: pull_request_fraction = pr_fraction.pr_score(url)
    except: pull_request_fraction = -1
    scores = [
        correct, busfactor, responsiveMaintainers, ramp, pull_request_fraction
    ]
    print(scores)
    return(sum(scores)/len(scores) * licenseScore)


    