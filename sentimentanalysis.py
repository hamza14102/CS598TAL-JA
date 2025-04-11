###############################################################
#All the imports for sentiment analysis & text processing

import nltk
import datetime
import os
import pickle

#String operations for preprocessing text
import string

#Stopwords to remove
from nltk.corpus import stopwords as stopwords
stop_words = set(stopwords.words('english'))
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
numbers = ["0","1","2","3","4","5","6","7","8","9"]

#Word tokenizer
#Use nltk.word_tokenize(line of words)
from nltk.tokenize import word_tokenize

#Word stemmer
#from nltk.stem.snowball import EnglishStemmer

#NLTK Sentiment Analyzer tool
from nltk.sentiment import sentiment_analyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#from nltk.sentiment.vader import SentiText

#NLTK basic sentiment analysis utilities
#demo_liu_hu_lexicon(sentence, plot=False) -> uses Liu Hu lexicon for pos/neg/neu word classification
#demo_sent_subjectivity(text) -> classify sentence as subjective or objective
from nltk.sentiment import util as sentiment_util

#For counting occurences of things in general
from collections import Counter

#These may need to be downloaded?
#nltk.download('punkt_tab')
#nltk.download('stopwords')
nltk.download('subjectivity')
nltk.download('vader_lexicon')

################################################################

#Needs to be set up as class
#Use stemmer.stem(word)
#stemmer = EnglishStemmer()
sia = SentimentIntensityAnalyzer()
#st = SentiText()


def journal_entry(file_name):

    file = open(file_name, "r")
    todays_date = datetime.datetime.now()
    #print(todays_date)

    if os.path.isfile("dated_scores.pkl"):
        dated_scores_file = open('dated_scores.pkl', 'rb')    
        dated_scores = pickle.load(dated_scores_file)

    else:

        dated_scores = dict()
        with open('dated_scores.pkl', 'wb') as fp:
            pickle.dump(dated_scores, fp)


    content = file.readlines()
    processed_lines = []

    ps = dict()
    pos = 0
    neu = 0
    neg = 0

    for line in content:

        line_score = sia.polarity_scores(line)
        pos += line_score["pos"]
        neu += line_score["neu"]
        neg += line_score["neg"]

        #print(sia.polarity_scores(line))

    ps["pos"] = pos
    ps["neu"] = neu
    ps["neg"] = neg

    dated_scores[todays_date] = ps
    with open('dated_scores.pkl', 'wb') as fp:
        pickle.dump(dated_scores, fp)
        #print("pickled")


#journal_entry("test.txt")

#def open_journal_entry(date):
def see_dated_scores():

    if os.path.isfile("dated_scores.pkl"):
        dated_scores_file = open('dated_scores.pkl', 'rb')    
        dated_scores = pickle.load(dated_scores_file)
        print(dated_scores)

#see_dated_scores()