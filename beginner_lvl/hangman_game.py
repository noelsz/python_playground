import nltk
import random

nltk.download('words')

word_list = list(set(w.lower() for w in nltk.corpus.words.words()))

word = random.choice(word_list)

print(word)