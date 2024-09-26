# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    movie_dict = {
        "title": title,
        "genre": genre,
        "rating": rating,
    }
    
    return movie_dict

def add_to_watched(user_data, movie):
    if not movie:
        return user_data
    user_data["watched"].append(movie)
    
    return user_data

def add_to_watchlist(user_data, movie):
    if not movie:
        return user_data
    user_data["watchlist"].append(movie)
    
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            break
    
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    watched_movies = []
    if "watched" in user_data:
        watched_movies = user_data["watched"]

    if not watched_movies:
        return 0.0
    
    total_rating = 0
    for show in watched_movies:
        total_rating += show["rating"]
    
    return total_rating / len(watched_movies)

def get_most_watched_genre (user_data):
    watched_movies = []
    if "watched" in user_data:
        watched_movies = user_data["watched"]

    if not watched_movies:
        return None

    genre_count = {}
    for movie in watched_movies:
        genre = movie["genre"]
        if genre in genre_count:
            genre_count[genre] += 1
        else:
            genre_count[genre] = 1
    most_watched_genre = None
    max_count = 0
    
    for genre, count in genre_count.items():
        if count > max_count:
            max_count = count
            most_watched_genre = genre
    
    return most_watched_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    user_data_copy = user_data.copy()
    friends_watched_movie_titles = set()

    for friend_dict in user_data_copy["friends"]:
        for movie_dict in friend_dict["watched"]:
            friends_watched_movie_titles.add(movie_dict["title"])

    user_unique_watched = []
    for movie_dict in user_data_copy["watched"]:
        if movie_dict["title"] not in friends_watched_movie_titles:
            user_unique_watched.append(movie_dict)

    return user_unique_watched

def get_friends_unique_watched(user_data):
    user_data_copy = user_data.copy()
    user_unique_watched = set ()

    for movie_dict in user_data_copy["watched"]:
        user_unique_watched.add(movie_dict["title"])

    friends_unique_movies = []
    for friend_dict in user_data_copy["friends"]:
        for movie_dict in friend_dict["watched"]:
            if movie_dict["title"] not in user_unique_watched:
                if movie_dict not in friends_unique_movies:
                    friends_unique_movies.append(movie_dict)
    
    return friends_unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    user_data_copy = user_data.copy()
    user_subscriptions_list = user_data_copy["subscriptions"]
    friends_list = user_data_copy["friends"]
    user_unique_watched_list = user_data_copy["watched"]

    user_unique_movies_set = set()
    friends_unique_movies_dict = dict()
    recommended_movies = list()

    for friend in friends_list:
        friend_watched_list = friend["watched"]
        for movie_dict in friend_watched_list:
            movie_title = movie_dict["title"]
            friends_unique_movies_dict[movie_title] = movie_dict

    for movie_dict in user_unique_watched_list:
        user_unique_movies_set.add(movie_dict["title"])

    for title, movie in friends_unique_movies_dict.items():
        if title not in user_unique_movies_set:
            if movie["host"] in user_subscriptions_list:
                recommended_movies.append(movie)

    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    pass

def get_rec_from_favorites(user_data):
    pass