import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("obama.txt")
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
