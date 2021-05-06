import unittest

class TestParcelPrices(unittest.TestCase):

    def testParcelSizePrice(self):
        self.assertEqual("1cmx1cmx1cmx", "Small Parcel: $3. Total Cost: $3")
        self.assertFalse("1cmx1cmx1cmx", "Small Parcel: $3. Total Cost: $3")

if __name__ == '__main__':
    test = TestParcelPrices()
    test.testParcelSizePrice()