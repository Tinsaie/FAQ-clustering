import re

def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text.lower())
    return text.strip()
