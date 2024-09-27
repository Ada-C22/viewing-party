import copy 
# ------------- WAVE 1 --------------------
# No.1
def create_movie(title, genre, rating):
    movie = {"title": title, "genre": genre, "rating": rating}

    if movie["title"] and movie["genre"] and movie["rating"]:
        return movie
    else:
        return None 
# No.2
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    print(len(user_data["watched"]))
    return user_data
    
# No.3
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data
# No.4 -A
def watch_movie(user_data,title):
    print(user_data, title)
    #user_data["watchlist"] = add_to_watchlist(user_data)
    #ser_data["watched"] = add_to_watched(user_data)
    for movie in user_data["watchlist"]:
        for value in movie.values():
            if title in value: 
                user_data["watchlist"].remove(movie)
                user_data["watched"].append(movie)
                return user_data
            else:
                return user_data
    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
# No.1-M
def get_watched_avg_rating(user_data):
    avg_rating = 0
    ratings = 0
    for movies in user_data.values():
        for movie in movies:
            rating = movie["rating"]
            ratings += rating
            avg_rating = ratings/ len(movies)
    return avg_rating


# No.2-A
def get_most_watched_genre(user_data):
    pass



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# No.1-M
def get_unique_watched(user_data):
    my_data = user_data["watched"].copy()
    friends_data = user_data["friends"]
    for watched in friends_data:
        their_watched = watched["watched"]
        for their_movie in their_watched:
            for i in range(0, len(my_data)):
                if their_movie["title"] == my_data[i]["title"]:
                    del my_data[i]
                    break
    return my_data

# No.2-A
def get_friends_unique_watched(user_data):
    pass

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
# No.1-M
def get_available_recs(user_data):
    pass

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
# No.1-A
def get_new_rec_by_genre(user_data):
    pass

# No.2-M
def get_rec_from_favorites(user_data):
    pass
