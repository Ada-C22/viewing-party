# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    pass

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def watch_movie(user_data, title):
    movies = user_data["watchlist"]

    for movie in movies:
        if title == movie["title"]:
            movies.remove(movie)
            return add_to_watched(user_data, movie)

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

