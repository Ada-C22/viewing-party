# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating: 
        return None
    new_movie = {
            "title": title,
            "genre": genre,
            "rating": rating
            }        
    return new_movie

def add_to_watched(user_data, movie): 
    user_data["watched"].append(movie)

    # for data in user_data.keys(): 
    #     user_data[data].append(movie)

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

