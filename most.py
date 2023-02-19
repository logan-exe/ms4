import string
import matplotlib.pyplot as plt

# Read the text file
with open('shakespeare.txt', 'r') as file:
    text = file.read()

# Convert all text to lowercase
text = text.lower()

# Remove punctuation and digits from the text
text = text.translate(str.maketrans('', '', string.punctuation + string.digits))

# Split the text into individual words
words = text.split()

# Load the stopwords
with open('stopwords.txt', 'r') as file:
    stopwords = set(file.read().split())

# Remove stopwords from the list of words
words = [word for word in words if word not in stopwords]

# Create a dictionary to store the word counts
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Sort the word counts in descending order
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# Select the top 10 words
top_words = [pair[0] for pair in sorted_word_counts[:10]]

# Count the frequency of each top word in the text
word_frequencies = []
for word in top_words:
    frequency = words.count(word)
    word_frequencies.append(frequency)

# Create a radar chart of the top 10 words
angles = [n / float(len(top_words)) * 2 * 3.14159 for n in range(len(top_words))]
angles += angles[:1]
word_frequencies += word_frequencies[:1]
plt.polar(angles, word_frequencies)
plt.xticks(angles[:-1], top_words)
plt.title('Most Used Words in Shakespeare\'s Works')
plt.show()
