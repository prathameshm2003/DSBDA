#Tokenization
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords
#Text
text='Real madrid is set to win the UCL for the season . Benzema might win Balon dor . Salah might be runner up .
#
tokens_sents = nltk.sent_tokenize(text)
print(tokens_sents)
#
tokens_words = nltk.word_tokenize(text)
print(tokens_words)

#Stemming
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
#
words = ["eating", "eats", "eat", "ate", "adjustable", "rafting", "ability", "meeting"]

for word in words:
    print(word, "|", stemmer.stem(word))

#Lemmitization
import spacy
#
nlp = spacy.load("en_core_web_sm")

doc = nlp("Mando talked for 3 hours although talking isn't his thing")
doc = nlp("eating eats eat ate adjustable rafting ability meeting better")
for token in doc:
    print(token, " | ", token.lemma_)
