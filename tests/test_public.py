import unittest

from pyNiceHashClient import public as pub


class PublicTestSuite(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_library_version(self):
        self.assertEquals(pub.get_library_version(), 0.1)

    def test_get_api_version(self):
        self.assertEquals(pub.get_api_version(), u'1.2.6')


if __name__ == '__main__':
    unittest.main()
