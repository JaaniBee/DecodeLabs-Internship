# AI Recommendation Logic System 🎬🤖

A sleek, lightweight Artificial Intelligence Recommendation Engine built from scratch. This project demonstrates core AI logic building, pattern matching, and recommendation concepts without relying on heavy external machine learning libraries.

## 🚀 Features

- **Content-Based Filtering:** Recommends items by matching user preferences against item attributes.
- **Jaccard Similarity Algorithm:** Core logic utilizes set intersection and union to calculate precise percentage matches.
- **Dual Interface:**
  - **Terminal CLI:** A robust Python-based interactive command-line application (`main.py`).
  - **Modern Web App:** A beautiful, glassmorphic UI built in pure HTML/CSS/JS (`index.html`) that runs instantly in any browser.
- **Real-Time Calculation:** Recommendations update dynamically in the web UI based on selected genres.

## 🧠 How it Works

The recommendation system utilizes **Jaccard Similarity** to calculate the distance between what a user likes and what a movie offers:

## 🛠️ Tech Stack

- **Core Logic (CLI):** Pure Python (`recommender.py`, `main.py`)
- **Web Application:** HTML5, Vanilla CSS3 (Custom properties, animations, glassmorphism), Vanilla JavaScript (`script.js`)

## 💻 Usage

### Running the Web Application (Recommended)
No installation required! Simply open the `index.html` file in any modern web browser (Google Chrome, Firefox, Safari).
```bash
# Or start a local server
python -m http.server 8000
# Then visit http://localhost:8000 in your browser
```

### Running the Command Line Interface
Ensure you have Python installed, then run:
```bash
python main.py
```
Follow the interactive terminal prompts to enter your favorite genres.

## 📂 Project Structure
```text
AI_Recommendation_Logic/
├── main.py              # CLI entry point handling user IO
├── recommender.py       # Python core logic & dataset
├── index.html           # Web App structure
├── style.css            # Web App modern styling
├── script.js            # Web App logic (JS port of recommender.py)
└── README.md            # Project documentation
```

## 🤝 Contribution
This project was developed to showcase foundational AI logic concepts. Feel free to fork, enhance the dataset, or implement more complex collaborative filtering algorithms!
