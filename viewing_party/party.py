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
    frecuency_data = []
    if user_data["watched"]:
        for movie in user_data["watched"]:
            if "genre":
                if movie["genre"] not in genres:
                    genres[movie["genre"]] = 1
                else:
                    genres[movie["genre"]] += 1
        for genre, frecuency in genres.items():
            frecuency_data.append(frecuency)
        for genre, frecuency in genres.items():
            if frecuency == max(frecuency_data):
                return genre 
        
        
    return None

# user_data = {   'watched': [   {   'genre': 'Fantasy',
#                     'rating': 4.8,
#                     'title': 'The Lord of the Functions: The Fellowship of '
#                                 'the Function'},
#                 {   'genre': 'Fantasy',
#                     'rating': 4.0,
#                     'title': 'The Lord of the Functions: The Two '
#                                 'Parameters'},
#                 {   'genre': 'Fantasy',
#                     'rating': 4.0,
#                     'title': 'The Lord of the Functions: The Return of the '
#                                 'Value'},
#                 {   'genre': 'Action',
#                     'rating': 2.2,
#                     'title': 'The JavaScript and the React'},
#                 {'genre': 'Intrigue', 'rating': 2.0, 'title': 'Recursion'},
#                 {   'genre': 'Intrigue',
#                     'rating': 4.5,
#                     'title': 'Instructor Student TA Manager'}]}

# get_watched_avg_rating(user_data)


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# ----------------------------------------