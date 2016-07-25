A CFG Grammar Parser To make out a sentence
- Use the python parser NTLK
- http://stackoverflow.com/questions/17695611/nltk-context-free-grammar-genaration
- Read NLTK Book [http://www.nltk.org/book/] Yeah that's a huge book

- ```from nltk.book import *```: import all books
- ```text1.concordance("monstrous")```: Search monstrous in text1
- ```text1.similar("monstrous")```: Find where monstrous is used similarly
- ```text2.common_contexts(["monstrous", "very"])```: Find where monstrous and very are used in same context
- ```text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])```: See where these words are used as a graph with word count
- ```FreqDist(text1)```: Get A Frequency Distribution for words in text1
- ```text4.collocations()```: Frequent Bigrams with rare words
