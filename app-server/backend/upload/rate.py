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
    print("I GOT ALL THE WAY HERE WEEEEEE1")
    try : correct = correctness.getCorrectnessScore(url)
    except: return -1
    print("I GOT ALL THE WAY HERE WEEEEEE2")
    try: busfactor = metric_busfactor.bus_factor_score(url)
    except: return -1
    print("I GOT ALL THE WAY HERE WEEEEEE3")
    try: licenseScore = metric_license.license_score(url)
    except: return -1
    print("I GOT ALL THE WAY HERE WEEEEEE4")
    try: responsiveMaintainers = responsive.getResponsiveScore(url)
    except: return -1
    print("I GOT ALL THE WAY HERE WEEEEEE5")
    try: ramp = rampup.getRampUpScore(url)
    except: return -1
    try: pull_request_fraction = pr_fraction.pr_score(url)
    except: return -1
    
    scores = [
        correct, busfactor, licenseScore, responsiveMaintainers, ramp, pull_request_fraction
    ]

    print("I GOT ALL THE WAY HERE WEEEEEE")
    return(sum(scores)/len(scores))


    