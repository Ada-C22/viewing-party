# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    
    movie_dict = {
        "title": title,
        "genre": genre,
        "rating": rating,
    }
    
    # movie_dict["title"] = title
    # movie_dict["genre"] = genre
    # movie_dict["rating"] = rating

    return movie_dict

def add_to_watched(user_data, movie):
    if not movie:
        return user_data
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(data, movie):
    pass

def watch_movie(data, title):
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

