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
    
    def update(self, truth, prediction):
        if truth not in [self.pos_tag, self.neg_tag]:
            raise ValueError(f"Invalid truth value: {truth}")
        if prediction not in [self.pos_tag, self.neg_tag]:
            raise ValueError(f"Invalid prediction value: {prediction}")
        
        if truth == self.pos_tag:
            if prediction == self.pos_tag:
                self.tp += 1
            else:
                self.fn += 1
        else:
            if prediction == self.pos_tag:
                self.fp += 1
            else:
                self.tn += 1
                
    def compute_from_dicts(self, truth_dict, pred_dict):
        self.tp = 0
        self.fp = 0
        self.tn = 0
        self.fn = 0
        
        for key in truth_dict:
            self.update(truth_dict[key], pred_dict[key])
