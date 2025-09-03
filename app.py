import os
import gradio as gr
from news_classifier import (
    load_or_train,
    predict_text,
    predict_proba_text,
    CATEGORY_ID_TO_NAME,
)


BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, 'model_pipeline.joblib')
# DATA_PATH = r"D:\\AI_Diploma\\AI_diploma\\nlp\\nlp_project\\News_Category_Dataset_v3.json"
DATA_PATH = "dataset_small.json"


pipeline = load_or_train(MODEL_PATH, DATA_PATH)


def infer(text: str):
    if not text or not text.strip():
        return "", {}

    predicted_id = predict_text(pipeline, text)
    label = CATEGORY_ID_TO_NAME.get(int(predicted_id), str(predicted_id))

    probs = predict_proba_text(pipeline, text)
    probs_named = {
        CATEGORY_ID_TO_NAME.get(int(cls), str(cls)): float(p)
        for cls, p in probs.items()
    }

    return label, probs_named


with gr.Blocks(title="News Headline Classifier") as demo:
    gr.Markdown("**Simple interface to classify news headlines**")
    input_text = gr.Textbox(label="Headline", lines=2, placeholder="Type a news headline...")
    submit_btn = gr.Button("Classify")
    out_label = gr.Label(label="Predicted Category")
    out_probs = gr.JSON(label="Class Probabilities")

    submit_btn.click(fn=infer, inputs=input_text, outputs=[out_label, out_probs])


if __name__ == "__main__":
    # For local testing
    # demo.launch(server_name="127.0.0.1", inbrowser=True)
    
    # For public sharing (uncomment the line below and comment the line above)
    
    demo.launch(share=True)

