from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(vectors):
    """
    Calculate the cosine similarity between vectors.
    """
    similarity_matrix = cosine_similarity(vectors)
    return similarity_matrix
