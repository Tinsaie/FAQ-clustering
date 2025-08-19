from collections import defaultdict
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sentence_transformers import SentenceTransformer
from keybert import KeyBERT

from .keywords import extract_keywords
from .representative import get_representative

def cluster_questions(questions):
    # Initialize models
    embedder = SentenceTransformer('all-mpnet-base-v2')
    kw_model = KeyBERT('paraphrase-MiniLM-L6-v2')
    
    # Get embeddings
    embeddings = embedder.encode(questions)
    
    # Optimal clustering
    clustering = AgglomerativeClustering(
        n_clusters=None,
        metric='cosine',
        linkage='average',
        distance_threshold=0.55
    )
    labels = clustering.fit_predict(embeddings)
    
    # Organize clusters
    clusters = defaultdict(list)
    for idx, label in enumerate(labels):
        clusters[label].append(questions[idx])
    
    # Prepare output
    results = []
    for label, cluster_questions in clusters.items():
        cluster_embeds = embeddings[[questions.index(q) for q in cluster_questions]]
        rep = get_representative(cluster_questions, cluster_embeds)
        keywords = extract_keywords(cluster_questions, kw_model)
        
        results.append({
            'label': label,
            'size': len(cluster_questions),
            'theme': ', '.join(keywords),
            'representative': rep,
            'all_questions': cluster_questions
        })
    
    # Sort by cluster size
    results.sort(key=lambda x: x['size'], reverse=True)
    return results
