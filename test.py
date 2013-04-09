import os
import demosite
import unittest
import tempfile

class DemositeTestCase(unittest.TestCase):
    def setUp(self):
        demosite.app.config['DATAFILE'] = "tempDataFile"
        demosite.app.config['TESTING'] = True
        self.app = demosite.app.test_client()

    def tearDown(self): 
        pass

    def test_empty_db(self):
        d = demosite.dataStore();
        assert d.isEmpty()

if __name__ == '__main__':
    unittest.main()
