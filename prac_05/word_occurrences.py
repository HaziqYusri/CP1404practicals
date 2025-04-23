"""
Word Occurrences
Estimate: 20 minutes
Actual:   10 minutes
"""

#User input
text = input("Enter text: ")
words = text.lower().split()
word_to_count = {}

# Count word occurrences
for word in words:
    word = word.strip('.,!?;:"\'')  # Remove punctuation
    word_to_count[word] = word_to_count.get(word, 0) + 1


