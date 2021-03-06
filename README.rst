=============
Storage Stats
=============

Calculates statistics about minimum, maximum and mean average file sizes for each file extension within a directory.

|license|

Intallation
===========

::

    pip install storage_stats

Documentation
=============

Usage: ``storage_stats [-h] [-e MAPFILE] [-o OUTPUT] [--no-aggregation] [--no-recursion] [--no-timing] [-s] [-v] path [path ...]``

Calculates file size statistics for the specified folder(s).

positional arguments:
  path(s)            the folder(s) to characterise

optional arguments:
  -h, --help        Show the help message and exit
  -e MAPFILE        User file overriding similar extension mappings
  -o OUTPUT         CSV file to output statistics too
  --no-aggregation  Do not aggregate results from all specified paths together
  --no-recursion    Do not include sub-folders in stats
  --no-timing       Turn off preprocessing of directory to improve run-time (no timing information provided)
  -s, --silent      Turn off command line output (useful if you just want to output a CSV file)
  -v, --version     Provide the version of this application

If multiple folders are specified, the results are aggregated together, unless the --no-aggregation flag is used.
If --no-aggregation is specified along with the -o (output csv file) flag, then one csv file will be created per
input folder (by appending a "-<index>" onto the end of the specified file name, e.g. stats-1.csv, stats-2.csv, etc.

MAPFILE
-------
MAPFILE should be a text file with one group of similar file extensions per line, separated by commas. Each line
should be in lowercase and take the form:

``.main_ext,.alt1,.alt2,etc``

For example:

::

    .jpeg,.jpg
    .tiff,.tif

Note the period in each extension.

The first extension listed will be the one referenced in the output.

Licence
=======

Released under `Apache version 2.0 license <LICENSE>`_.

Contribute
==========

1. `Fork the GitHub project <https://help.github.com/articles/fork-a-repo>`_
2. Change the code and push into the forked project
3. `Submit a pull request <https://help.github.com/articles/using-pull-requests>`_


.. |license| image:: https://img.shields.io/badge/license-Apache%20V2-blue.svg
   :target: https://github.com/pmay/storage-stats/blob/master/LICENSE
   :alt: Apache V2
