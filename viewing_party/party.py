# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or  not genre or not rating:
        return None
    else:
        movies = {}
        movies["title"] = title
        movies["genre"] = genre
        movies["rating"] = rating
        return movies 

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    if title in user_data["watchlist"]:
        user_data["watchlist"].remove(title)
        user_data["watched"].append(title)
        return user_data
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    sum_rating = 0
    no_movies = 0
    
    for movies in user_data["watched"]:
        sum_rating += movies["rating"]
            
    no_movies = len(user_data["watched"])

    if no_movies == 0:
        avg_rating = 0.0
    else:
        avg_rating = sum_rating/no_movies
    
    return avg_rating

def get_most_watched_genre(user_data):
    if not user_data["watched"] :
        return None

    genre_list = []
    for movies in user_data["watched"]:
        genre_list.append(movies["genre"])

    dict = {}
    for item in genre_list:
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1
    
    max_value = 0
    max_key = None

    for key, value in dict.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key
  
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def user_movies_list(user_data):
    user_movies = []
    for movie in user_data["watched"]:
        if movie not in user_movies:
            user_movies.append(movie)
    return user_movies

def friend_movies_list(user_data):
    friend_movies = []
    for items in user_data["friends"]:
        for movie in items["watched"]:
            if movie not in friend_movies:
                friend_movies.append(movie)
    return friend_movies

def get_unique_watched(user_data):
    
    user_movies_collection = user_movies_list(user_data)
    friend_movies_collection = friend_movies_list(user_data)
   
    unique_movies = []
    for movie in user_movies_collection:
        if movie not in friend_movies_collection:
            unique_movies.append(movie)
    return unique_movies

def get_friends_unique_watched(user_data):

    user_movies_collection = user_movies_list(user_data)
    friend_movies_collection = friend_movies_list(user_data)

    friends_unique_movies = []

    for movies in friend_movies_collection:
        if movies not in user_movies_collection:
            friends_unique_movies.append(movies)

    return friends_unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):

    recomanded_movies = []
    friend_movies_collection = friend_movies_list(user_data)

    for movie in friend_movies_collection:
        if movie["host"] in user_data["subscriptions"] and movie not in user_data["watched"] and movie not in recomanded_movies:
            recomanded_movies.append(movie)
    return recomanded_movies         

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):

    recomanded_movie = []
    if  not user_data["watched"]  or not user_data["friends"]:
        return recomanded_movie 

    most_genre = get_most_watched_genre(user_data)
    
    friend_movies_collection = friend_movies_list(user_data)
    
    for movie in friend_movies_collection:
        if movie not in user_data["watched"] and movie["genre"]  in most_genre and movie not in recomanded_movie :
            recomanded_movie.append(movie)
    return recomanded_movie

def get_rec_from_favorites(user_data):

    friend_movies_collection = friend_movies_list(user_data)
    recommanded_movies = []
    favorite_movies = []
    for movie in user_data["favorites"]:
        favorite_movies.append(movie)

        for movies in favorite_movies:
            if movie not in friend_movies_collection and movie not in recommanded_movies:
                recommanded_movies.append(movie)
    #print(favorite_movies)
    #print(friend_movies_collection)
    return recommanded_movies
        