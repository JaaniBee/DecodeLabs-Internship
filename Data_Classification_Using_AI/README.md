# Data Classification Using AI

A compact Python project demonstrating a supervised learning workflow for classifying the Iris dataset.

## Project overview

This project loads a real dataset, performs exploratory data analysis, splits the data into training and test sets, trains a classification model, and evaluates the results.

The project also generates an HTML report that can be opened in Google Chrome for a browser-based view of the model summary, dataset preview, and evaluation metrics.

## Included files

- `src/data_loader.py`: loads and summarizes the Iris dataset
- `src/model.py`: prepares data splits and builds the classifier
- `src/evaluate.py`: computes accuracy, classification report, and confusion matrix
- `src/report.py`: generates a Chrome-friendly HTML results report
- `src/main.py`: runs the end-to-end project workflow
- `requirements.txt`: Python dependencies for running the project

## How to run

1. Open PowerShell and go to the project folder:

```powershell
cd "c:\Users\JAANI BEE\OneDrive\Desktop\Data_Classification_Using_AI"
```

2. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install required packages:

```powershell
pip install -r requirements.txt
```

4. Run the project:

```powershell
python -m src.main
```

5. Open the generated report in Google Chrome:

```powershell
# Recommended: open the file directly in Windows Explorer
explorer report.html

# Or open with Chrome using a file URI if the simple command fails
start chrome "file:///c:/Users/JAANI BEE/OneDrive/Desktop/Data_Classification_Using_AI/report.html"
```

## Notes

- The model uses the built-in Iris dataset from Scikit-Learn.
- The default classifier is Logistic Regression, but you can switch to a Decision Tree by changing the model in `src/model.py`.
- The HTML report file will be created as `report.html` in the project root.
