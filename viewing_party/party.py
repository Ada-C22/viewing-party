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
def get_unique_watched(user_data):

    friends_movies = set()
    for friend in user_data["friends"]:
        friends_movies.update(movie["title"] for movie in friend["watched"])

    unique_movies = [
        movie for movie in user_data["watched"] if movie["title"] not in friends_movies
    ]

    return unique_movies


def get_friends_unique_watched(user_data):

    user_movie_titles = {movie["title"] for movie in user_data["watched"]}
    
    unique_friends_movies = []
    friends_movie_titles = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            title = movie["title"]
            if title not in user_movie_titles:
                if title not in friends_movie_titles:
                    friends_movie_titles.add(title)
                    unique_friends_movies.append(movie)
    return unique_friends_movies


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):

    unique_movies = get_friends_unique_watched(user_data)

    recommended_movies = []
    for movie in unique_movies:
        host = movie["host"]
        if host in user_data["subscriptions"]:
            recommended_movies.append(movie)
    return recommended_movies
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):

    watched_genre_dict = {}
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in watched_genre_dict:
            watched_genre_dict[genre] += 1
            continue
        watched_genre_dict[genre] = 1
    
    frequent_genre = ""
    genre_highest_count = 0
    for genre, count in watched_genre_dict.items():
        if count > genre_highest_count:
            frequent_genre = genre
            genre_highest_count = count

    not_watched = get_friends_unique_watched(user_data)

    recommended_movies = [movie for movie in not_watched if movie["genre"] == frequent_genre]

    return recommended_movies


def get_rec_from_favorites(user_data):
    friends_movies = set()
    for friend in user_data["friends"]:
        friends_movies.update(movie["title"] for movie in friend["watched"])

    unique_movies = [
        movie for movie in user_data["favorites"] if movie["title"] not in friends_movies
    ]

    return unique_movies