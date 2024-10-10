# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movies = {}

    movies ["title"] = title
    movies["genre"] = genre
    movies["rating"] = rating
    
    for movie in movies.values():
        if movie == None:
            return None
        
    return movies 

def add_to_watched(user_data, movie):
    user_data["watched"] = movie
    return user_data

def add_to_watchlist(user_data,movie):
    user_data["watchedlist"] = movie
    return user_data
def watch_movie(user_data, title):
    if title in user_data["watchlist"]:
        user_data["watchlist"].remove(title)
        user_data["watched"].append(title)
        return user_data
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum_rating = 0
    no_movies = 0
    for value in user_data.values():
        for movies in value:
            sum_rating += movies["rating"]
            
    for value in user_data.values():
        for movies in value:
            no_movies += 1

    avg_rating = sum_rating/no_movies

    
    

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

