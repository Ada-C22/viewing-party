# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        return {
            "title": title,
            "genre": genre,
            "rating": rating
        }
    else: 
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data,  movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        if title == user_data["watchlist"][i]["title"]:
            user_data["watched"].append(user_data["watchlist"][i])
            user_data["watchlist"].remove(user_data["watchlist"][i])
    return user_data
        

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    # use the .get() method to get the watched list from user_data
    # check to see if the list is empty then return 0.0
    # initialize the total rating and count all movies in the dict
    # loop through each movies in watched_movies to get the ratings
    # add each rating to total_rating
    # calculate the average rating by dividing the total rating by the movie counts
    # return the average rating 

    watched_movies = user_data.get("watched", [])

    if not watched_movies:
        return 0.0
    
    total_rating = 0.0
    all_movies = len(watched_movies)

    for movie in watched_movies:
        total_rating += movie["rating"]

    avg_rating = total_rating / all_movies

    return avg_rating

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

