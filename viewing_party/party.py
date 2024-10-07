# ------------- WAVE 1 --------------------


def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None 
    movie_dict = {}
    movie_dict["title"] = title
    movie_dict["genre"] = genre
    movie_dict["rating"] = rating
    return movie_dict

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie) 
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if title in movie.values():
            user_data["watchlist"].remove(movie)
            add_to_watched(user_data, movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0.0
    
    average_rating = 0
    movie_list_count = len(user_data["watched"])

    for movie in user_data["watched"]:
        average_rating += movie["rating"]
    average_rating_total = average_rating / movie_list_count 

    return average_rating_total

def get_most_watched_genre(user_data):
    
    genre = {}

    for movie in user_data["watched"]:
        movie_genre = movie.get("genre")
        if movie_genre not in genre:
            genre[movie_genre] = 1 
        else:
            genre[movie_genre] += 1 
    
    genre_count = 0
    most_watched_genre = None
    for genre, count in genre.items():
        if count > genre_count:
            genre_count = count
            most_watched_genre = genre
    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_all_friends_movies(user_data):
    all_friends_movies = []  

    for friend in user_data["friends"]:   
        friend_movie_list = friend["watched"]   
        for movie in friend_movie_list:
            if not all_friends_movies.count(movie):
                all_friends_movies.append(movie)
    return all_friends_movies

def get_unique_watched(user_data): 
    all_friends_movies = get_all_friends_movies(user_data)
    unique_watched = [
        movie
        for movie in user_data["watched"] 
        if not all_friends_movies.count(movie)
        ]
    return unique_watched

def get_friends_unique_watched(user_data):
    unique_friend_watched = get_all_friends_movies(user_data)

    for movie in user_data["watched"]:
        if unique_friend_watched.count(movie):
            unique_friend_watched.remove(movie)
    return unique_friend_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    unique_friend_movies = get_friends_unique_watched(user_data)
    recommended_movie_list = [ 
        movie 
        for movie in unique_friend_movies 
        if movie["host"] in user_data["subscriptions"]
        ]
    return recommended_movie_list

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    favorite_genre = get_most_watched_genre(user_data)
    friends_movies = get_friends_unique_watched(user_data)
    recommended_genre_movies = [
        movie
        for movie in friends_movies
        if movie["genre"] == favorite_genre
        ]
    return recommended_genre_movies

def get_rec_from_favorites(user_data):
    fav_movies = get_unique_watched(user_data)
    fav_movies_rec = [
        movie
        for movie in fav_movies 
        if movie in user_data["favorites"]
        ]
    return fav_movies_rec



