# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    movie_dict = {}

    movie_dict["title"] = True
    movie_dict["genre"] = True
    movie_dict["rating"] = True

    for key, value in movie_dict.items():
        if not title or not genre or not rating:
            return None
        else:
            movie_dict["title"] = title
            movie_dict["genre"] = genre
            movie_dict["rating"] = rating

    return movie_dict

def add_to_watched(user_data, movie):

    user_data["watched"].append(movie) #if movie is single movie dictionary

    return user_data 
        


def add_to_watchlist(user_data, movie):

    
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):

    # check if watchlist is empty
    if not user_data["watchlist"]:
        return user_data #return user_data if no movies to watch

    # accessing value of user_data which is a list
    for movie in user_data["watchlist"]:
        if movie["title"] == title: # title not in watchlist
            user_data["watchlist"].remove(movie) # removing movie from watchlist
            user_data["watched"].append(movie) # add movie to watched
            break # exit loop after title is removed from watchlist
        
    return user_data


    #  break
    #     else: # title in watchlist

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

