import unittest
import main

class TestParcelPrices(unittest.TestCase):

    def testParcelSizePrice(self):
        result = main.Order.getParcelSize()
        self.assertEqual(result, "Small Parcel: $3. Total Cost $3")

    def addSpeedShipping(self):
        result = main.Order.speedyShipping()
        self.assertEqual(result, 6)
if __name__ == '__main__':
    unittest.main()