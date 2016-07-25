import nltk
input_sentence = "I Facebook love"
text = nltk.word_tokenize(input_sentence)
print(nltk.sent_tokenize(input_sentence))
list_of_tokens = nltk.pos_tag(text)
print(list_of_tokens)
