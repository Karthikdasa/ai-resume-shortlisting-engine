import re
import torch
from transformers import pipeline

# Load summarization model once
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn",
    device=0 if torch.cuda.is_available() else -1
)


def clean_text(text):
    """
    Basic cleaning to remove PII and formatting noise.
    """
    text = re.sub(r"\S+@\S+", "", text)
    text = re.sub(r"\+?\d[\d\s\-]{8,}\d", "", text)
    text = re.sub(r"(address|location)[:\-]?.*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"[|•]", " ", text)
    text = re.sub(r"\s{2,}", " ", text)
    return text.strip()


def summarize_text(text, max_chars=3000):
    """
    Generate AI summary using BART.
    """
    text = clean_text(text)
    text = text[:max_chars]

    chunks = [text[i:i+1024] for i in range(0, len(text), 1024)]
    summary = ""

    for chunk in chunks:
        result = summarizer(
            chunk,
            max_length=150,
            min_length=40,
            do_sample=False
        )
        summary += result[0]["summary_text"] + " "

    return summary.strip()