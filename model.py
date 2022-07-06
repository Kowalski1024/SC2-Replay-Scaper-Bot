import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier
import pickle

datasets = ["data/datasets/" + file for file in os.listdir("data\\datasets")]
units = [*range(16, 16+19), *range(80, 80 + 19)]
structures = [*range(36, 36+16), *range(100, 100+16)]
state = list(range(6))

train_units = list(range(144, 144+19))
train_structures = list(range(164, 164+16))

clf = RandomForestClassifier(n_estimators=500, max_depth=10)

for file in datasets:
    train_X = pd.read_csv(file, skiprows=1, header=None, usecols=state+units+structures)
    train_y = pd.read_csv(file, skiprows=1, header=None, usecols=train_units+train_structures)
    clf.fit(train_X, train_y)
    print('f')

filename = 'finalized_model.sav'
pickle.dump(clf, open(filename, 'wb'))
