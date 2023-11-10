import numpy as np

def get_top_similar(similarity_matrix, top_n):
    """
    Get the top N most similar documents for each document.
    """
    top_similar = np.argsort(-similarity_matrix, axis=1)[:, :top_n]
    return top_similar
