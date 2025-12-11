# use a decision tree to classify and predict data
# evaluate the model with precision and recall
# identify a labelled dataset with a discrete outcome or classification
# example outcomes: insurance claim, loan default, customer purchase
# ideal dataset size: not too big not too small
# eg, 2000 lines of data, 5 features

import pytest
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import precision_score, recall_score

# making fake data for testing
@pytest.fixture
def sample_stars_df():
    data = {
        "temperature": [3000, 4500, 6000, 7500, 9000],
        "radius": [0.8, 1.0, 1.2, 1.5, 2.0],
        "brightness": [0.5, 1.0, 1.3, 2.0, 3.5],
        "colour": ["red", "orange", "yellow", "white", "blue"],
        "type": ["M", "K", "G", "A", "B"]   # discrete classes
    }
    return pd.DataFrame(data)

# testing the preprocessing and the one hot encoding stuff (what ohe stands for)
def test_preprocessing_ohe(sample_stars_df):
    preprocessor = ColumnTransformer(
        transformers=[
            ("colour_ohe", OneHotEncoder(), ["colour"])
        ],
        remainder="passthrough"
    )

    # fit-transform only features (X)
    X = sample_stars_df[["temperature", "radius", "brightness", "colour"]]
    transformed = preprocessor.fit_transform(X)

    # expect 5 samples
    assert transformed.shape[0] == len(sample_stars_df)

    # expect 5 encoded colour categories + 3 numeric columns
    expected_features = len(preprocessor.named_transformers_["colour_ohe"].categories_[0])
    assert transformed.shape[1] == expected_features + 3


# making sure the train test split, making sure it matches the original dataset in length
def test_train_test_split(sample_stars_df):
    X = sample_stars_df[["temperature", "radius", "brightness", "colour"]]
    y = sample_stars_df["type"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.4, random_state=42
    )

    # sizes must add up
    assert len(X_train) + len(X_test) == len(X)
    assert len(y_train) + len(y_test) == len(y)

    # maintain row correspondence
    assert X_train.shape[0] == y_train.shape[0]
    assert X_test.shape[0] == y_test.shape[0]


# checking whether the full pipeline (preprocessing + model) can be fit and used for prediction without errors. if the model can't fit the whole thing will fail
def test_decision_tree_fit_predict(sample_stars_df):
    X = sample_stars_df[["temperature", "radius", "brightness", "colour"]]
    y = sample_stars_df["type"]

    preprocessor = ColumnTransformer(
        transformers=[("colour_ohe", OneHotEncoder(), ["colour"])],
        remainder="passthrough"
    )

    clf = DecisionTreeClassifier(max_depth=3, random_state=42)

    pipe = Pipeline([
        ("preprocess", preprocessor),
        ("classifier", clf)
    ])

    pipe.fit(X, y)
    preds = pipe.predict(X)

    # shape check
    assert len(preds) == len(y)

    # labels must be valid star types
    assert all(p in y.unique() for p in preds)

# confirming that evaluation metrics (precision and recall) can be computed from the model outputs. basically making sure that theres no invalid values being spat out
def test_precision_recall_computable(sample_stars_df):
    X = sample_stars_df[["temperature", "radius", "brightness", "colour"]]
    y = sample_stars_df["type"]

    preprocessor = ColumnTransformer(
        transformers=[("colour_ohe", OneHotEncoder(), ["colour"])],
        remainder="passthrough"
    )

    model = Pipeline([
        ("preprocess", preprocessor),
        ("classifier", DecisionTreeClassifier(max_depth=2, random_state=42))
    ])

    model.fit(X, y)
    preds = model.predict(X)

    # macro precision and recall must be floats between 0 and 1
    precision = precision_score(y, preds, average="macro", zero_division=0)
    recall = recall_score(y, preds, average="macro", zero_division=0)

    assert 0.0 <= precision <= 1.0
    assert 0.0 <= recall <= 1.0
