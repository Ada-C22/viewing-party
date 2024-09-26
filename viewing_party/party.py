from copy import deepcopy 
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
    for movie in user_data["watchlist"]:
        if title in movie["title"]: 
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
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
    if len(user_data["watched"]) == 0:
        return None
    most_watched_list = []
    max_count = 0
    max_genre = 0
    for movie in user_data["watched"]:
        #for genre in movie["genre"]:
        most_watched_list.append(movie["genre"])
    for genre in set(most_watched_list):
        if most_watched_list.count(genre) > max_count:
            max_count = most_watched_list.count(genre)
            max_genre = genre

    return max_genre    



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# No.1-M
def get_unique_watched(user_data):
    pass
# No.2-A
def get_friends_unique_watched(user_data):
    user_data_copy = deepcopy(user_data)
    unique_watched = []
    user_watched_list = []
    #unique_list = []
    user_watched_unique = []
    for movie in user_data_copy["watched"]:
        user_watched_list.append(movie["title"])
    for friend in user_data_copy["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in user_watched_list:
                unique_watched.append(movie)
                #unique_list.append(movie["title"])
    #unique_list_set = set(unique_list)
    #print(unique_list_set) 
    unique_list_set = set()           

    for movie in unique_watched:
        if movie["title"] not in unique_list_set:
            user_watched_unique.append(movie)
            unique_list_set.add(movie["title"])
    #print(user_watched_unique)                   
            
    return user_watched_unique
    pr        



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
