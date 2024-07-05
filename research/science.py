import os

from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Define your text data (replace with your actual text content)
# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, 'constitution.txt')).read()

# Create a WordCloud object
wordcloud = WordCloud(width=1000, height=500, background_color="white", min_font_size=1, max_font_size=50).generate(text)

# Display the word cloud
plt.figure(figsize=(10, 10))
plt.imshow(wordcloud)
plt.axis("off")
# plt.title("", fosavefigntsize=20)
plt.savefig("science.png")
# plt.show()