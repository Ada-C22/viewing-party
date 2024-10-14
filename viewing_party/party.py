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
    for value in user_data.values():
        for movies in value:
            sum_rating += movies["rating"]
            
    for value in user_data.values():
        for movies in value:
            no_movies += 1

    if no_movies == 0:
        avg_rating = 0.0
    else:
        avg_rating = sum_rating/no_movies
    
    return avg_rating

def get_most_watched_genre(user_data):
    genre_list = []
    for value in user_data.values():
        for movies in value:
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
    for movies in user_data["watched"]:
        user_movies.append(movies)
    #print(user_movies)

    friend_movies = []
    for items in user_data["friends"]:
        for movies in items["watched"]:
                friend_movies.append(movies)
    

    #print (friend_movies)
    
    
    unique_movies = []
    for movie in friend_movies:
        if movie not in user_movies:
            unique_movies.append(movie)

        
    #list_dict =  []
    
    print (unique_movies)
    return unique_movies
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

