def extract_keywords(texts, model):
    combined = ' '.join(texts)
    keywords = model.extract_keywords(combined, 
                                   keyphrase_ngram_range=(1, 2),
                                   stop_words='english',
                                   top_n=3)
    return [kw[0] for kw in keywords]
