from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# i was taking a ride in the car.
# i was riding in the car.

ps = PorterStemmer()

example_words = ["python", "pythoner", "pythoning", "pythoned","pythonly"]


new_text = "It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly atleast once."

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))
