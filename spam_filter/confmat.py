class BinaryConfusionMatrix:
    
    def __init__(self, pos_tag, neg_tag):
        self.pos_tag = pos_tag
        self.neg_tag = neg_tag
        self.tp = 0
        self.fp = 0
        self.tn = 0
        self.fn = 0
        
    def as_dict(self):
        return {'tp': self.tp, 'fp': self.fp, 'tn': self.tn, 'fn': self.fn}