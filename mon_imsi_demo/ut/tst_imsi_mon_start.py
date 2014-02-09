import unittest
from mon_imsi_demo.imsi import imsi
from mon_imsi_demo.imsi_list import imsi_list
from mon_imsi_demo.imsi_mon_start import imsi_mon_start

class Test(unittest.TestCase):


    def test_imsi_mon_start(self):
        imsi_1 = imsi('1', '3')
        imsi_2 = imsi('2', '3')
        tmp_imsi_list = imsi_list()
        tmp_imsi_list.add_imsi(imsi_1)
        tmp_imsi_list.add_imsi(imsi_2)
        tmp_imsi_mon_start = imsi_mon_start(tmp_imsi_list)
        self.assertEqual('xb1,2,\
1,10,00,00,00,00,00,00,00,3,\
1,20,00,00,00,00,00,00,00,3,\
00,00,00,00,00,00,00,00,00,00,\
00,00,00,00,00,00,00,00,00,00,\
00,00,00,00,00,00,00,00,00,00,\
00,00,00,00,00,00,00,00,00,00,\
00,00,00,00,00,00,00,00,00,00,\
00,00,00,00,00,00,00,00,00,00',\
tmp_imsi_mon_start.get_imsi_mon_start_str())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()