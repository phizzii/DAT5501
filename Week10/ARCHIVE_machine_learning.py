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
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import graphviz
from sklearn.tree import export_graphviz
import matplotlib.pyplot as plt

 # convert finger positions to numerical array
def parse_finger_positions(fp):
    # 'x' or None -> -1, numeric strings -> int
    return [int(f) if f.isdigit() else -1 for f in fp.replace(" ", "").split(",")]

def main():
    df = pd.read_csv('datasets/guitar_chords_clean.csv')

    df['FINGER_POS_ARRAY'] = df['FINGER_POSITIONS'].apply(parse_finger_positions)

    # make chord structure (intervals) into one-hot encoded features
    # "1;3;5;b7" -> [1,0,1,0,...]
    df['STRUCTURE_LIST'] = df['CHORD_STRUCTURE'].apply(lambda x: x.split(';'))
    mlb = MultiLabelBinarizer()
    structure_features = mlb.fit_transform(df['STRUCTURE_LIST'])
    structure_df = pd.DataFrame(structure_features, columns=mlb.classes_)

    # combine them
    finger_df = pd.DataFrame(df['FINGER_POS_ARRAY'].tolist(), columns=[f'F{i}' for i in range(1, 7)])
    X = pd.concat([finger_df, structure_df], axis=1)

    # make target chord type
    y = df['CHORD_TYPE']

    # train test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # train decision tree
    clf = DecisionTreeClassifier(max_depth=10, random_state=42)
    clf.fit(X_train, y_train)

    # evalutate it
    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred, zero_division=0))  # zero_division avoids warnings

    # try do it in graphviz
    dot_data = export_graphviz(
        clf,
        out_file=None,
        feature_names=X.columns,
        class_names=clf.classes_,
        filled=True,
        rounded=True,
        special_characters=True,
        max_depth=5
    )
    graph = graphviz.Source(dot_data)
    try:
        graph.render("guitar_chord_tree", format='pdf', view=True)
    except FileNotFoundError:
        print("grpahviz not installed so we skip!")
        

    # feature importance
    import pandas as pd
    importances = pd.Series(clf.feature_importances_, index=X.columns)
    importances = importances.sort_values(ascending=False)

    plt.figure(figsize=(12,6))
    importances.plot(kind='bar', color='skyblue')
    plt.title("Feature Importance in Chord Classification")
    plt.ylabel("Importance")
    plt.show()

    # do classifiers

if __name__=="__main__":
    main()