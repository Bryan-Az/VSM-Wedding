from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
def calculate_similarity(vectors, vectorizer, terms):
    """
    Calculate the cosine similarity between vectors.
    """
    term_similarities = {}
    for term in terms:
        # Get the index of the term in the feature names
        term_index = np.where(vectorizer.get_feature_names_out() == term)
        if term_index[0].size > 0:
            term_index = term_index[0][0]
            # Get the vector representation of the term
            term_vector = vectors[:, term_index].reshape(1, -1)
            # Calculate the cosine similarity between the term vector and each term vector
            term_similarities[term] = cosine_similarity(vectors.T, term_vector).flatten()
        else:
            print(f"Term '{term}' not found in the vocabulary.")
    term_df_similarities = pd.DataFrame(term_similarities)
    print(term_df_similarities)
    # collate all the arrays in the dictionary into a single array of arrays (cosine similarity matrix)
    term_similarities = np.stack(list(term_similarities.values()))
    return term_similarities
    
