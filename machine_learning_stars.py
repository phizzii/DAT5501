import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.tree import export_graphviz
import graphviz
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/stardataset.csv")

# features n target
X = df[["temperature", "radius", "brightness", "colour"]]
y = df["type"]


# preprocessing > has one categorical feature (colour), machine learning model can't use text labels > convert to one-hot encoded columns like changing red to [1,0,0,0,0] using one hot encoder function and using a pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ("colour_ohe", OneHotEncoder(), ["colour"]),
    ],
    remainder="passthrough"   # keep numeric columns
)


clf = DecisionTreeClassifier(max_depth=5, random_state=42)

# pipeline = preprocessing + classifier
model = Pipeline(steps=[
    ("preprocess", preprocessor),
    ("classifier", clf)
])

# test train split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# training model
model.fit(X_train, y_train)

# PREDICT
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred, zero_division=0))


# using graph viz to visualise the thing
# to export, i need the feature names one hot encoding.
ohe = model.named_steps["preprocess"].named_transformers_["colour_ohe"]
ohe_features = list(ohe.get_feature_names_out(["colour"]))
final_feature_names = ohe_features + ["temperature", "radius", "brightness"]

dot_data = export_graphviz(
    model.named_steps["classifier"],
    out_file=None,
    feature_names=final_feature_names,
    class_names=model.named_steps["classifier"].classes_,
    filled=True,
    rounded=True,
    special_characters=True
)

graph = graphviz.Source(dot_data)
try:
    graph.render("star_type_tree", format="pdf", view=True)
except:
    print("Graphviz not installed — skipping tree export.")


# feature importance
importances = pd.Series(
    model.named_steps["classifier"].feature_importances_,
    index=final_feature_names
).sort_values(ascending=False)

plt.figure(figsize=(12,5))
importances.plot(kind="bar", color="skyblue")
plt.title("Feature Importance - Star Classification")
plt.ylabel("Importance")
plt.show()

from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

extra_models = {
    "Random Forest": RandomForestClassifier(random_state=42),
    "KNN": KNeighborsClassifier(),
    "SVM": SVC()
}

for name, model_base in extra_models.items():
    pipeline = Pipeline([
        ("preprocess", preprocessor),
        ("classifier", model_base)
    ])

    pipeline.fit(X_train, y_train)
    preds = pipeline.predict(X_test)

    print("\n\n==============================")
    print(f"MODEL: {name}")
    print("==============================")
    print(classification_report(y_test, preds, zero_division=0))