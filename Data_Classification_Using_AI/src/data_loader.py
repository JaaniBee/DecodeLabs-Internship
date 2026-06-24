import pandas as pd
from sklearn.datasets import load_iris


def load_iris_dataset():
    iris = load_iris(as_frame=True)
    df = iris.frame.copy()
    df.columns = [*iris.feature_names, "target"]
    df["species"] = df["target"].map({i: name for i, name in enumerate(iris.target_names)})

    X = df[iris.feature_names].copy()
    y = df["species"].copy()

    return X, y, df, iris.feature_names, iris.target_names, iris.DESCR


def summarize_dataset(df: pd.DataFrame) -> str:
    summary = []
    summary.append(f"Shape: {df.shape}")
    summary.append(df.describe().to_string())
    summary.append("\nClass distribution:\n" + df["species"].value_counts().to_string())
    return "\n\n".join(summary)
