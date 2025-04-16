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

    #todays_date represents exact datetime, in case of multiple entries per day
    todays_date = datetime.datetime.now()
    

    #string_today represents the general month day, year
    #This should make it easier to search for entries by date
    string_today = todays_date.strftime("%B %d, %Y")
    

    if os.path.isfile("dated_scores.pkl"):
        dated_scores_file = open('dated_scores.pkl', 'rb')    
        dated_scores = pickle.load(dated_scores_file)

    else:

        dated_scores = dict()
        with open('dated_scores.pkl', 'wb') as fp:
            pickle.dump(dated_scores, fp)


    content = file.readlines()
    

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
        

    ps["pos"] = pos
    ps["neu"] = neu
    ps["neg"] = neg
    ps["compound"] = compound
    ps["entry"] = content
    
    #Check if there is already an entry for the given date
    if string_today in dated_scores:

        #If there is, access the existing dictionary for this day
        existing_entry = dated_scores[string_today]

        #Add an entry for this day, using specific datetime as key
        existing_entry[todays_date] = ps

        #Update dated_scores
        dated_scores[string_today] = existing_entry

    else:

        #Create a new entry dictionary for this general date
        new_entry = dict()

        #Add an entry for this specific datetime
        new_entry[todays_date] = ps

        #Update dated scores
        dated_scores[string_today] = new_entry

    #dated_scores[todays_date] = ps
    with open('dated_scores.pkl', 'wb') as fp:
        pickle.dump(dated_scores, fp)



#journal_entry("test.txt")

#def open_journal_entry(date):
     #"""Open a journal entry by date
     #   and print the content.
     #"""
def see_dated_scores():
    """Open the pickled dictonary and print
       all the content.
    """

    if os.path.isfile("dated_scores.pkl"):
        dated_scores_file = open('dated_scores.pkl', 'rb')    
        dated_scores = pickle.load(dated_scores_file)
        print(dated_scores)

#see_dated_scores()
