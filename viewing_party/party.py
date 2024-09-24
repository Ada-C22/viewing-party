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


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

