###############################################################
#All the imports

import nltk
import datetime
import os
import pickle

from nltk import tokenize

#NLTK Sentiment Analyzer tool
from nltk.sentiment import sentiment_analyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#from nltk.sentiment.vader import SentiText

#These may need to be downloaded?
#nltk.download('punkt_tab')
#nltk.download('stopwords')
#nltk.download('subjectivity')
#nltk.download('vader_lexicon')

################################################################

#Needs to be set up as class
#Use stemmer.stem(word)
#stemmer = EnglishStemmer()
sia = SentimentIntensityAnalyzer()
#st = SentiText()


def journal_entry(file_name):
    """Open a new journal entry as a text file.
       Use SentimentIntensityAnalyzer to score.
       Save scores and entry in a pickled dictionary.
    """

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
    #print(content)

    ps = dict()
    pos = 0
    neu = 0
    neg = 0
    compound = 0


    for line in content:

        line_score = sia.polarity_scores(line)
        pos += line_score["pos"]
        neu += line_score["neu"]
        neg += line_score["neg"]
        compound += line_score["compound"]
        
        #print(line)
        #print(sia.polarity_scores(line))

    ps["pos"] = pos
    ps["neu"] = neu
    ps["neg"] = neg
    ps["compound"] = compound
    ps["entry"] = content

    dated_scores[todays_date] = ps
    with open('dated_scores.pkl', 'wb') as fp:
        pickle.dump(dated_scores, fp)
        #print("pickled")


#journal_entry("test.txt")

#def open_journal_entry(date):
     """Open a journal entry by date
        and print the content.
     """
def see_dated_scores():
    """Open the pickled dictonary and print
       all the content.
    """

    if os.path.isfile("dated_scores.pkl"):
        dated_scores_file = open('dated_scores.pkl', 'rb')    
        dated_scores = pickle.load(dated_scores_file)
        print(dated_scores)

#see_dated_scores()
