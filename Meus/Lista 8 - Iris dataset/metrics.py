import numpy as np
from sklearn.metrics import confusion_matrix

def accuracy_score(y, y_pred):
    cm = confusion_matrix(y, y_pred)
    return np.sum(np.diagonal(cm))/np.sum(cm)

def precision_score(y, y_p):
    cm = confusion_matrix(y, y_p, labels=np.unique(y))
    pond = np.unique(y, return_counts=True)[1]
    pre = []
    for i in range(cm.shape[0]): 
        pre.append((pond[i] * cm[i,i]) / np.sum(cm[:,i]))
    return np.sum(pre)/np.sum(pond)

def recall_score(y, y_p):
    cm = confusion_matrix(y, y_p, labels=np.unique(y))
    pond = np.unique(y, return_counts=True)[1]
    pre = []
    for i in range(cm.shape[0]): 
        pre.append((pond[i] * cm[i,i]) / np.sum(cm[i]))
    return np.sum(pre)/np.sum(pond)

def f1_measure_score(y, y_p):
    recall = recall_score(y, y_p)
    precision = precision_score(y, y_p)
    return 2 * ((precision * recall) / (precision + recall))