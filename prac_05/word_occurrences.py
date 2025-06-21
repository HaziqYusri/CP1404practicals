"""
Word Occurrences
Estimate: 15 minutes
Actual:    minutes
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

