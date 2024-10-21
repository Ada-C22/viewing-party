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
def get_unique_watched(user_data):
    user_movies = []
    for movie in user_data["watched"]:
        if movie not in user_movies:
            user_movies.append(movie)

    #print(user_movies)

    friend_movies = []
    

    for items in user_data["friends"]:
        for movie in items["watched"]:
            if movie not in friend_movies:
                friend_movies.append(movie)

    #print (friend_movies)
    
    
    unique_movies = []
    for movie in user_movies:
        if movie not in friend_movies:
            unique_movies.append(movie)
    
    
    
    return unique_movies

def get_friends_unique_watched(user_data):

    user_movies = []
    for movie in user_data["watched"]:
        if movie not in user_movies:
            user_movies.append(movie)

    friend_movies = []
    for items in user_data["friends"]:
        for movie in items["watched"]:
            if movie not in friend_movies:
                friend_movies.append(movie)

    friends_unique_movies = []

    for movies in friend_movies:
        if movies not in user_movies:
            friends_unique_movies.append(movies)

    return friends_unique_movies


   
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):

    recomanded_movies = []
    friend_movies = []
    for items in user_data["friends"]:
        for movie in items["watched"]:
            friend_movies.append(movie)


    for movie in friend_movies:
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

    user_genre = []
    for movies in user_data["watched"]:
            user_genre.append(movies["genre"])
   
    genre_dict = {}
    for genre in user_genre:
        if genre in genre_dict:
            genre_dict[genre] += 1
        else:
            genre_dict[genre] = 1 
    
    max_value = 0
    max_key = None

    for key, value in genre_dict.items():
        if value > max_value:
            max_value = value
            max_key = key
    
    most_genre = max_key
    

    friends_movies = []
    for items in user_data["friends"]:
        for movies in items["watched"]:
            friends_movies.append(movies)
    
    
    for movie in friends_movies:
        if movie not in user_data["watched"] and movie["genre"]  in most_genre and movie not in recomanded_movie :
            recomanded_movie.append(movie)
    return recomanded_movie