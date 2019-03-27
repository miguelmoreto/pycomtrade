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

    def test_digital_ids(self):
        result = "86_G1;87UA_G1;87UB_G1;87UC_G1;64S_G1;51_G1;46_G1;32_G1;\
86_G2;87UA_G2;87UB_G2;87UC_G2;64S_G2;51_G2;46_G2;32_G2;86_G3;\
87UA_G3;87UB_G3;87UC_G3;64S_G3;51_G3;46_G3;32_G3;86_G4;87UA_G4;\
87UB_G4;87UC_G4;64S_G4;51_G4;46_G4;32_G4"
        self.assertEqual(self.comtradeObj.get_digital_ids(), result)

    def test_numsamples(self):
        self.assertEqual(self.comtradeObj['endsamp'][-1], 24768)

    def test_samplingrate(self):
        self.assertEqual(self.comtradeObj['samp'][-1], 5760)


if __name__ == '__main__':
    unittest.main()
