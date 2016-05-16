Changelog
=========

All notable changes to this project will be documented in this file.
This project adheres to `Semantic Versioning <http://semver.org/>`_.

[Unreleased]
------------

Added
~~~~~
* CLI flag for preventing pre-counting of files in folder
* File extension mapping file to map between similar file extensions, e.g. .jpeg and .jpg

Changed
~~~~~~~
* File extensions are converted to lowercase


[0.2.1] - 2016-05-11
--------------------

Added
~~~~~
* Single-source versioning via __init__.py
* Added ability to print out program version via CLI

Changed
~~~~~~~
* Improved tabular command line output


[0.2] - 2016-05-10
------------------

Added
~~~~~
* Initial scan of folder to provide scope for progress bar

Changed
~~~~~~~
* Now using scandir for faster processing of folder

[0.1] - 2016-05-08
------------------

Added
~~~~~
* Initial version of code
* Setup.py and entry points
* Readme
* Changelog
