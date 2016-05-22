Changelog
=========

All notable changes to this project will be documented in this file.
This project adheres to `Semantic Versioning <http://semver.org/>`_.

[0.4.1] - 2016-05-22
--------------------

Added
~~~~~
* Unit tests

[0.4.0] - 2016-05-19
--------------------

Added
~~~~~
* Enabled support for specifying multiple paths. Results are aggregated together by default unless --no-aggregation
  flag is used

Fixed
~~~~~
* Corrected problems with writing to CSV files


[0.3.1] - 2016-05-18
--------------------

Changed
~~~~~~~
* Adjusted import lines to enable PyInstaller to work
* Updated README

Fixed
~~~~~
* Amended directory counting to cope with restricted permissions access to directories
* Ensured directory counting adheres to user specified directory recursion request
* Adjusted walk of directory so that symbolic links are not followed

[0.3.0] - 2016-05-16
--------------------

Added
~~~~~
* File extension mapping file to map between similar file extensions, e.g. .jpeg and .jpg
* CLI flag for preventing pre-counting of files in folder
* CLI flag for allowing the user to specify a list of similar file extension mappings

Changed
~~~~~~~
* File extensions are converted to lowercase
* Updated README


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
