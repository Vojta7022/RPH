from confmat import BinaryConfusionMatrix
import unittest

SPAM_TAG = 'SPAM'
HAM_TAG = 'OK'

class TestBinaryConfusionMatrix(unittest.TestCase):
    def setUp(self):
        self.bcm = BinaryConfusionMatrix(pos_tag=SPAM_TAG, neg_tag=HAM_TAG)
    
    def test_creation(self):
        pass
        
    def test_afterCreation_allCountersAreZero(self):
        bcm = BinaryConfusionMatrix(pos_tag=SPAM_TAG, neg_tag=HAM_TAG)
        self.assertDictEqual(self.bcm.as_dict(), dict('tp': 0, 'fp': 0, 'tn': 0, 'fn': 0))
        
    def test_update_TCP(self):
                
if __name__ == '__main__':
    unittest.main()
