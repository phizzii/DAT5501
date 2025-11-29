# use a decision tree to classify and predict data
# evaluate the model with precision and recall
# identify a labelled dataset with a discrete outcome or classification
# example outcomes: insurance claim, loan default, customer purchase
# ideal dataset size: not too big not too small
# eg, 2000 lines of data, 5 features

# test_guitar_chords.py
import pytest
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.tree import DecisionTreeClassifier
from Week10.machine_learning import parse_finger_positions  # import your function if in a separate file

# sample minimal dataset for testing
@pytest.fixture
def sample_df():
    data = {
        'FINGER_POSITIONS': ['0,2,2,1,0,0', 'x,0,2,2,1,0', '1,3,3,2,1,1'],
        'CHORD_STRUCTURE': ['1;3;5', '1;b3;5', '1;3;5;b7'],
        'CHORD_TYPE': ['maj', 'm', '7']
    }
    return pd.DataFrame(data)

def test_parse_finger_positions():
    assert parse_finger_positions('0,1,2,x,4,5') == [0, 1, 2, -1, 4, 5]
    assert parse_finger_positions('x,x,x,x,x,x') == [-1, -1, -1, -1, -1, -1]
    assert parse_finger_positions('1,2,3,4,5,6') == [1, 2, 3, 4, 5, 6]

def test_structure_encoding(sample_df):
    sample_df['STRUCTURE_LIST'] = sample_df['CHORD_STRUCTURE'].apply(lambda x: x.split(';'))
    mlb = MultiLabelBinarizer()
    features = mlb.fit_transform(sample_df['STRUCTURE_LIST'])
    # checkign that shape matches rows x unique intervals
    assert features.shape[0] == sample_df.shape[0]
    assert features.shape[1] == len(set(sum(sample_df['STRUCTURE_LIST'].tolist(), [])))

def test_train_test_split_shapes(sample_df):
    X = pd.DataFrame([[0,1,2], [1,2,3], [3,4,5]])
    y = pd.Series([0,1,2])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    assert len(X_train) + len(X_test) == len(X)
    assert len(y_train) + len(y_test) == len(y)

def test_decision_tree_fit_predict(sample_df):
    sample_df['FINGER_POS_ARRAY'] = sample_df['FINGER_POSITIONS'].apply(parse_finger_positions)
    finger_df = pd.DataFrame(sample_df['FINGER_POS_ARRAY'].tolist(), columns=[f'F{i}' for i in range(1,7)])
    sample_df['STRUCTURE_LIST'] = sample_df['CHORD_STRUCTURE'].apply(lambda x: x.split(';'))
    mlb = MultiLabelBinarizer()
    structure_df = pd.DataFrame(mlb.fit_transform(sample_df['STRUCTURE_LIST']), columns=mlb.classes_)
    X = pd.concat([finger_df, structure_df], axis=1)
    y = sample_df['CHORD_TYPE']

    clf = DecisionTreeClassifier(max_depth=2, random_state=42)
    clf.fit(X, y)
    preds = clf.predict(X)
    # checking predictions return correct number of elements
    assert len(preds) == len(y)
    # checking all predicted labels exist in training labels
    assert all(p in y.values for p in preds)