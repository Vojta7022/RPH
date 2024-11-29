import os
from utils import read_classification_from_file
import confmat

def quality_score(tp, tn, fp, fn):
    return (tp + tn) / (tp + tn + (10 * fp) + fn)

def compute_quality_for_corpus(corpus_dir):
    truth_file = os.path.join(corpus_dir, '!truth.txt')
    prediction_file = os.path.join(corpus_dir, '!prediction.txt')
    
    truth_dict = read_classification_from_file(truth_file)
    pred_dict = read_classification_from_file(prediction_file)

    cm = confmat.BinaryConfusionMatrix('SPAM', 'OK')
    cm.compute_from_dicts(truth_dict, pred_dict)
    
    return quality_score(cm.tp, cm.tn, cm.fp, cm.fn)

