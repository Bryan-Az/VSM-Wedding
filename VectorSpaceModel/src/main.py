from sample import load_data, preprocess_data
from explore import plot_data
from modify import transform_data
from model import calculate_similarity
from assess import get_top_similar

def main():
    # Sample
    data = load_data('data/wedding_data.csv')
    data = preprocess_data(data)

    # Explore
    plot_data(data, 'wedding_gown')

    # Modify
    vectors, vectorizer = transform_data(data, 'wedding_gown')

    # Model
    similarity_matrix = calculate_similarity(vectors)

    # Assess
    top_similar = get_top_similar(similarity_matrix, 5)
    print(top_similar)

if __name__ == "__main__":
    main()
