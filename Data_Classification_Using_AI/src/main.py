from pathlib import Path

from src.data_loader import load_iris_dataset, summarize_dataset
from src.model import split_data, build_classifier, train_model
from src.evaluate import evaluate_model
from src.report import generate_report_html


def main():
    X, y, df, feature_names, target_names, description = load_iris_dataset()

    print("==== Dataset Overview ====")
    print(description.split("\n\n")[0])
    print("\n==== First rows ====")
    print(df.head().to_string(index=False))
    print("\n==== Summary ====")
    print(summarize_dataset(df))

    X_train, X_test, y_train, y_test = split_data(X, y)
    print(f"\nTrain size: {len(X_train)}, Test size: {len(X_test)}")

    model = build_classifier("logistic")
    model = train_model(model, X_train, y_train)

    print("\n==== Model Evaluation ====")
    metrics = evaluate_model(model, X_test, y_test)
    print(f"Accuracy: {metrics['accuracy']:.4f}")
    print("\nClassification report:")
    print(metrics["report"])
    print("\nConfusion matrix:")
    print(metrics["confusion_matrix"].to_string())

    report_path = Path("report.html")
    generate_report_html(report_path, df, metrics, model_name="logistic")
    print(f"\nHTML report created: {report_path.resolve()}")
    print("Open report.html in Google Chrome to view the visualization in a browser.")


if __name__ == "__main__":
    main()
