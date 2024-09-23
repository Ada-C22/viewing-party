# ------------- WAVE 1 --------------------
user_data = {
    "watched": [],
    "watchlist": []
}
def create_movie(title, genre, rating):
    movie = {}
    if title and genre and rating:
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie
    else:
        return None
    
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    
    movies = user_data.copy()
    if title in movies["watchlist"]["title"]:
        movies["watchlist"]["title"].remove(title)
        movies["watched"]["title"].append(title)
        return movies
    else:
        return user_data
        

# create_movie("Title A", "Horror", 3.5)
# movie ="Title A", "Horror", 3.5
# add_to_watched(user_data, movie)
# add_to_watchlist(user_data, movie)
# print (user_data)

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

