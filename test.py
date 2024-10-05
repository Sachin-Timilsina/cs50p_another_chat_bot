pronoun_map = {
        "i": "you",
        "me": "you",
        "my": "your",
        "you": "I",
        "your": "my"
    }
user_input = 'I feel angry'
words = user_input.lower().split()
# switched_sentence = " ".join([pronoun_map.get(word, word) for word in words])
# print(switched_sentence)
match_words = []
for word in words:
    if word in pronoun_map:
        match_words.append(pronoun_map[word])
    else:
        match_words.append(word)
joined_mapped_words = " ".join(match_words)
print(joined_mapped_words)