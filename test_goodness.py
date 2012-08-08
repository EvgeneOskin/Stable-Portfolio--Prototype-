import goodness
import unittest

class TestGoodness(unittest.TestCase):
    
    def setUp(self):
        self.good = goodness.Quotes()
        self.good.add_symbol([100.0, 1.0, 100.0])
        self.good.add_symbol([1.0, 100.0, 1.0])
        self.good.add_symbol([1.0, 5.0, 10.0])
        self.good.add_symbol([1.0, -3.0, -8.0])
        self.bad = goodness.Quotes()
        self.bad.add_symbol([1.0, 2.0, 3.0])
        self.bad.add_symbol([1.0, 0.0, -1.0])
        self.bad.add_symbol([1.0, 2.0, 3.0])
        self.bad.add_symbol([1.0, 0.0, 3.0])

    def test_bad(self):
        print ( "goodnes of good:  " + str (goodness.goodness(self.good)))
        self.assertAlmostEqual(goodness.goodness(self.good), 0)

    def test_good(self):
        print ( "goodnes of bad:  " + str (goodness.goodness(self.bad)))
        self.assertNotAlmostEqual(goodness.goodness(self.bad), 0.0)

    def test_comparison_good_vs_bad(self):
        self.assertTrue(goodness.goodness(self.good) < goodness.goodness(self.bad))

suite = unittest.TestLoader().loadTestsFromTestCase(TestGoodness)
unittest.TextTestRunner(verbosity=2).run(suite)
