"""
Word Occurrences
Estimate: 15 minutes
Actual:   9 minutes
"""

#User input
text = input("Enter text: ")
words = text.lower().split()
word_to_count = {}

# Count word occurrences
for word in words:
    word = word.strip('.,!?;:"\'')  # Remove punctuation
    word_to_count[word] = word_to_count.get(word, 0) + 1

# Displays text to analyse word occurence
print(f"\nText: {text}\n")

# Word sorting
unique_words = list(word_to_count.keys())
unique_words.sort()

max_word_length = max(len(word) for word in unique_words)

for word in unique_words:
    print(f"{word:{max_word_length}} : {word_to_count[word]}")
