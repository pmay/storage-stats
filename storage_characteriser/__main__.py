__author__ = 'pmay'

import argparse
import sys
import StorageCharacteriser as sc

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    ### Process CLI arguments ###
    ap = argparse.ArgumentParser(description="Calculates file size statistics for the specified folder")
    ap.add_argument("path", help="the folder to characterise")
    ap.add_argument("-o", dest="output", help="CSV file to output statistics too")
    ap.add_argument("--no-recursion", dest="recursive", action="store_false", help="do not include sub-folders in stats")
    ap.add_argument("-s", "--silent", dest="silent", action="store_true", help="turn off command line output (useful if "
                                                                               "you just want to output a CSV file")
    args = ap.parse_args()

    if args.path:
        # process the specified directory and print the stats
        sc.process_directory(args.path, args.recursive)

        if not args.silent:
            sc.print_stats(sc.filestats)

        if args.output:
            sc.write_csv(args.output, sc.filestats)

if __name__ == "__main__":
    main()