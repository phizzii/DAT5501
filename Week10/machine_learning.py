# data preparation: Label features, clean dataset
# feature selection: Identify key features, normalise if required
# test-train split: ~70/30 test/train split is common
# model selection & training: Choose models and train on training data
# model evaluation & optimisation: Test on test data, evaluate and optimise performanc

# use a decision tree to classify and predict data
# evaluate the model with precision and recall
# identify a labelled dataset with a discrete outcome or classification
# example outcomes: insurance claim, loan default, customer purchase
# ideal dataset size: not too big not too small
# eg, 2000 lines of data, 5 features

# do the guitar chord dataset from the uc irvine machine learning repo
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

data = pd.read_csv("guitar_chords_clean.csv")

