__author__ = 'pmay'

import hashlib
import os
import tempfile
import unittest
from storage_stats import storagestats


class CharacteriserTestCase(unittest.TestCase):

    def test_empty_creation(self):
        """ Test default creation of the Characteriser object
        """
        characteriser = storagestats.Characteriser(None)
        # no stats to start with
        self.assertEqual(len(characteriser.filestats.keys()), 0)
        # default file extension mappings
        mappings = characteriser.extmap
        self.assertEquals(mappings, {'.jpeg': '.jpg', '.jpg': '.jpg', '.tif': '.tiff', '.tiff': '.tiff'})

    def test_mapfile_creation(self):
        """ Test creation of the Characteriser object with a default extension map file
        """
        characteriser = storagestats.Characteriser('tests/resources/data/testextensionmap')
        # no stats to start with
        self.assertEqual(len(characteriser.filestats.keys()), 0)
        # check file extensions map to those in specified file
        mappings = characteriser.extmap
        self.assertEquals(mappings, {'.tif': '.tiff', '.tiff': '.tiff'})

    def test_process_recursive(self):
        """ Tests processing of a directory with recursion
        """
        characteriser = storagestats.Characteriser(None)
        characteriser.process_directory('tests/resources/data')
        # check filestats
        self.assertEquals(len(characteriser.filestats.keys()), 3)   # .jpg, .tiff, <blank>
        self.assertEquals(characteriser.filestats['.jpg'].numbervalues(), 2)
        self.assertEquals(characteriser.filestats['.tiff'].numbervalues(), 1)
        self.assertEquals(characteriser.filestats[''].numbervalues(), 1)

    def test_process_no_recursion(self):
        """ Tests processing of a directory without recursion
        """
        characteriser = storagestats.Characteriser(None)
        characteriser.process_directory('tests/resources/data', recursive=False)
        # check filestats
        self.assertEquals(len(characteriser.filestats.keys()), 2)   # .jpg, <blank>
        self.assertEquals(characteriser.filestats['.jpg'].numbervalues(), 2)
        self.assertEquals(characteriser.filestats[''].numbervalues(), 1)

    def test_write_csv(self):
        """ Tests writing of CSV file
        """
        characteriser = storagestats.Characteriser(None)
        characteriser.process_directory('tests/resources/data')

        tmpfile = os.path.join(tempfile.gettempdir(), 'storage-stats-output.csv')
        characteriser.write_csv(tmpfile)

        # Check that the written file is identical
        md5 = hashlib.md5()
        with open(tmpfile, 'rb') as csvfile:
            for line in csvfile.readlines():
                md5.update(line)
        self.assertEquals(md5.hexdigest(), "ff7c658a8487a5aaf15478067e9844e5")

        # clear up
        os.remove(tmpfile)


    def test_write_csv_indexed(self):
        """ Tests writing of CSV file when an index is specified
        """
        characteriser = storagestats.Characteriser(None)
        characteriser.process_directory('tests/resources/data')

        tmpfile = os.path.join(tempfile.gettempdir(), 'storage-stats-output.csv')
        characteriser.write_csv(tmpfile, "1")

        # Check index file exists
        indextmpfile = os.path.join(tempfile.gettempdir(), 'storage-stats-output-1.csv')
        self.assertTrue(os.path.exists(indextmpfile))

        # Check that the written file is identical
        md5 = hashlib.md5()
        with open(indextmpfile, 'rb') as csvfile:
            for line in csvfile.readlines():
                md5.update(line)
        self.assertEquals(md5.hexdigest(), "ff7c658a8487a5aaf15478067e9844e5")

        # clear up
        os.remove(indextmpfile)


if __name__ == '__main__':
    unittest.main()
