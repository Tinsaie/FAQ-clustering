import numpy as np

def get_representative(questions, embeddings):
    if len(questions) == 1:
        return questions[0]
    sim_matrix = np.inner(embeddings, embeddings)
    scores = np.mean(sim_matrix, axis=1)
    return questions[np.argmax(scores)]
