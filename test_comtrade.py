import unittest

from src import pyComtrade


class TestPyComtrade(unittest.TestCase):

    comtradeObj = pyComtrade.ComtradeRecord()

    def setUp(self):
        self.comtradeObj.read('./examples/test_data3/test3.cfg',
                              './examples/test_data3/test3.dat')

    def tearDown(self):
        self.comtradeObj.reset()

    def test_numsamples(self):
        self.assertEqual(self.comtradeObj['endsamp'][-1], 24768)

    def test_samplingrate(self):
        self.assertEqual(self.comtradeObj['samp'][-1], 5760)


if __name__ == '__main__':
    unittest.main()
