import string
from nltk.corpus import stopwords

# Stopwords: Common words
print(stopwords.words('english')[:10])

test_sentence = 'This is my first test string. Wow!! we are doing just fine'

# Remove punctuations
no_punctuation = [char for char in test_sentence if char not in string.punctuation]
no_punctuation = "".join(no_punctuation)

# Remove Stopwords
clean_sentence = [word for word in no_punctuation.split(' ') if word not in stopwords.words('english')]
print(clean_sentence)
