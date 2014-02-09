import unittest
from mon_imsi_demo.imsi import imsi

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_2_imsi_length(self):
        imsi_val = imsi('12', '1')
        imsi_table_length = imsi_val.get_imsi_length()
        imsi_table = imsi_val.get_imsi_table_str()
        imsi_mon_dir = imsi_val.get_imsi_mon_dir()
        self.assertEqual('2', str(imsi_table_length))
        self.assertEqual('12,00,00,00,00,00,00,00', imsi_table)
        self.assertEqual('1', imsi_mon_dir)
        
    def test_3_imsi_length(self):
        imsi_val = imsi('123', '2')
        imsi_table_length = imsi_val.get_imsi_length()
        imsi_table = imsi_val.get_imsi_table_str()
        self.assertEqual('3', str(imsi_table_length))
        self.assertEqual('12,30,00,00,00,00,00,00', imsi_table)
        
    def test_15_imsi_length(self):
        imsi_val = imsi('123456789012345', '3')
        imsi_table_length = imsi_val.get_imsi_length()
        imsi_table = imsi_val.get_imsi_table_str()
        self.assertEqual('15', str(imsi_table_length))
        self.assertEqual('12,34,56,78,90,12,34,50', imsi_table)
        
    def test_imsi_str(self):
        imsi_val = imsi('1234567890123456', '3')
        self.assertEqual('10,12,34,56,78,90,12,34,56,3', imsi_val.get_imsi_str())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testImsiMon']
    unittest.main()