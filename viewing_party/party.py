# -----------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------
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

    #Crate a copy of user data to avoid modifying original LM
    updated_user_data = {
            "watched": user_data["watched"][:]}

    updated_user_data["watched"].append(movie)
    return updated_user_data


def add_to_watchlist(user_data, movie):
    # user_data is a DICT with key "watchlist": 
    #[movies user WANTS to watch]

    #Crate a copy of user data to avoid modifying original LM
    updated_user_data = {
            "watchlist": user_data["watchlist"][:],
        } 
    updated_user_data["watchlist"].append(movie)
    return updated_user_data


def watch_movie(user_data, title):
    # user_data = dict with
    # "watchlist" and "watched" keys
    # title is a str

    #Crate a copy of user data to avoid modifying original LM
    updated_user_data = {
            "watchlist": user_data["watchlist"][:],
            "watched": user_data["watched"][:]
        } 

    for movie in updated_user_data["watchlist"]:
        if movie["title"] == title:
            updated_user_data["watchlist"].remove(movie)
            updated_user_data["watched"].append(movie)         
    return updated_user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    #User data is a dict wich contain "watched" key
    count = 0.0
    sum = 0.0

    if len(user_data["watched"]) == 0:
        return sum
    for movie in user_data["watched"]:
        if movie["rating"]:
            count += 1
            sum += movie["rating"]
        else:
            sum = 0

    return sum/count


def get_most_watched_genre(user_data):
    pass



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    #ONLY THE USER HAS WATCHED, BUT THE FRIENDS HAVE NOT
    user_unique_watched = []
    friends_watched = []

    for friend in user_data["friends"]:
        for movie in friend['watched']:
            friends_watched.append(movie)
    
    for movie in user_data["watched"]:
        if movie not in friends_watched:
            user_unique_watched.append(movie)

    return user_unique_watched


def get_friends_unique_watched(user_data):
    #AT LEAST ONE OF THE FRIENDS HAS WATCHED,
    # BUT THE USER HAS NOT

    user_watched = []
    friends_unique_watched = []
    

    for movie in user_data["watched"]:
        user_watched.append(movie)

    for friend in user_data["friends"]:
        for movie in friend['watched']:
            if movie not in user_watched\
                and movie not in friends_unique_watched:
                friends_unique_watched.append(movie)

    return friends_unique_watched
    

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    
    rec_list = []

    friends_uniques = get_friends_unique_watched(user_data)

    for movie in friends_uniques:
        if movie["host"] in user_data["subscriptions"]:
            rec_list.append(movie)
            
    return rec_list

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    
    # Call function from ...
    freq_genre = get_most_watched_genre(user_data)
    friends_unique_movies = get_friends_unique_watched(user_data)
    

    rec_list = []
    
    if len(friends_unique_movies) >0 :

        for movie in friends_unique_movies:
            if freq_genre in movie.values():
                rec_list.append(movie)

    return rec_list
    

def get_rec_from_favorites(user_data):

    user_only_movies = get_unique_watched(user_data)

    rec_list = []
    
    for movie in user_only_movies:
        if movie in user_data["favorites"]:
            rec_list.append(movie)
            
    return rec_list