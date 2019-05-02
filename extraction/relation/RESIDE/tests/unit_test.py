import unittest
from os import sys, path 

sys.path.append("..")
from reside import reside
res = reside()
    


class TestImputationMethods(unittest.TestCase):

    def setUp(self):
        self.relation_extraction_method = res 
        self.input_file = "riedel_processed.pkl"
        self.verificationErrors = []
        
       
    def test_read_dataset(self):
        success_or_fail = self.relation_extraction_method.read_dataset(self.input_file)
        success = 1
        self.assertEqual(success, success_or_fail)
        
            
    def test_data_preprocess(self):
        success_or_fail = self.relation_extraction_method.data_preprocess(self.input_file)
        success = 1
        self.assertEqual(success, success_or_fail)
        

    
    
if __name__ == '__main__':
	unittest.main()
