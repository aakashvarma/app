from flask import Flask, jsonify
import numpy as np
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import PunktSentenceTokenizer
from nltk.probability import FreqDist
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names

app = Flask(__name__)

# Fetch Api

import json
import codecs
from urllib.request import urlopen
url = "http://letsrant.azurewebsites.net/api/values"
reader = codecs.getreader("utf-8")
obj = json.load(reader(urlopen(url)))

# Data assigning
a = []
b = []
for i in range(0,len(obj)):
    data = obj[i]['Tweet']

# Tokenizer 

    tokenizer = RegexpTokenizer(r'\w+')

    stopWords = set(stopwords.words('english'))
    words = tokenizer.tokenize(data)
    wordsFiltered = []
    
    for w in words:
        if w not in stopWords:
            wordsFiltered.append(w)

    tagged = nltk.pos_tag(wordsFiltered)

    # Sentiment analysis

    # def sent():
    def word_feats(words_):
        return dict([(wor, True) for wor in words_])

    positive_vocab = [ 'awesome', 'outstanding', 'fantastic', 'terrific', 'good', 'nice', 'great', ':)' ]
    negative_vocab = [ 'bad', 'terrible','useless', 'hate', ':(' ]
    neutral_vocab = [ 'movie','the','sound','was','is','actors','did','know','words','not' ]

    positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab]
    negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]
    neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]

    train_set = negative_features + positive_features + neutral_features

    classifier = NaiveBayesClassifier.train(train_set) 

    neg = 0
    pos = 0
    sentence = obj[i]['Tweet']
    sentence = sentence.lower()
    words_ = sentence.split(' ')
    for wor in words_:
        classResult = classifier.classify( word_feats(wor))
        if classResult == 'neg':
            neg = neg + 1
        if classResult == 'pos':
            pos = pos + 1

    pos = str(float(pos)/len(words_))
    neg = str(float(neg)/len(words_))

    # Noun extraction

    sentences = nltk.sent_tokenize(data)   
    
    d = []
    for sent in sentences:
        d = d + nltk.pos_tag(nltk.word_tokenize(sent))
    
    for word in d: 
        if 'NNS' in word[1]: 
            issue = word
        if 'NNS' not in word[1]:
            issue = 'null'
        if 'NNP' in word[1]: 
            place_nnp = word
        if 'NNP' not in word[1]:
            issue = 'null'

    tweetid = obj[i]['TweetID']
    place = obj[i]['PlaceName']

    if place == 'None':
        placename = plane_nnp
    else:
        placename = place

    # coordinates assigning

    coordinates = obj[i]['coordinates']

    # JSON return

    a = {'tweetid':tweetid, 'place':placename, 'issue':issue, 'sentpos':pos, 'sentneg':neg, 'coordinates':coordinates}

    # print (a)

    b.append(a)



@app.route('/', methods=['GET'])
def get_tasks():
    return jsonify({'data': b})

if __name__ == '__main__':
    app.run(debug=True)














