import unittest

from pyNiceHashClient import public as pub


class PublicTestSuite(unittest.TestCase):
    def test_get_library_version(self):
        self.assertEquals(pub.get_library_version(), 0.1)


if __name__ == '__main__':
    unittest.main()

    # suite = unittest.TestLoader().loadTestsFromTestCase(PublicTestSuite)
    # unittest.TextTestRunner(verbosity=2).run(suite)
