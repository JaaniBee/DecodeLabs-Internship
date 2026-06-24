import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    return {
        "accuracy": accuracy_score(y_test, y_pred),
        "report": classification_report(y_test, y_pred),
        "confusion_matrix": pd.DataFrame(
            confusion_matrix(y_test, y_pred),
            columns=model.classes_,
            index=model.classes_,
        ),
    }
