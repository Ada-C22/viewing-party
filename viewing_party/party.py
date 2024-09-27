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
    if not user_data["watched"]:
        return 0.0
    
    total_rating = 0
    for movie in user_data["watched"]:
        total_rating += movie["rating"]
    return total_rating / len(user_data["watched"])

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    
    genre_count = {}
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in genre_count:
            genre_count[genre] += 1
        else:
            genre_count[genre] = 1
            
    max_count = 0
    most_watched_genre = None
    for genre, count in genre_count.items():
        if count > max_count:
            max_count = count
            most_watched_genre = genre
    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    friends_watched_movie_titles = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_movie_titles.add(movie["title"])
            
    user_unique_watched = []
    for movie in user_data["watched"]:
        if movie["title"] not in friends_watched_movie_titles:
            user_unique_watched.append(movie)
    return user_unique_watched

def get_friends_unique_watched(user_data):
    user_unique_watched = set()
    for movie in user_data["watched"]:
        user_unique_watched.add(movie["title"])
        
    friends_unique_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if (movie["title"] not in user_unique_watched and
                movie not in friends_unique_movies):
                friends_unique_movies.append(movie)
    return friends_unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    friends_unique_movies = get_friends_unique_watched(user_data)
    recommended_movies = []
    
    for movie in friends_unique_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)
    friends_unique_movies = get_friends_unique_watched(user_data)
    recommended_movies = []
    
    for movie in friends_unique_movies:
        if movie["genre"] == most_watched_genre:
            recommended_movies.append(movie)
    return recommended_movies

def get_rec_from_favorites(user_data):
    # We made the assumption that the favorites are in "user_unique_watched"
    user_unique_watched = get_unique_watched(user_data)
    recommended_movies = []
    
    for movie in user_data["favorites"]:
        if movie in user_unique_watched:
            recommended_movies.append(movie)
    return recommended_movies
