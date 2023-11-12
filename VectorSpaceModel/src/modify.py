from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
def transform_data(data, column):
    """
    Transform the data into a vector representation using TF-IDF.
    """
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(data[column])
    # create a DataFrame
    df = pd.DataFrame(vectors.toarray(), columns=vectorizer.get_feature_names_out())
    print(df)
    return vectors, vectorizer
