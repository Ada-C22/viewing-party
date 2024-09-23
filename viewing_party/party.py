# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    movie = {
    "title": title,
        "genre": genre,
        "rating": rating
    }
    if movie["title"] and movie["genre"] and movie["rating"]:
        return movie
    else: return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    print(len(user_data["watched"]))
    return user_data
    

def add_to_watchlist(user_data,title):
    pass
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

