# ------------- WAVE 1 --------------------
user_data = {
    "watched": [],
    "watchlist": []
}
def create_movie(title, genre, rating):
    movie = {}
    if title and genre and rating:
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie
    else:
        return None
    
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    
    movies = user_data.copy()

    movies["watchlist"] = movies["watchlist"].copy()
    movies["watched"] = movies["watched"].copy()

    for movie in movies["watchlist"]:
        if title in movie["title"]:
            watchlist_movie = movie
            movies["watchlist"].remove(watchlist_movie)
            movies["watched"].append(watchlist_movie)
    
    return movies


# ------------- WAVE 2 --------------------
def get_watched_avg_rating(user_data):
    ratings = 0
    movie_counter = 0
    avg_rating = 0
    
    if user_data["watched"]:
        for movie in user_data["watched"]:
            if "rating":
                ratings += movie["rating"]
                movie_counter += 1
            else:
                movie_counter += 1
        return ratings/movie_counter
    return 0.0

def get_most_watched_genre(user_data):
    genres = {}

    if user_data["watched"]:
        for movie in user_data["watched"]:
            genre = movie["genre"]
            if genre not in genres:
                genres[genre] = 1
            else:
                genres[genre] += 1
        
        max_frequency = max(genres.values())
        
        for genre, frequency in genres.items():
            if frequency == max_frequency:
                return genre

    return None


# ------------- WAVE 3 --------------------

def get_unique_watched(user_data):
    friends_movies = set()

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movies.add(movie["title"])
    movies_unwatched = []
    for movie in user_data["watched"]:
        if movie["title"] not in friends_movies:
            movies_unwatched.append(movie)
    return movies_unwatched

def get_friends_unique_watched(user_data):
    friends_movies = set()
    
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movies.add(movie["title"])
    
    user_watched = {movie["title"] for movie in user_data["watched"]}
    
    friends_unwatched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in user_watched and movie not in friends_unwatched:
                friends_unwatched.append(movie)
    
    return friends_unwatched
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# ----------------------------------------