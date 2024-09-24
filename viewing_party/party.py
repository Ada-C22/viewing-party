# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    
    return {"title" : title,
            "genre" : genre,
            "rating" : rating}

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    movies = user_data["watchlist"]

    for movie in movies:
        if title == movie["title"]:
            movies.remove(movie)
            return add_to_watched(user_data, movie)

    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    total_rating = 0
    movies = user_data["watched"]

    if not movies:
        return total_rating

    for movie in movies:
        total_rating += movie["rating"]

    return total_rating / len(movies)

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    
    genre_count = {}
    for movie in user_data["watched"]:
        if movie["genre"] not in genre_count:
            genre_count[movie["genre"]] = 1
        else:
            genre_count[movie["genre"]] +=1

    max_num = 0
    most_watched_genre = None
    for genre in genre_count:
        if genre_count[genre] > max_num:
            max_num = genre_count[genre]
            most_watched_genre = genre
    
    return most_watched_genre
        
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
