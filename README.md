# Vector Space Model for Weddings


## Project Description
*This code is part of an assignment for my CMPE 256 class at SJSU by Chandrasekar Vappulapati that creates a Vector Space Model for predicting a user's preferred wedding gown based on their user data and document features related to wedding store items such as wedding gowns, roses, diamond rings, and other related items. The code processes the user data and document features to create a vector representation of each document, which is then used to calculate the cosine similarity between the user data and each document. The document with the highest cosine similarity score is considered the predicted preferred wedding gown for the user.*

## Project Structure
This project follows the SEMMA methodology, which stands for Sample, Explore, Modify, Model, and Assess. The basic project structure is as follows:

- Sample: Collect and preprocess the data.
- Explore: Perform exploratory data analysis to understand the data.
- Modify: Transform the data to prepare it for modeling.
- Model: Build and train the Vector Space Model.
- Assess: Evaluate the performance of the model.

## Packages Used
The following packages will be used in this project:
- pandas: for data manipulation and analysis.
- numpy: for numerical operations.
- scikit-learn: for building and training the Vector Space Model.
- matplotlib: for data visualization.

## Conclusion
The Vector Space Model was successfully built and used to predict a user's preferred wedding gown based on their user data and document features **(cosine similarity of tfidf representation of document content as compared to the vocabulary vector)** related to wedding store items. The model achieved a max similarity of 95% on the test data, which is a good performance. The following images show the conclusion of the project.

Similarity scores of the vocab vector Vocabulary Vector (Gown, Rose, Diamond, Flowers)
![Conclusion of the Vector Space Model for Weddings](/VectorSpaceModel/images/conclusion_VSM.png)

Search Space
![Wordcloud of the Vector Space Model for Weddings](/VectorSpaceModel/images/wordcloud_VSM.png)


