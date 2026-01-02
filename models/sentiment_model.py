from transformers import pipeline

class SentimentModel:
    def __init__(self):
        self._pipeline = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english",
            device='cuda'
        )

    def predict(self, text: str) -> dict:
        """
        Input: raw text
        Output: normalized response
        """
        result = self._pipeline(text)[0]

        return {
            "label": result["label"].lower(),  # positive / negative
            "confidence": float(result["score"])
        }