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

def get_unique_watched(user_data):
    user_unique_movie_list = [] 
    friends_watched_titles = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_titles.append(movie["title"])

    for movie in user_data["watched"]:
        if movie["title"] not in friends_watched_titles:
            user_unique_movie_list.append(movie) 

    return user_unique_movie_list


def get_friends_unique_watched(user_data):
    friends_unique_movies = []
    user_watched_titles = []

    for movie in user_data["watched"]:
        user_watched_titles.append(movie["title"])

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in user_watched_titles and movie not in friends_unique_movies:
                friends_unique_movies.append(movie)

    return friends_unique_movies
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommended_movies_list = []
    user_watched_titles = []

    for movie in user_data["watched"]:
        user_watched_titles.append(movie["title"])

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in user_watched_titles and movie["host"] in user_data["subscriptions"]:
                if movie not in recommended_movies_list:
                    recommended_movies_list.append(movie)

    return recommended_movies_list

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

