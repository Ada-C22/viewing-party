# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }

    if title is None or genre is None or rating is None:
        return None
    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    
    return user_data

def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data,title):
    for movies_to_watch in user_data["watchlist"]:
        if title == movies_to_watch["title"]:
            user_data["watched"].append(movies_to_watch)
            user_data["watchlist"].remove(movies_to_watch)
    
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):

    if len(user_data["watched"]) == 0:
        return 0.0
    sum_rating = 0.0
    for movie in user_data["watched"]:
        sum_rating += movie["rating"]   
    avg_rating = float(sum_rating/len(user_data["watched"]))

    return avg_rating

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None
    count_genre = {}
    
    for movie in user_data["watched"]:
        count_genre[movie["genre"]] = count_genre.get(movie["genre"],0) + 1
    
    max_count = 0
    popular_genre = None
    for gerne,count in count_genre.items():
        if count > max_count:
            popular_genre = gerne
            max_count = count
    
    return popular_genre





# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

