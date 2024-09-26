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
def get_watched_avg_rating(user_data):
    watched_movie = user_data["watched"]

    if len(watched_movie) == 0:
        return 0.0 
    
    average_rating = 0
    movie_list_count = 0

    for movie in watched_movie:
        if "rating" in movie:
            average_rating += movie["rating"]
            movie_list_count += 1 
            average_rating_total = average_rating / movie_list_count 

    return average_rating_total

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None 
    
    genre = {}
    watched_movie = user_data["watched"]

    for movie in watched_movie:
        movie_genre = movie.get("genre")
        if movie_genre not in genre:
            genre[movie_genre] = 1 
        elif movie_genre in genre:
            genre[movie_genre] += 1 
    
    genre_count = 0
    most_watched_genre = None
    for key, value in genre.items():
        if value > genre_count:
            genre_count = value
            most_watched_genre = key 
    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    unique_watched = []
    collect_friends_movies = []
    user_watched = user_data["watched"]

    friends_watched = user_data["friends"]   # the list of 2 dictionaries in the "friends" key
    for friend in friends_watched:   # the inner "watched dict"
        friend_movie_list = friend["watched"]   # the inner list of dicts
        for friend_movie in friend_movie_list:
            collect_friends_movies.append(friend_movie)

    for movie in user_watched:
        if movie not in collect_friends_movies:
            unique_watched.append(movie)
    return unique_watched

def get_friends_unique_watched(user_data):
    unique_friend_watched = []
    user_watched = user_data["watched"]

    friends_watched = user_data["friends"]   # the list of 2 dictionaries in the "friends" key
    for friend in friends_watched:   # the inner "watched dict"
        friend_movie_list = friend["watched"]   # the inner list of dicts
        for friend_movie in friend_movie_list:
            if friend_movie not in user_watched and friend_movie not in unique_friend_watched:
                unique_friend_watched.append(friend_movie)
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
def get_available_recs(user_data):
    user_watched = user_data["watched"]
    recommended_movie_list = []
    available_movies = []

    friends_watched = user_data["friends"]   # the list of 2 dictionaries in the "friends" key
    for friend in friends_watched:   # the inner "watched dict"
        friend_movie_list = friend["watched"]   # the inner list of dicts
        for friend_movie in friend_movie_list:
            if friend_movie["host"] in user_data["subscriptions"]:
                available_movies.append(friend_movie)

    for movie in available_movies:
        if movie not in user_watched and movie not in recommended_movie_list:
            recommended_movie_list.append(movie)
    return recommended_movie_list

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
USER_DATA_5 = {
    "watched": [
        FANTASY_1b, 
        FANTASY_2b, 
        FANTASY_3b, 
        ACTION_1b, 
        INTRIGUE_1b, 
        INTRIGUE_2b
        ],
    "subscriptions" : [
        "netflix",
          "hulu"
        ], 
    "favorites" : [
        FANTASY_1b, 
        FANTASY_2b, 
        INTRIGUE_1b,
        INTRIGUE_2b
        ], 
    "friends":  [
        {
            "watched": [
                FANTASY_1b,
                FANTASY_3b,
                FANTASY_4b,
                HORROR_1b,
            ]
        },
        {
            "watched": [
                FANTASY_1b,
                FANTASY_4b,
                ACTION_1b,
                INTRIGUE_1b,
                INTRIGUE_3b,
            ]
        }  
    ]
}

USER_DATA_5["friends"][0]["watched"][0]["host"]

USER_DATA_5["subscriptions"]




def get_new_rec_by_genre(user_data):
    favorite_genre = get_most_watched_genre(user_data)
    friend_genre_list = []
    recommended_genre = []


    friends_watched = user_data["friends"]   # the list of 2 dictionaries in the "friends" key
    for friend in friends_watched:   # the inner "watched dict"
        friend_movie_list = friend["watched"]   # the inner list of dicts
        for friend_movie in friend_movie_list:
            if friend_movie["genre"] == favorite_genre:
                friend_genre_list.append(friend_movie)

    for movie in friend_genre_list:
        if movie not in user_data["watched"] and movie not in recommended_genre:
            recommended_genre.append(movie)
    return recommended_genre

def get_rec_from_favorites(user_data):
    recommended_movies = []
    collect_friend_movies = []

    friends_watched = user_data["friends"]   # the list of 2 dictionaries in the "friends" key
    for friend in friends_watched:   # the inner "watched dict"
        friend_movie_list = friend["watched"]   # the inner list of dicts
        for friend_movie in friend_movie_list:
            if friend_movie not in collect_friend_movies:
                collect_friend_movies.append(friend_movie)

    for movie in user_data["favorites"]:
        if movie not in collect_friend_movies:
            recommended_movies.append(movie)
    return recommended_movies



