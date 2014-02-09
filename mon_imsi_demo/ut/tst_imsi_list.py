import unittest
from mon_imsi_demo.imsi_list import imsi_list
from mon_imsi_demo.imsi import imsi

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_1_imsi_imsi_list(self):
        tmp_imsi_list = imsi_list()
        imsi_1 = imsi('1', '3')
        tmp_imsi_list.add_imsi(imsi_1)
        self.assertEqual(1, tmp_imsi_list.get_imsi_list_length())

    def test_2_imsi_imsi_list(self):
        tmp_imsi_list = imsi_list()
        imsi_1 = imsi('1', '3')
        imsi_2 = imsi('2', '3')
        tmp_imsi_list.add_imsi(imsi_1)
        tmp_imsi_list.add_imsi(imsi_2)
        self.assertEqual(2, tmp_imsi_list.get_imsi_list_length())

    def test_imsi_list_str(self):
        tmp_imsi_list = imsi_list()
        imsi_1 = imsi('1', '3')
        imsi_2 = imsi('2', '3')
        tmp_imsi_list.add_imsi(imsi_1)
        tmp_imsi_list.add_imsi(imsi_2)
        self.assertEqual('2,\
1,10,00,00,00,00,00,00,00,3,\
1,20,00,00,00,00,00,00,00,3,\
00,00,00,00,00,00,00,00,00,00,\
00,00,00,00,00,00,00,00,00,00,\
00,00,00,00,00,00,00,00,00,00,\
00,00,00,00,00,00,00,00,00,00,\
00,00,00,00,00,00,00,00,00,00,\
00,00,00,00,00,00,00,00,00,00',\
tmp_imsi_list.get_imsi_list_str())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()