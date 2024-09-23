#
##------------- WAVE 1 --------------------
def create_movie(movie_title, genre, rating):
    movie= {}

    if movie_title and genre and rating:
        
        if isinstance(movie_title,str) or isinstance(genre,str)\
        or rating.isinstance(rating (int,float)):
            
            movie["title"] = movie_title
            movie["genre"] = genre
            movie["rating"] = rating          
                
        return movie
    
    return None

# ALEIDA V changes:
def add_to_watched(user_data, movie):
    # user_data is a DICT, ONE KEY: "watched": [list of dicts]
    # movie, is a single DICT with "title", "genre", "rating" keys
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    # user_data is a DICT with key "watchlist": 
    #[movies user WANTS to watch]
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    #pass
    # user_data = dict with
    # "watchlist" and "watched" keys
    # title is a str

    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            
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

