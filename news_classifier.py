import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib


CATEGORY_NAME_TO_ID = {
    'SPORTS': 0,
    'CRIME': 1,
    'EDUCATION': 2,
    'COMEDY': 3,
}

CATEGORY_ID_TO_NAME = {value: key for key, value in CATEGORY_NAME_TO_ID.items()}
CATEGORIES = list(CATEGORY_NAME_TO_ID.keys())


def load_or_train(model_path: str, data_path: str) -> Pipeline:
    """Load a saved pipeline if available, otherwise train and save a new one."""
    if os.path.exists(model_path):
        return joblib.load(model_path)

    df = pd.read_json(data_path, lines=True)[['headline', 'category']]
    df = df[df['category'].isin(CATEGORIES)].copy()

    # Balance classes
    min_samples = df['category'].value_counts().loc[CATEGORIES].min()
    frames = [
        df[df['category'] == name].sample(min_samples, random_state=22)
        for name in CATEGORIES
    ]
    df_balanced = pd.concat(frames, axis=0).copy()
    df_balanced['label'] = df_balanced['category'].map(CATEGORY_NAME_TO_ID)

    X_train, X_test, y_train, y_test = train_test_split(
        df_balanced['headline'],
        df_balanced['label'],
        test_size=0.2,
        random_state=22,
        stratify=df_balanced['label'],
    )

    pipeline = Pipeline([
        ('vectorizer', CountVectorizer(ngram_range=(1, 3))),
        ('classifier', MultinomialNB()),
    ])

    pipeline.fit(X_train, y_train)

    try:
        y_pred = pipeline.predict(X_test)
        report = classification_report(y_test, y_pred)
        print(report)
    except Exception:
        pass

    joblib.dump(pipeline, model_path)
    return pipeline


def predict_text(pipeline: Pipeline, text: str) -> int:
    return int(pipeline.predict([text])[0])


def predict_proba_text(pipeline: Pipeline, text: str) -> dict:
    probabilities = pipeline.predict_proba([text])[0]
    return {int(cls): float(p) for cls, p in zip(pipeline.classes_, probabilities)}


