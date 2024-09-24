from copy import deepcopy 
# ------------- WAVE 1 --------------------
# No.1
def create_movie(title, genre, rating):
    movie = {"title": title, "genre": genre, "rating": rating}

    if movie["title"] and movie["genre"] and movie["rating"]:
        return movie
    else:
        return None 
# No.2
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    print(len(user_data["watched"]))
    return user_data
    
# No.3
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data
# No.4 -A
def watch_movie(user_data,title):
    pass

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
# No.1-M
def get_watched_avg_rating(user_data):
    avg_rating = 0
    ratings = 0
    for movies in user_data.values():
        for movie in movies:
            rating = movie["rating"]
            ratings += rating
            avg_rating = ratings/ len(movies)
    return avg_rating


# No.2-A
def get_most_watched_genre(user_data):
    pass



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# No.1-M
def get_unique_watched(user_data):
    pass
# No.2-A
def get_friends_unique_watched(user_data):
    pass
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
# No.1-M
def get_available_recs(user_data):
    pass

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
# No.1-A
def get_new_rec_by_genre(user_data):
    pass

# No.2-M
def get_rec_from_favorites(user_data):
    pass
