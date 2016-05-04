#!/usr/bin/env python

__author__ = 'Peter May'

import argparse
import csv
import locale
import math
import numpy
import os

path = r'C:\Data'


class RunningStat(object):
    def __init__(self):
        self.n = 0
        self.m = 0.0
        self.M2 = 0.0

    def add(self, x):
        self.n += 1
        delta = x - self.m
        self.m += delta/self.n
        self.M2 += delta*(x-self.m)

    def numberValues(self):
        return self.n

    def mean(self):
        if (self.n > 0):
            return self.m
        else:
            return 0.0

    def variance(self):
        if (self.n > 1):
            return self.M2/(self.n)
        else:
            return 0.0

    def sd(self):
        return math.sqrt(self.variance())

# Requires stats to be a dictionary of 5-tuples (length, min, mean, sd, max)
def print_stats(statsdict, filesizes):
    for ext in statsdict.keys():
        stats = statsdict[ext]

        #num_size = locale.format('%5.0f', stats[0], 3)
        #min_size = locale.format('%12.0f', stats[1])
        #avg_size = locale.format('%12.0f', stats[2])
        #sd_size  = locale.format('%12.0f', stats[3])
        #max_size = locale.format('%12.0f', stats[4])

        print ext.ljust(5),
        print stats[0],
        print stats[2],
        print stats[3],
        #print num_size,
        #print min_size,
        #print avg_size,
        #print sd_size,
        #print max_size,
        print filesizes[ext]

def ps(new):
    for ext in new.keys():

        print ext.ljust(5),
        print new[ext].numberValues(),
        print new[ext].mean(),
        print new[ext].sd()

def write_csv(csv_file, statsdict):
    with open(csv_file, 'wb') as csvfile:
        statswriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

        for ext in statsdict.keys:
            stats = statsdict[ext]
            statswriter.writerow(stats[0], stats[1], stats[2], stats[3], stats[4])

filestats = {}

def process_directory(path):
    # grab file extension and file sizes across all files in the specified directory
    for root, dirs, files in os.walk(path):
        for name in files:
            filename = os.path.join(root, name)
            fname, fext = os.path.splitext(filename)

            if (os.path.exists(filename)):
                if(not filestats.has_key(fext)):
                    filestats[fext] = RunningStat()
                filestats[fext].add(os.stat(filename).st_size)

# summarise
process_directory(path)
ps(filestats)

# def main():
#     process_directory()
#
# if __name__ == "__main__":
#     main()
