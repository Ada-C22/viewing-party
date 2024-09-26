# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    if title and genre and rating:
        return {
            "title": title,
            "genre": genre,
            "rating": rating,
        }
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):

    total_ratings = 0
    number_of_movies = 0
    for movie in user_data["watched"]:
        total_ratings += movie["rating"]
        number_of_movies += 1
        average_rating = total_ratings / number_of_movies

    if number_of_movies == 0:
        return 0.0
    return average_rating

def get_most_watched_genre(user_data):

    if user_data['watched'] == []:
        return None

    count_genres = {}

    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in count_genres:
            count_genres[genre] +=1
        else:
            count_genres[genre] =1

    most_watched = max(count_genres, key= count_genres.get)
    return most_watched

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    user_watched_movies = user_data["watched"][:]
    friends = user_data["friends"]

    for friend in friends:
        for movie in friend["watched"]:
            if movie in user_watched_movies:
                user_watched_movies.remove(movie)
    return user_watched_movies

def get_friends_unique_watched(user_data):
    user_watched_movies = user_data["watched"]
    friends = user_data["friends"]
    unique_watched = []

    for friend in friends:
        for friend_movie in friend["watched"]:
            if friend_movie not in user_watched_movies and friend_movie not in unique_watched:
                unique_watched.append(friend_movie)
    return unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):

    recommended_title = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie["host"] in user_data["subscriptions"]:
                if movie not in recommended_title:
                    recommended_title.append(movie)
    return recommended_title

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    rec_pool = get_friends_unique_watched(user_data)
    user_watched = user_data["watched"]
    genre_count = dict()

    for movie in user_watched:
        if movie["genre"] in genre_count:
            genre_count[movie["genre"]] += 1
        else:
            genre_count[movie["genre"]] = 1

    fav_genre = ""
    fav_genre_count = 0
    for genre, count in genre_count.items():
        if count > fav_genre_count:
            fav_genre = genre
            fav_genre_count = count

    recommendations = []
    for movie in rec_pool:
        if movie["genre"] == fav_genre:
            recommendations.append(movie)
    return recommendations

def get_rec_from_favorites(user_data):

    favorites = user_data["favorites"][:]

    friends_watched = []
    friends = user_data["friends"]

    for friend in friends:
        for friend_movie in friend["watched"]:
            friends_watched.append(friend_movie)

    for movie in favorites:
        if movie in friends_watched:
            favorites.remove(movie)

    return favorites
