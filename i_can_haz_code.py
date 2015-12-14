#!/usr/bin/env python

import matplotlib.pyplot as plt
import math
import random

ds = [random.randint(10,100) for i in range(0,100)]

def anal(ds=[]):
    if not isinstance(ds,list):
        return('no list... why no list???')
    if not isinstance(random.choice(ds), int):
        return('At least one element of ds is not an int.')
    def mean(ds):
        return(sum(ds)/len(ds))
    def median(ds):
        ds = sorted(ds)
        if len(ds) < 1:
            return (None)
        if len(ds) %2 == 1:
            return (ds[((len(ds)+1)/2)-1])
        else:
            return float(sum(ds[(len(ds)/2)-1:(len(ds)/2)+1]))/2.0
    def mode(ds):
        return(max(set(ds), key=ds.count))
    def std(ds):
        return(math.sqrt(sum([(val - mean(ds))**2 for val in ds])/(len(ds) - 1)))
    def get_max(ds):
        return(max(ds))
    def get_min(ds):
        return(min(ds))
    def get_range(ds):
        return(max(ds)-min(ds))
    def graphit(ds,mean=mean(ds),median=median(ds),mode=mode(ds),maxs=get_max(ds),get_min=get_min(ds),get_range=get_range(ds),std=std(ds)):
        means = [mean for i in ds]
        medians = [median for i in ds]
        modes = [mode for i in ds]
        maxes = [maxs for i in ds]
        mins = [get_min for i in ds]
        stdsp = [mean + std for i in ds]
        stdsm = [mean - std for i in ds]
        ranges = [get_range for i in ds]
        [plt.plot(i) for i in [ds,means,medians,modes,maxes,mins,ranges,stdsp,stdsm]]
    graphit(ds)
    plt.title('mean = %s median = %s mode = %s std = %s max = %s min = %s range = %s'%(mean(ds),median(ds),mode(ds),std(ds),get_max(ds),get_min(ds),get_range(ds)))
#   plt.savefig('./tmp.png')
    plt.show()



anal(ds)
