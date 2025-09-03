# News Headline Classifier (Scikit-learn + Gradio)

Classify news headlines into four categories: SPORTS, CRIME, EDUCATION, COMEDY. The model uses CountVectorizer (1-3 n-grams) with Multinomial Naive Bayes. A simple Gradio web UI is included for quick testing.

## Features
- Balanced sampling across selected categories
- Train or load cached pipeline (joblib)
- Gradio UI for interactive inference
- Probability breakdown per class

## Tech Stack
- Python, pandas, scikit-learn, joblib
- Gradio for the web interface

## Project Structure
```
nlp_project/
├─ app.py                  # Gradio app entrypoint
├─ news_classifier.py      # Training/loading and inference helpers
├─ requirements.txt
├─ README.md
└─ News_Category_Dataset_v3.json (local dataset, not committed)
```

## Quickstart (Windows / PowerShell)
```powershell
cd d:\AI_Diploma\AI_diploma\nlp\nlp_project
py -3 -m venv .venv
.\.venv\Scripts\python -m pip install --upgrade pip
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python app.py
```
Then open the local URL printed by Gradio (for example, http://127.0.0.1:7863/).

- Change port if needed:
```powershell
.\.venv\Scripts\python app.py --server.port 7861
```
- Stop the server: press Ctrl+C in the terminal.

## Re-opening the project later
If you close the terminal or reboot, activate the virtual environment and run the app again:
```powershell
cd d:\AI_Diploma\AI_diploma\nlp\nlp_project
.\.venv\Scripts\activate
python app.py
```
If activation is not available, use the absolute path:
```powershell
.\.venv\Scripts\python app.py
```

## Training notes
- On first run, the app trains a balanced classifier on the four categories and saves it to model_pipeline.joblib. Subsequent runs will load the saved pipeline.
- Update CATEGORIES in news_classifier.py if you want different classes (ensure the dataset contains them).

## License
MIT
