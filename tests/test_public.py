import unittest

from pyNiceHashClient import public as pub


class PublicTestSuite(unittest.TestCase):
    def test_get_library_version(self):
        self.assertEquals(pub.get_library_version(), '0.1.0')

    def test_get_api_version(self):
        self.assertEquals(pub.get_api_version(), '1.2.6')

    def test_get_stats_global_current_no_location(self):
        stats = pub.get_stats_global_current()
        self.assertTrue(len(stats) == 25)

    def test_get_stats_global_current_location_set(self):
        stats = pub.get_stats_global_current(0)
        self.assertTrue(len(stats) == 25)


if __name__ == '__main__':
    unittest.main()
