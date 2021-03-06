# Copyright 2016 Peter May
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

__author__ = 'pmay'

import unittest
from storage_stats import storagestats


class RunningStatTestCase(unittest.TestCase):
    def setUp(self):
        self.stats = storagestats.RunningStat()

    def test_creation(self):
        """ Tests creation of a RunningStat object
        """
        self.assertEquals(self.stats.n, 0)
        self.assertEquals(self.stats.m, 0)   # mean
        self.assertEquals(self.stats.M2, 0)
        self.assertEquals(self.stats.min, 0)
        self.assertEquals(self.stats.max, 0)

    def test_add(self):
        """ Tests adding a single value
        """
        self.stats.add(1)
        self.assertEquals(self.stats.numbervalues(), 1)
        self.assertEquals(self.stats.getmin(), 1)
        self.assertEquals(self.stats.getmax(), 1)
        self.assertEquals(self.stats.getmean(), 1)
        self.assertEquals(self.stats.variance(), 0)

    def test_add_2(self):
        """ Tests adding two values
        """
        self.stats.add(1)
        self.stats.add(2)
        self.assertEquals(self.stats.numbervalues(), 2)
        self.assertEquals(self.stats.getmin(), 1)
        self.assertEquals(self.stats.getmax(), 2)
        self.assertEquals(self.stats.getmean(), 1.5)
        self.assertEquals(self.stats.variance(), 0.25)

    def test_add_3(self):
        """ Tests adding three values
        """
        map(self.stats.add, [1, 2, 3])
        self.assertEquals(self.stats.numbervalues(), 3)
        self.assertEquals(self.stats.getmin(), 1)
        self.assertEquals(self.stats.getmax(), 3)
        self.assertEquals(self.stats.getmean(), 2)
        self.assertEquals(self.stats.variance(), float(2)/float(3))

    def test_add_4(self):
        """ Tests adding four values
        """
        map(self.stats.add, [4, 3, 2, 1])
        self.assertEquals(self.stats.numbervalues(), 4)
        self.assertEquals(self.stats.getmin(), 1)
        self.assertEquals(self.stats.getmax(), 4)
        self.assertEquals(self.stats.getmean(), 2.5)
        self.assertEquals(self.stats.variance(), 1.25)


if __name__ == '__main__':
    unittest.main()
