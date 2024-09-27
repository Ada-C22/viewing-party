# ------------- WAVE 1 --------------------
# create dictionary with following key value pairs. 
def create_movie(title, genre, rating):
    if title is None: 
        return None
    elif genre is None: 
        return None
    elif rating is None: 
        return None
    movie_dictionary= {"title": title, "genre": genre, "rating": rating }
    return movie_dictionary


def add_to_watched(user_data,movie):
    watched_list=user_data["watched"]
    watched_list.append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    watch_list=user_data["watchlist"]
    watch_list.append(movie)
    return user_data
    pass

def watch_movie(user_data, movie):
    watch_list = user_data["watchlist"]
    print("watch list :", user_data["watchlist"])
    print("watched list :", user_data["watched"])
    watched_list = user_data["watched"]

    for to_watch_movie in watch_list: 
        movie_name = to_watch_movie["title"]
        if movie_name == movie:
            watch_list.remove(to_watch_movie)
            watched_list.append(to_watch_movie)
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

