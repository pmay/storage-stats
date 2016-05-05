#!/usr/bin/python

__author__ = 'Peter May'

import argparse
import csv
import locale
import math
import os

class RunningStat(object):
    def __init__(self):
        self.n = 0
        self.m = 0.0
        self.M2 = 0.0

        self.min = 0.0
        self.max = 0.0

    def add(self, x):
        self.n += 1
        delta = x - self.m
        self.m += delta/self.n
        self.M2 += delta*(x-self.m)

        if (self.n==1):
            self.min = x
            self.max = x
        else:
            if (x < self.min):
                self.min = x
            if (x > self.max):
                self.max = x

    def numberValues(self):
        return self.n

    def getMin(self):
        return self.min

    def getMax(self):
        return self.max

    def getMean(self):
        return self.m

    def variance(self):
        if (self.n > 1):
            return self.M2/(self.n)
        else:
            return 0.0

    def sd(self):
        return math.sqrt(self.variance())

def print_stats(stats):
    print 'Ext'.ljust(5), \
          '# values'.rjust(12), \
          ' Min Size (bytes)'.rjust(18), \
          'Mean Size (bytes)'.rjust(18), \
          'S.D.'.rjust(12), \
          ' Max Size (bytes)'.rjust(18)

    for ext in stats.keys():

        print ext.ljust(5),
        print locale.format('%12.0f', stats[ext].numberValues()),
        print locale.format('%18.0f', stats[ext].getMin()),
        print locale.format('%18.0f', stats[ext].getMean()),
        print locale.format('%12.0f', stats[ext].sd()),
        print locale.format('%18.0f', stats[ext].getMax())

def write_csv(csv_file, statsdict):
    with open(csv_file, 'wb') as csvfile:
        statswriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        header = ['Ext','# Values', 'Min Size (bytes)', 'Mean Size (bytes)', 'S.D.', 'Max Size (bytes)']
        statswriter.writerow(header)

        for ext in statsdict.keys():
            stats = statsdict[ext]
            row = [ext,stats.numberValues(), stats.getMin(), stats.getMean(), stats.sd(), stats.getMax()]
            statswriter.writerow(row)

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

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Calculates file size statistics for the specified folder")
    ap.add_argument("path", help="the folder to characterise")
    ap.add_argument("-o", "--output", dest="output", help="CSV file to output statistics too")
    args = ap.parse_args()

    if args.path:
        # process the specified directory and print the stats
        process_directory(args.path)
        print_stats(filestats)
        if args.output:
            write_csv(args.output, filestats)

