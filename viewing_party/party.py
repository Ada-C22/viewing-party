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

    genre_frequencies= 0
    max_value =0
    most_watched = {}
    if len((user_data["watched"])) > 0:
        for i in range(len((user_data["watched"]))-1):

            if user_data["watched"][i]["genre"] in most_watched:
                genre_frequencies += 1
                most_watched[user_data["watched"][i]["genre"]] = genre_frequencies
            else:
                most_watched[user_data["watched"][i]["genre"]] = 1

        for key, current_value in most_watched.items():
            if current_value > max_value:
                max_value = current_value
                most_watched_genre = key

        return most_watched_genre
    return None


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

