# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None 
    movie_dict = {}
    if type(title) == str and type(genre) == str and type(rating) == int or type(rating) == float or int:
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
    rating_sum = 0.0
    movie_count = 0
    for movie in user_data["watched"]:
        movie_count += 1
        rating_sum += movie["rating"]
    if movie_count > 0:
        return (rating_sum/movie_count)
    else:
        return 0.0    

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

# This is another way that we could implement this function without using the max method
#  genres_count = {}
#     if user_data["watched"]:
#         for movie in user_data["watched"]:
#             genre_count = genres_count.setdefault(movie["genre"], 0)
#             if genre_count >= 0:
#                 genre_count += 1
#                 genres_count[movie["genre"]] = genre_count
        
#         pop_genre = None
#         pop_genre_count = 0 

#         for genre, count in genres_count.items():
#             if count > pop_genre_count:
#                 pop_genre = genre
#                 pop_genre_count = count 
        
#         return pop_genre
#     else:
#         return None
    
# ------------- WAVE 3 --------------------

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
   

# ------------- WAVE 4 --------------------

def get_available_recs(user_data):
    friend_unique_movies = get_friends_unique_watched(user_data)
    recommendations = []
    for movies in friend_unique_movies:
        if movies["host"] in user_data["subscriptions"]:
            recommendations.append(movies)
    return recommendations

# ------------- WAVE 5 --------------------

def get_new_rec_by_genre(user_data):
    recs = get_friends_unique_watched(user_data)
    new_rec_by_genre = []
    most_freq_genre = get_most_watched_genre(user_data)
    for movie in recs: 
        if movie["genre"] == most_freq_genre:
            new_rec_by_genre.append(movie)
    return new_rec_by_genre

def get_rec_from_favorites(user_data):
    rec_from_favorites = []
    unique_watched = get_unique_watched(user_data)
    for movie in user_data["favorites"]:
        if movie in unique_watched:
            rec_from_favorites.append(movie)
    return rec_from_favorites

