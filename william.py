import string
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the Complete Works of William Shakespeare
with open('shakespeare.txt', 'r') as f:
    shakespeare = f.read()

# Remove punctuation and convert to lowercase
shakespeare = shakespeare.translate(str.maketrans('', '', string.punctuation)).lower()

# Split the text into words
words = shakespeare.split()

# Filter out stopwords
with open('stopwords.txt', 'r') as f:
    stopwords = [line.strip() for line in f]
words = [word for word in words if word not in stopwords]

# Calculate the frequency of each word
word_freq = Counter(words)

# Generate the word cloud
wordcloud = WordCloud(width=800, height=800, background_color='white').generate_from_frequencies(word_freq)

# Display the word cloud
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()
