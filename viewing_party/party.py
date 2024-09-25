# ------------- WAVE 1 --------------------
from tests.test_constants import *

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None 
    movie_title = {
        "title": MOVIE_TITLE_1,
        "genre": GENRE_1,
        "rating": RATING_1 ,
    }
    return movie_title

def add_to_watched(user_data, movie):
    user_data_values = user_data["watched"]
    user_data_values.append(movie) 
    user_data["watched"] = user_data_values
    return user_data

def add_to_watchlist(user_data, movie):
    user_data_values = user_data["watchlist"]
    user_data_values.append(movie)
    user_data["watchlist"] = user_data_values
    return user_data

def watch_movie(user_data, title):
    user_watchlist = user_data["watchlist"]
    user_watchedlist = user_data["watched"]

    for i in range(len(user_watchlist)):
        if user_watchlist[i]["title"] == title:
            user_watchedlist.append(user_watchlist[i])
            user_data["watchlist"].remove(user_watchlist[i])
            user_data["watched"] = user_watchedlist
            # add updated watched list to user data
    return user_data






# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


user_data = {
    "watched": [
        FANTASY_1, 
        FANTASY_2, 
        FANTASY_3, 
        ACTION_1, 
        INTRIGUE_1, 
        INTRIGUE_2
        ],
    "friends": [
        {
            "watched": [
                FANTASY_1,
                FANTASY_3,
                FANTASY_4,
                HORROR_1,
            ]
        }]}



def get_unique_watched(user_data):
    unique_watched = []
    collect_friends_movies = []
    user_watched = user_data["watched"]

    friends_watched = user_data["friends"]
    for i in range(len(friends_watched)):
        friends_movies = friends_watched[i]["watched"]
        collect_friends_movies.append[friends_movies]

    for movie in user_watched:
        if movie not in collect_friends_movies:
            unique_watched.append(movie)
    return unique_watched

def get_friends_unique_watched(user_data):
    unique_friend_watched = []
    collect_friends_movies = []
    user_watched = user_data["watched"]

    friends_watched = user_data["friends"]
    for i in range(len(friends_watched)):
        friends_movies = friends_watched[i]["watched"]
        collect_friends_movies.append[friends_movies]

    for movie in collect_friends_movies:
        if movie not in user_watched:
            unique_friend_watched.append(movie)
    return unique_friend_watched

    

# user_data is a dictionary containing 2 key value pair
# the value for watched is a list of dicts
 # the inner dicts have the key values for movie, rating, genre
# the value for friends is a a list of dictionaries
 #  each inner dict has a key "watched" and a list of dicts for values
 # the inner inner have key values for movie, rating, genre


        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

