from sklearn.feature_extraction.text import TfidfVectorizer

def transform_data(data, column):
    """
    Transform the data into a vector representation using TF-IDF.
    """
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(data[column])
    return vectors, vectorizer
