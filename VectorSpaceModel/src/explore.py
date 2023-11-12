import matplotlib.pyplot as plt
#import the wordcloud library
from wordcloud import WordCloud


def plot_data(data, column):
    """
    Plot a word cloud of the text data from the 'content' column.
    """
    text = ' '.join(data[column].tolist())
    wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
