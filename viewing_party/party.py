# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {}

    if title == None or title == "" or genre == None or genre == "" or rating == None or rating == "":
        return None

    movie["title"] = title
    movie["genre"] = genre
    movie["rating"] = rating

    return movie

def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):

    watchlist = user_data["watchlist"]

    for movie in watchlist:
        if movie["title"] == title:
            watchlist.remove(movie)
            user_data["watched"].append(movie)
            return user_data
    
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):

    if len(user_data["watched"]) == 0:
        return 0.0
    
    sum = 0

    for movie in user_data["watched"]:
        sum += movie["rating"]
    
    return sum / len(user_data["watched"])


def get_most_watched_genre(user_data):

    if len(user_data["watched"]) == 0:
        return None

    genres_count = {}

    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in genres_count:
            genres_count[genre] += 1
        else:
            genres_count[genre] = 1
    
    max_count = 0
    most_frequently_watched_genre = ""

    for genre in genres_count.keys():
        if genres_count[genre] > max_count:
            max_count = genres_count[genre]
            most_frequently_watched_genre = genre
    
    return most_frequently_watched_genre








# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

