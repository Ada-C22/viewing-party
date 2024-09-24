# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None 
    movie_dict = {}
    if type(title) == str and type(genre) == str and type(rating) == int or type(rating) == float or int:
        # movie_dict["title"] = title
        # movie_dict["genre"] = genre
        # movie_dict["rating"] = rating
        movie_dict = {
            "title": title,
            "genre": genre,
            "rating": rating
        }

    else:
        return None
    return movie_dict

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data

# ------------- WAVE 2 --------------------


def get_watched_avg_rating(user_data):
    total_ratings = 0
    
    if len(user_data["watched"]) > 0:
        for movie in user_data["watched"]:
            total_ratings += movie["rating"]
            total_movies = len(user_data["watched"])
            average = total_ratings / total_movies
    else: 
        return 0.0
    return average

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None
    
    genre_count = {}
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in genre_count:
            genre_count[genre] += 1
        else:
            genre_count[genre] = 1
    popular_genre = max(genre_count, key=genre_count.get)
    return popular_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):        
    user_unique_movie = []
    friend_watched_movies = []
    for friends in user_data["friends"]:
        for movie in friends["watched"]:
            friend_watched_movies.append(movie["title"])

    for movie in user_data["watched"]:
        if movie["title"] not in friend_watched_movies:
            user_unique_movie.append(movie)
    return user_unique_movie
    
 
def get_friends_unique_watched(user_data):
    friends_unique_movies = []
    user_watched_movies = []
    for movie in user_data["watched"]:
        user_watched_movies.append(movie["title"])
    for friends in user_data["friends"]:
        for movie in friends["watched"]:
            if movie["title"] not in user_watched_movies and movie not in friends_unique_movies:
                friends_unique_movies.append(movie)
    return friends_unique_movies
   
# # -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    friend_unique_movies = get_friends_unique_watched(user_data)
    recommendations = []
    for movies in friend_unique_movies:
        if movies["host"] in user_data["subscriptions"]:
            recommendations.append(movies)
    return recommendations


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    friend_unique_movies = get_friends_unique_watched(user_data)
    recommendations = []
    genre_dict = {}
    if user_data["watched"] == 0:
        return 0
    for movies in user_data["watched"]:
        genre = movies["genre"]
        if genre in genre_dict:
            genre_dict[genre] += 1
        else:
            genre_dict[genre] = 1
    favorite_genre = max(genre_dict, key=genre_dict.get)
    for movies in friend_unique_movies:
        if movies["genre"] == favorite_genre:
            recommendations.append(movies)
    return recommendations

# 1. Create a function named  `get_new_rec_by_genre`. This function should...

# - take one parameter: `user_data`
# - Consider the user's most frequently watched genre. Then, determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The user has not watched it
#   - At least one of the user's friends has watched
#   - The `"genre"` of the movie is the same as the user's most frequent genre
# - Return the list of recommended movies

# 2. Create a function named  `get_rec_from_favorites`. This function should...

# - take one parameter: `user_data`
#   - `user_data` will have a field `"favorites"`. The value of `"favorites"` is a list of movie dictionaries
#     - This represents the user's favorite movies
# - Determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The movie is in the user's `"favorites"`
#   - None of the user's friends have watched it
# - Return the list of recommended movies
