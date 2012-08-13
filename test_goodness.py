import goodness
import unittest

class TestGoodness(unittest.TestCase):
    
    def setUp(self):
        self.good = goodness.Quotes()
        self.good.add_symbol([100.0, 1.0, 100.0])
        self.good.add_symbol([1.0, 100.0, 1.0])
        self.good.add_symbol([1.0, 1.0, 1.0])
        self.bad = goodness.Quotes()
        self.bad.add_symbol([9.84,9.65,9.85,9.91,9.62,9.64,9.69,9.7,10.0,10.08,9.9,9.85,9.87,9.8,9.84,9.86,9.65,9.92,9.9,9.98,9.97,10.14,9.84,9.03,9.15,9.29,9.77,9.91,10.2,9.2,9.67,9.52,9.88,10.04,9.92,10.35,10.18,9.6,10.08,10.09,10.08,10.5,9.99,10.51,10.56,10.51,10.51,10.43,10.47,10.49,10.47,10.42,10.38,10.41,10.15,10.29,10.36,10.18,9.96,9.88,9.63,9.58,9.71,9.79,9.76,9.73,9.39,9.48,9.57,9.76,9.77,9.74,9.83,9.67])
        self.bad.add_symbol([25.17,25.28,25.28,25.26,25.32,25.19,25.33,25.28,25.15,25.19,25.25,25.22,25.3,25.21,25.2,25.31,25.33,25.4,25.42,25.34,25.37,25.35,25.41,25.35,25.35,25.47,25.44,25.41,25.42,25.38,25.38,25.41,25.39,25.38,25.41,25.47,25.47,25.45,25.45,25.43,25.53,25.1,25.07,25.25,25.33,25.11,25.11,25.14,25.2,25.29,25.2,25.35,25.33,25.25,25.22,25.31,25.31,25.25,25.25,25.27,25.36,25.25,25.35,25.37,25.35,25.29,25.41,25.38,25.35,25.4,25.36,25.43,25.38,25.35])
        self.bad.add_symbol([4.67,4.69,4.7,4.69,4.7,4.69,4.7,4.65,4.65,4.64,4.59,4.58,4.59,4.53,4.52,4.5,4.58,4.59,4.55,4.57,4.56,4.5,4.46,4.4,4.35,4.35,4.4,4.42,4.44,4.38,4.42,4.36,4.35,4.31,4.26,4.32,4.31,4.33,4.41,4.37,4.36,4.44,4.43,4.46,4.49,4.53,4.53,4.54,4.54,4.55,4.55,4.44,4.39,4.46,4.5,4.51,4.52,4.51,4.54,4.57,4.54,4.53,4.37,4.41,4.42,4.41,4.43,4.45,4.46,4.47,4.45,4.47,4.47,4.36])
        
    def test_bad(self):
        print ( "goodnes of good:  " + str (goodness.goodness(self.good)))
        self.assertAlmostEqual(goodness.goodness(self.good), 0.0)

    def test_good(self):
        print ( "goodnes of bad:  " + str (goodness.goodness(self.bad)))
        self.assertNotAlmostEqual(goodness.goodness(self.bad), 0.0)

    def test_comparison_good_vs_bad(self):
        self.assertTrue(goodness.goodness(self.good) < goodness.goodness(self.bad))

suite = unittest.TestLoader().loadTestsFromTestCase(TestGoodness)
unittest.TextTestRunner(verbosity=2).run(suite)
