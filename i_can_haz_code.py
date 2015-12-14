#!/usr/bin/env python
import random
from math import sqrt

import matplotlib.pyplot as plt

data = [random.randint(10, 100) for i in range(0, 100)]


class Analysis(object):
    def __init__(self, data):
        data = data or []
        if not isinstance(data, list):
            return 'no list... why no list???'
        if any(not isinstance(d, int) for d in data):
            return 'At least one element of ds is not an int.'
        self.data = data

    def mean(self):
        return sum(self.data) / len(self.data)

    def median(self):
        data = sorted(self.data)
        ds_length = len(data)
        if ds_length < 1:
            return None
        elif ds_length % 2 == 1:
            return self.data[((ds_length + 1) / 2) - 1]
        else:
            return float(sum(data[(ds_length / 2) - 1:(ds_length / 2) + 1])) / 2.0

    def mode(self):
        return max(set(self.data), key=self.data.count)

    def std_dev(self):
        return sqrt(sum((val - self.mean()) ** 2 for val in self.data) / (len(self.data) - 1))

    def get_max(self):
        return max(self.data)

    def get_min(self):
        return min(self.data)

    def get_range(self):
        return max(self.data) - min(self.data)

    def graph_it(self, data=None, mean=None, median=None, mode=None, maximum=None, minimum=None, data_range=None, std_dev=None):
        self.data = data or self.data
        mean = mean or self.mean()
        median = median or self.median()
        mode = mode or self.mode()
        maximum = maximum or self.get_max()
        minimum = minimum or self.get_min()
        data_range = data_range or self.get_range()
        std_dev = std_dev or self.std_dev()

        means = [mean for i in self.data]
        medians = [median for i in self.data]
        modes = [mode for i in self.data]
        maxes = [maximum for i in self.data]
        mins = [minimum for i in self.data]
        stdsp = [mean + std_dev for i in self.data]
        stdsm = [mean - std_dev for i in self.data]
        ranges = [data_range for i in self.data]
        for i in (self.data, means, medians, modes, maxes, mins, ranges, stdsp, stdsm):
            plt.plot(i)
        plt.title(
            'mean = {} median = {} mode = {} std = {} max = {} min = {} range = {}'.format(
                mean, median, mode, std_dev, maximum, minimum, data_range))
        #  plt.savefig('./tmp.png')
        plt.show()


Analysis(data).graph_it()
