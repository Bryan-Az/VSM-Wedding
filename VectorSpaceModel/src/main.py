from load import load_metadata
from sample import preprocess_data
from explore import plot_data
from modify import transform_data
from model import calculate_similarity
from assess import get_top_similar

def main():
    # load metadata
    doc_df = load_metadata('./src/data')

    # Preprocess
    doc_df = preprocess_data(doc_df)

    # Explore
    plot_data(doc_df, 'content')

    # Modify
    vectors, vectorizer = transform_data(doc_df, 'content')

    # Model
    similarity_matrix = calculate_similarity(vectors, vectorizer, ['gown', 'rose', 'diamond', 'flowers'])

    # Assess
    top_similar = get_top_similar(similarity_matrix, 5)
    print(top_similar)

if __name__ == "__main__":
    main()
