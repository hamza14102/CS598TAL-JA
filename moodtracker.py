import datetime
import os
import pickle

from enum import Enum

class Mood(Enum):

	ANGRY = ['angry', 'mad']
	BORED = ['bored']
	CONFIDENT = ['confident']
	DAZED = ['dazed', 'dizzy', 'sleepy', 'tired']
	EMBARRASSED = ['embarrassed']
	ENERGIZED = ['energized', 'energetic']
	FINE = ['fine', 'ok', 'okay']
	FLIRTY = ['flirty', 'romantic']
	FOCUSED = ['focused']
	HAPPY = ['happy', 'joyful']
	INSPIRED = ['inspired', 'creative']
	PLAYFUL = ['playful']
	SAD = ['sad']
	SCARED = ['scared']
	TENSE = ['tense']
	UNCOMFORTABLE = ['uncomfortable']



def log_mood(mood):
	"""Intended to take a mood (enum) as input
	   and log it in a tracker.
	"""

	#todays_date represents exact datetime, in case of multiple entries per day
    todays_date = datetime.datetime.now()
    

    #string_today represents the general month day, year
    #This should make it easier to search for entries by date
    string_today = todays_date.strftime("%B %d, %Y")
    

    if os.path.isfile("mood_tracker.pkl"):
        mood_tracker_file = open('mood_tracker.pkl', 'rb')    
        mood_tracker = pickle.load(mood_tracker_file)

    else:

        mood_tracker = dict()
        with open('mood_tracker.pkl', 'wb') as fp:
            pickle.dump(mood_tracker, fp)

    #Should probably check if it is valid member of mood class?
    if isinstance(mood, Enum):
        continue
    else:
        print("error")
        return

    #Check if there is already an entry for the given date
    if string_today in mood_tracker:

        #If there is, access the existing dictionary for this day
        existing_entry = mood_tracker[string_today]

        #Add an entry for this day, using specific datetime as key
        existing_entry[todays_date] = mood

        #Update mood_tracker
        mood_tracker[string_today] = existing_entry

    else:

        #Create a new entry dictionary for this general date
        new_entry = dict()

        #Add an entry for this specific datetime
        new_entry[todays_date] = mood

        #Update dated scores
        mood_tracker[string_today] = new_entry

    #dated_scores[todays_date] = ps
    with open('mood_tracker.pkl', 'wb') as fp:
        pickle.dump(mood_tracker, fp)



def see_dated_mood():
    """Open the pickled dictonary and print
       all the content.
    """

    if os.path.isfile("mood_tracker.pkl"):
        mood_tracker_file = open('mood_tracker.pkl', 'rb')    
        mood_tracker = pickle.load(mood_tracker_file)
        print(mood_tracker)



def playlist_creation(playlist_name):
    """Initialize an empty playlist with the given name.
    """
    
    #Check if the pickled dictionary already exists
    if os.path.isfile("playlists.pkl"):
        playlists_file = open('playlists.pkl', 'rb')    
        playlists = pickle.load(playlists_file)

    else:

        playlists = dict()
        with open('playlists.pkl', 'wb') as fp:
            pickle.dump(playlists, fp)

    #Check if the mood already exists
    if playlist_name in playlists:
        return
    else:
        playlists[playlist_name] = []
        with open('playlists.pkl', 'wb') as fp:
            pickle.dump(playlists, fp)



def add_track(track, playlist_name):
    """Adds a track to the specified playlist.
    """

    playlists_file = open('playlists.pkl', 'rb')    
    playlists = pickle.load(playlists_file)

    #Check if the mood already exists
    if playlist_name in playlists:
        continue
    else:
        playlists[playlist_name] = []

    playlist = playlists[playlist_name]
    playlist.append(track)
    playlists[playlist_name] = playlist

    with open('playlists.pkl', 'wb') as fp:
        pickle.dump(playlists, fp)

def see_playlists():
    """See the current saved playlists.
    """

    playlists_file = open('playlists.pkl', 'rb')    
    playlists = pickle.load(playlists_file)
    print(playlists)

def print_tracklist(playlist_name):
    """See the tracks in a playlist.
    """
    playlists_file = open('playlists.pkl', 'rb')    
    playlists = pickle.load(playlists_file)

    if playlist_name in playlists:
        print(playlists[playlist_name])
    else:
        print("Playlist does not exist.")
        
#def remove_track(playlist, track):
#def remove_playlist(playlist):
