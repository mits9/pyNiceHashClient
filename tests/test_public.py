import unittest

from pyNiceHashClient import public as pub


class PublicTestSuite(unittest.TestCase):
    def test_get_library_version(self):
        self.assertEquals(pub.get_library_version(), '0.1.0')

    def test_get_api_version(self):
        self.assertEquals(pub.get_api_version(), '1.2.6')


if __name__ == '__main__':
    unittest.main()
