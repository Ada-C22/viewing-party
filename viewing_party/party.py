# ------------- WAVE 1 --------------------
from tests.test_constants import *


def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None 
    movie = {
        "title": MOVIE_TITLE_1,
        "genre": GENRE_1,
        "rating": RATING_1 ,
    }
    return movie 

def add_to_watched(user_data, movie):
    user_watched = user_data["watched"]
    user_watched.append(movie) 
    user_data["watched"] = user_watched
    return user_data

def add_to_watchlist(user_data, movie):
    user_watched = user_data["watchlist"]
    user_watched.append(movie)
    user_data["watchlist"] = user_watched
    return user_data

def watch_movie(user_data, title):
    user_watchlist = user_data["watchlist"]
    user_watched = user_data["watched"]

    for i in range(len(user_watchlist)):
        if user_watchlist[i]["title"] == title:
            user_watched.append(user_watchlist[i])
            user_data["watchlist"].remove(user_watchlist[i])
            user_data["watched"] = user_watched
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    user_watched = user_data["watched"]

    if len(user_watched) == 0:
        return 0.0 
    
    average_rating = 0
    movie_list_count = 0

    for movie in user_watched:
            average_rating += movie["rating"]
            movie_list_count += 1 
            average_rating_total = average_rating / movie_list_count 

    return average_rating_total

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None 
    
    genre = {}
    user_watched = user_data["watched"]

    for movie in user_watched:
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

def get_all_friends_movies(user_data):
    all_friends_movies = []
    friends_watched = user_data["friends"]   

    for friend in friends_watched:   
        friend_movie_list = friend["watched"]   
        for friend_movie in friend_movie_list:
            if friend_movie not in all_friends_movies:
                all_friends_movies.append(friend_movie)
    return all_friends_movies

def get_unique_watched(user_data):
    unique_watched = []
    all_friends_movies = get_all_friends_movies(user_data)

    for movie in user_data["watched"]:
        if movie not in all_friends_movies:
            unique_watched.append(movie)
    return unique_watched

def get_friends_unique_watched(user_data):
    unique_friend_watched = get_all_friends_movies(user_data)

    for movie in user_data["watched"]:
        if movie in unique_friend_watched:
            unique_friend_watched.remove(movie)
    return unique_friend_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommended_movie_list = []
    all_friends_movies = get_all_friends_movies(user_data)

    for movie in all_friends_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movie_list.append(movie)

    for movie in user_data["watched"]:
        if movie in recommended_movie_list:
            recommended_movie_list.remove(movie)
    return recommended_movie_list

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    favorite_genre = get_most_watched_genre(user_data)
    recommended_genre = []
    all_friends_movies = get_all_friends_movies(user_data)

    for movie in all_friends_movies:
        if movie["genre"] == favorite_genre:
            recommended_genre.append(movie)

    for movie in user_data["watched"]:
        if movie in recommended_genre:
            recommended_genre.remove(movie)
    return recommended_genre

def get_rec_from_favorites(user_data):
    recommended_movies = []
    all_friends_movies = get_all_friends_movies(user_data)

    for movie in user_data["favorites"]:
        if movie not in all_friends_movies:
            recommended_movies.append(movie)
    return recommended_movies



