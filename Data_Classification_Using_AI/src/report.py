from pathlib import Path


def generate_report_html(output_path, df, metrics, model_name="logistic"):
    summary_html = df.describe().to_html(classes="table", border=0)
    distribution_html = df["species"].value_counts().to_frame("count").to_html(classes="table", border=0)
    head_html = df.head().to_html(index=False, classes="table", border=0)
    confusion_html = metrics["confusion_matrix"].to_html(classes="table", border=0)
    classification_html = f"<pre>{metrics['report']}</pre>"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Data Classification Report</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 24px; line-height: 1.5; background: #f9f9f9; color: #222; }}
    h1, h2 {{ color: #1f4e79; }}
    .table {{ border-collapse: collapse; width: 100%; margin-bottom: 24px; }}
    .table th, .table td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
    .table th {{ background: #e8f1fb; }}
    pre {{ background: #fff; border: 1px solid #ddd; padding: 12px; overflow: auto; }}
    .metric {{ font-weight: bold; padding: 8px 0; }}
    .section {{ background: #fff; border: 1px solid #ddd; padding: 18px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0 1px 2px rgba(0,0,0,0.05); }}
  </style>
</head>
<body>
  <h1>Data Classification Report</h1>
  <div class="section">
    <h2>Model</h2>
    <p>Classifier: <strong>{model_name.title()}</strong></p>
    <p class="metric">Test accuracy: <strong>{metrics['accuracy']:.4f}</strong></p>
  </div>
  <div class="section">
    <h2>Dataset Preview</h2>
    {head_html}
  </div>
  <div class="section">
    <h2>Dataset Summary</h2>
    {summary_html}
  </div>
  <div class="section">
    <h2>Class Distribution</h2>
    {distribution_html}
  </div>
  <div class="section">
    <h2>Classification Report</h2>
    {classification_html}
  </div>
  <div class="section">
    <h2>Confusion Matrix</h2>
    {confusion_html}
  </div>
</body>
</html>"""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    return output_path
