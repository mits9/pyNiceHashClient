import unittest

from pyNiceHashClient import public as pub


class PublicTestSuite(unittest.TestCase):
    def test_get_library_version(self):
        self.assertEquals(pub.get_library_version(), '0.1.0')

    def test_get_api_version(self):
        self.assertEquals(pub.get_api_version(), '1.2.6')

    def test_get_stats_global_current_no_location(self):
        stats = pub.get_stats_global_current()
        self.assertEquals(len(stats), 25)

    def test_get_stats_global_current_location_set(self):
        stats = pub.get_stats_global_current(0)
        self.assertEquals(len(stats), 25)

    def test_get_stats_global_24h_no_location(self):
        stats = pub.get_stats_global_24h()
        self.assertEquals(len(stats), 25)

    def test_get_stats_global_24h_location_set(self):
        stats = pub.get_stats_global_24h(1)
        self.assertEquals(len(stats), 25)

    def test_get_stats_provider_with_addr(self):
        btc_address = '1P5PNW6Wd53QiZLdCs9EXNHmuPTX3rD6hW'
        stats = pub.get_stats_provider(btc_address)
        self.assertEquals(stats['addr'], btc_address)

    def test_get_stats_provider_with_no_addr(self):
        btc_address = ''
        self.assertRaises(ValueError, pub.get_stats_provider, btc_address)

    def test_get_buy_info(self):
        stats = pub.get_buy_info()
        self.assertEquals(len(stats['algorithms']), 25)

    def test_get_orders(self):
        location = 0
        algo = 1
        result = pub.get_orders(location, algo)
        self.assertGreater(len(result['orders']), 0)


if __name__ == '__main__':
    unittest.main()
