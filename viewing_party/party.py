# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    """
    Creates a movie dictionary with title, genre and rating
    """
    # Verify the arguments exist
    if title and genre and rating:
        return {
            "title": title,
            "genre": genre,
            "rating": rating,
        }

def add_to_watched(user_data, movie):
    """
    Adds the movie to the user's watched list.
    """
    # Verify the arguments exist
    if user_data and movie:
        user_data["watched"].append(movie)
        return user_data

def add_to_watchlist(user_data, movie):
    """
    Adds the movie to the user's watch list.
    """
    # Verify the arguments exist
    if user_data and movie:
        user_data["watchlist"].append(movie)
        return user_data

def watch_movie(user_data, title):
    """
    Moves a movie with the title "title" from the user's 
    watch list to the user's watched list.
    """
    # Verify the arguments exist
    if user_data and title:
        for movie in user_data["watchlist"]:
            if movie["title"] == title:
                user_data["watchlist"].remove(movie)
                add_to_watched(user_data, movie)
        return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    """
    Calculates the average rating of all the movies in the watched list.
    """
    # Verify the argument exists
    if user_data:
        total_ratings = 0
        number_of_movies = 0
        average_rating = 0.0
        # Sum all ratings and count movies
        for movie in user_data["watched"]:
            total_ratings += movie["rating"]
            number_of_movies += 1
        # Check if there are any movies to avoid ZeroDevisionError
        if number_of_movies:
            average_rating = total_ratings / number_of_movies

        return average_rating

def get_most_watched_genre(user_data):
    """
    Determines the most frequently watched genre from the user's watched list.
    """
    
    count_genres = {}

    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in count_genres:
            count_genres[genre] +=1
        else:
            count_genres[genre] =1
    # Find the maximum genre count based on count_genres values, return None if empty
    most_watched = max(count_genres, key=count_genres.get, default=None)
    return most_watched

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    """
    Identifies and returns a list of movies that the user has 
    watched but non their friends have watched.
    """
    user_watched_movies = user_data["watched"][:]
    friends = user_data["friends"]

    for friend in friends:
        for movie in friend["watched"]:
            if movie in user_watched_movies:
                user_watched_movies.remove(movie)
    return user_watched_movies

def get_friends_unique_watched(user_data):
    """
    Identifies and returns a list of movies watched by friends but not
    by the user.
    """
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
    """
    Generates and returns a list of movies watched by friends, unwatched by user, 
    and available on user’s subscriptions.
    """

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
    """
    Returns a list of unwatched movies in user’s favorite genre that friends have watched
    """

    rec_pool = get_friends_unique_watched(user_data)

    fav_genre = get_most_watched_genre(user_data)

    recommendations = []
    for movie in rec_pool:
        if movie["genre"] == fav_genre:
            recommendations.append(movie)
    return recommendations

def get_rec_from_favorites(user_data):
    """
    Returns a list of user's favorites movies their friends haven't watched.
    """

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
