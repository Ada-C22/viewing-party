import copy
# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    new_movie = {
            "title": title,
            "genre": genre,
            "rating": rating
            }
    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)


    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data


def watch_movie(user_data, title):

    watch_list = user_data["watchlist"]
    watched = user_data["watched"]

    for movie in watch_list:
        if movie["title"] == title:
            watched.append(movie)
            watch_list.remove(movie)
            break
    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    if not len(user_data["watched"]):
        return 0.0
    sum = 0
    for movie in user_data["watched"]:
        sum += movie["rating"]

    average = sum / len(user_data["watched"])
    return average

def get_most_watched_genre(user_data):
    if not user_data:
        return None

    genres = {}
    for movie in user_data["watched"]:
        movie_genre = movie["genre"]
        count = genres.get(movie_genre, 0)
        genres[movie_genre] = count + 1

    entry = None
    max_number_of_occurences = 0

    for genre, count in genres.items():
        if count > max_number_of_occurences:
            entry = genre
            max_number_of_occurences = count

    return entry

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    friend_movie = []

    for friend_list in user_data["friends"]:
        for movie in friend_list["watched"]:
            if movie not in friend_movie:
                friend_movie.append(movie)

    unique_user_movie = []

    for movie in user_data["watched"]:
        if movie not in friend_movie:
            unique_user_movie.append(movie)
    return unique_user_movie


def get_friends_unique_watched(user_data):
    unique_user_movie = []

    for movie in user_data["watched"]:
        if movie not in unique_user_movie:
            unique_user_movie.append(movie)

    friend_unique_movie = []

    for friend_list in user_data["friends"]:
        for movie in friend_list["watched"]:
            if movie not in unique_user_movie and movie not in friend_unique_movie:
                friend_unique_movie.append(movie)

    return friend_unique_movie

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------


def get_available_recs(user_data):
    friend_unique_movie = get_friends_unique_watched(user_data)
    rec_movies = []
    for movie in friend_unique_movie:
        if movie["host"] in user_data["subscriptions"]:
            rec_movies.append(movie)
    return rec_movies
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


def get_new_rec_by_genre(user_data):
    rec_movies = []
    most_watched_genre = get_most_watched_genre(user_data)
    friend_unique_movie = get_friends_unique_watched(user_data)

    for movie in friend_unique_movie:
        if most_watched_genre == movie["genre"]:
            rec_movies.append(movie)

    return rec_movies


def get_rec_from_favorites(user_data):
    unique_watched_movie = get_unique_watched(user_data)
    fav_titles = {movie["title"] for movie in user_data["favorites"]}


    rec_movies = [movie for movie in unique_watched_movie if movie["title"] in fav_titles]


    return rec_movies
