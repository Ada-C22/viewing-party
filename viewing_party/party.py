# ------------- WAVE 1 --------------------

# Create movies
def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None

    return {"title": title, "genre": genre, "rating": rating}

# Add movie to "watched" list
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

# Add movies to the watchlist
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

# Adds movie from watchlist to "watched" list
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

# Get average rating of user "watched" movies
def get_watched_avg_rating(user_data):
    total_rating = 0
    movies = user_data["watched"]

    # Return 0 if list of "watched" is empty
    if not movies:
        return total_rating

    # Find sum of ratings
    for movie in movies:
        total_rating += movie["rating"]

    return total_rating / len(movies)

# Get most watched genre
def get_most_watched_genre(user_data):
    # Return None if list of "watched" is empty
    if not user_data["watched"]:
        return None

    # Count watched genres
    genre_count = {}
    for movie in user_data["watched"]:
        if movie["genre"] not in genre_count:
            genre_count[movie["genre"]] = 1
        else:
            genre_count[movie["genre"]] += 1

    # Determine most watched genre
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

# Get all movies unique to user
def get_unique_watched(user_data):

    # Put titles that friends watched in a set
    friends_movies = set()
    for friend in user_data["friends"]:
        friends_movies.update(movie["title"] for movie in friend["watched"])

    # Create list of movies that only user watched
    unique_movies = [
        movie for movie in user_data["watched"] 
        if movie["title"] not in friends_movies
    ]

    return unique_movies

# Get movies unique to friends that user hasn't watched
def get_friends_unique_watched(user_data):

    # Put movie titles user has watched in a set
    user_movie_titles = {movie["title"] for movie in user_data["watched"]}

    # Create a list for movies only friends watched
    unique_friends_movies = []

    # Put movies friends watched to a set
    friends_movie_titles = set()
   
    # Iterate through movies, if movie title is not in a set 
    # unique to a user and if movie title is not in friends movies
    # add it to a set of titles unique to friends, so that we don't add
    # duplicates to unique friend's movies. Append movies 
    # to a list of unique movies 
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

# Get friends' recommendations for user
def get_available_recs(user_data):

    # Get unique movies friends watched, but user hasn't
    unique_movies = get_friends_unique_watched(user_data)

    recommended_movies = []
    # Append a movie to a list of recommended movies
    # if a movie is hosted by a subscription user has acces to
    for movie in unique_movies:
        host = movie["host"]
        if host in user_data["subscriptions"]:
            recommended_movies.append(movie)
    return recommended_movies


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

# Recommend movies from friends list based on user most frequent genre
def get_new_rec_by_genre(user_data):

    # Get user most frequent genre
    most_frequent_genre = get_most_watched_genre(user_data)

    # Create list of recommended movies with most frequent genre
    not_watched = get_friends_unique_watched(user_data)
    recommended_movies = [
        movie for movie in not_watched 
        if movie["genre"] == most_frequent_genre
    ]

    return recommended_movies

# Recommend movies from user favorites
def get_rec_from_favorites(user_data):
    # Get the list of movies that only the user has watched
    unique_movies = get_unique_watched(user_data)

    # Get a set of favorite movie titles
    favorite_movies = {fav_movie["title"] for fav_movie in user_data["favorites"]}
    
    # Filter the unique movies to only those that are in the user's favorites
    recommended_favorites = [
        movie
        for movie in unique_movies
        if movie["title"] in favorite_movies
    ]

    return recommended_favorites
