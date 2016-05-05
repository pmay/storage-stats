#!/usr/bin/python

""" Program for capturing statistics about file sizes in a specified directory.
    Captures minimum, maximum, mean and standard deviation of file sizes.
"""
__author__ = 'Peter May'

import argparse
import csv
import locale
import math
import os

class RunningStat(object):
    """ Object for capturing statistics related to a specific file extension.
        Captures minimum file size, maximum file size, and the running population
        mean and standard deviation.

        Code adapted from wiki page https://en.m.wikipedia.org/wiki/Algorithms_for_calculating_variance
    """
    def __init__(self):
        self.n = 0
        self.m = 0.0
        self.M2 = 0.0

        self.min = 0.0
        self.max = 0.0

    def add(self, x):
        """ Adds the specified file size to the statistics for this file extension.
            Specifically, it keeps running values for the minimum, maximum, mean and
            standard deviation.
        :param x: file size to add
        :return:
        """
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
        """ Returns the number of file sizes added for this file extension
        :return: the number of file size values added
        """
        return self.n

    def getMin(self):
        """ Returns the minimum file size added for this file extension
        :return: the minimum file size
        """
        return self.min

    def getMax(self):
        """ Returns the maximum file size added for this extension
        :return: the maximum file size
        """
        return self.max

    def getMean(self):
        """ Returns the running mean average file size for all sizes added
            when this method is called
        :return: the population mean average file size
        """
        return self.m

    def variance(self):
        """ Returns the running variance in file sizes for all sizes added
            when this method is called
        :return: the variance in file sizes about the mean
        """
        if (self.n > 1):
            return self.M2/(self.n)
        else:
            return 0.0

    def sd(self):
        """ Returns the running standard deviation in file sizes for all sizes
            added when this method is called.
        :return: the standard deviation in file sizes about the mean
        """
        return math.sqrt(self.variance())

def print_stats(stats):
    """ Prints the specified statistics to the console in a tabular form
    :param stats: dictionary <ext, RunningStat> containing file size statistics
    :return:
    """
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
    """ Writes the file size statistics to the specified CSV file
    :param csv_file: path of the CSV file to create
    :param statsdict: dictionary <ext, RunningStat> containing statistics
    :return:
    """
    with open(csv_file, 'wb') as csvfile:
        statswriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        header = ['Ext','# Values', 'Min Size (bytes)', 'Mean Size (bytes)', 'S.D.', 'Max Size (bytes)']
        statswriter.writerow(header)

        for ext in statsdict.keys():
            stats = statsdict[ext]
            row = [ext,stats.numberValues(), stats.getMin(), stats.getMean(), stats.sd(), stats.getMax()]
            statswriter.writerow(row)

filestats = {}

def process_directory(path, recursive):
    """ Processes the specified directory, extracting file sizes for each file and
        adding to a file extension indexed dictionary.
    :param path: the path to analyse
    :param recursive: true if processing should include sub-directories
    :return:
    """
    # grab file extension and file sizes across all files in the specified directory
    for root, dirs, files in os.walk(path):
        # if only processing the top level, remove dirs so os.walk doesn't progress further
        if not recursive:
            del dirs[:]

        for name in files:
            filename = os.path.join(root, name)
            fname, fext = os.path.splitext(filename)

            if (os.path.exists(filename)):
                if(not filestats.has_key(fext)):
                    filestats[fext] = RunningStat()
                filestats[fext].add(os.stat(filename).st_size)

if __name__ == "__main__":
    ### Process CLI arguments ###
    ap = argparse.ArgumentParser(description="Calculates file size statistics for the specified folder")
    ap.add_argument("path", help="the folder to characterise")
    ap.add_argument("-o", dest="output", help="CSV file to output statistics too")
    ap.add_argument("--no-recursion", dest="recursive", action="store_false", help="do not include sub-folders in stats")
    ap.add_argument("-s", "--silent", dest="silent", action="store_true", help="turn off command line output")
    args = ap.parse_args()

    if args.path:
        # process the specified directory and print the stats
        process_directory(args.path, args.recursive)

        if not args.silent:
            print_stats(filestats)

        if args.output:
            write_csv(args.output, filestats)

