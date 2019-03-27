import unittest

from src import pyComtrade


class TestPyComtrade(unittest.TestCase):

    comtradeObj = pyComtrade.ComtradeRecord()

    def setUp(self):
        self.comtradeObj.read('./examples/test_data3/test3.cfg',
                              './examples/test_data3/test3.dat')

    def tearDown(self):
        self.comtradeObj.reset()

    def test_analog_ids(self):
        result = "IA_G1;IB_G1;IC_G1;VA_G1;VB_G1;VC_G1;IA_G2;IB_G2;IC_G2;\
VA_G2;VB_G2;VC_G2;IA_G3;IB_G3;IC_G3;VA_G3;VB_G3;VC_G3;\
IA_G4;IB_G4;IC_G4;VA_G4;VB_G4;VC_G4;VA_B69;VB_B69;\
VC_B69;IN_TF7;IA_TF7;IB_TF7;IC_TF7"
        self.assertEqual(self.comtradeObj.get_analog_ids(), result)

    def test_numsamples(self):
        self.assertEqual(self.comtradeObj['endsamp'][-1], 24768)

    def test_samplingrate(self):
        self.assertEqual(self.comtradeObj['samp'][-1], 5760)


if __name__ == '__main__':
    unittest.main()
