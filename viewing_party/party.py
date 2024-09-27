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
    user_data_copy = copy.deepcopy(user_data)
    unique_watched = []
    user_watched_list = []
    user_watched_unique = []
    for movie in user_data_copy["watched"]:
        user_watched_list.append(movie["title"])
    for friend in user_data_copy["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in user_watched_list:
                unique_watched.append(movie)

    unique_list_set = set()           

    for movie in unique_watched:
        if movie["title"] not in unique_list_set:
            user_watched_unique.append(movie)
            unique_list_set.add(movie["title"])                   
            
    return user_watched_unique 



# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
# No.1-M
def get_available_recs(user_data):
    my_data = user_data["watched"]
    my_data_titles = []
    for movie in my_data:
        my_data_titles.append(movie["title"])
    the_movies = []
    added_movies = []

    friends_data = user_data["friends"]
    subscriptions = user_data["subscriptions"]

    for watched in friends_data:
        their_watched = watched["watched"]
        for their_movie in their_watched:
            if their_movie["host"] not in subscriptions:
                continue
            if their_movie["title"] not in my_data_titles and their_movie["title"] not in added_movies:
                the_movies.append(their_movie)
                added_movies.append(their_movie["title"])
    return the_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
# No.1-A
def get_new_rec_by_genre(user_data):
    fav_genre = get_most_watched_genre(user_data)
    recommend = get_friends_unique_watched(user_data)
    recommend_watch = []
    if fav_genre is None:
        recommend_watch = []
    else:
        for movie in recommend:
            if fav_genre in movie["genre"]:
                recommend_watch.append(movie)
    return recommend_watch         

# No.2-M
def get_rec_from_favorites(user_data):
    my_data = user_data["favorites"].copy()

    friends_data = user_data["friends"]
    for watched in friends_data:
        their_watched = watched["watched"]
        for their_movie in their_watched:
            for i in range(0, len(my_data)):
                if their_movie["title"] != my_data[i]["title"]:
                    del my_data[i]
                    break 
    return my_data

def get_rec_from_favorites(user_data):
    my_data = {}
    for movie in user_data["favorites"]:
        my_data[movie["title"]] = movie

    friends_data = user_data["friends"]
    for watched in friends_data:
        their_watched = watched["watched"]
        for their_movie in their_watched:
            title = their_movie["title"]
            my_data.pop(title, None)
    return my_data.values()