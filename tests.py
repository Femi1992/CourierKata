import unittest
import main

class TestParcelPrices(unittest.TestCase):

    def testParcelSizePrice(self):
        result = main.getParcelSize()
        self.assertEqual(result, "Small Parcel: $3. Total Cost $3")

if __name__ == '__main__':
    unittest.main()