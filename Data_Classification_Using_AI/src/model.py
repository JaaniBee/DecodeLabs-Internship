from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


def split_data(X, y, test_size=0.2, random_state=42):
    return train_test_split(X, y, test_size=test_size, stratify=y, random_state=random_state)


def build_classifier(model_name="logistic", random_state=42):
    if model_name.lower() == "tree":
        return DecisionTreeClassifier(random_state=random_state)

    return LogisticRegression(max_iter=200, random_state=random_state)


def train_model(model, X_train, y_train):
    model.fit(X_train, y_train)
    return model
