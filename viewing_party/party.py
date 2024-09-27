# -----------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------
def create_movie(movie_title, genre, rating):

    movie= {}

    if movie_title and genre and rating:
    
        movie["title"] = movie_title
        movie["genre"] = genre
        movie["rating"] = rating          
        return movie

    return None

def add_to_watched(user_data, movie):

    # Create a copy of user data to avoid modifying original
    updated_user_data = {
            "watched": user_data["watched"][:]}

    updated_user_data["watched"].append(movie)
    return updated_user_data


def add_to_watchlist(user_data, movie):

    # Create a copy of user data to avoid modifying original
    updated_user_data = {
            "watchlist": user_data["watchlist"][:],
        } 
    updated_user_data["watchlist"].append(movie)
    return updated_user_data


def watch_movie(user_data, title):

    # Create a copy of user data to avoid modifying original 
    updated_user_data = {
            "watchlist": user_data["watchlist"][:],
            "watched": user_data["watched"][:]
        } 
    
    # Check if movie with the title is in watchlist 
    # and add it to the watched list
    for movie in updated_user_data["watchlist"]:
        if movie["title"] == title:
            updated_user_data["watchlist"].remove(movie)
            updated_user_data["watched"].append(movie)         
    return updated_user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):

    # User data is a dict which contains "watched" key
    count = 0.0
    sum = 0.0

    if len(user_data["watched"]) == 0:
        return sum
    
    # Count and sum rating values
    for movie in user_data["watched"]:
        if movie["rating"]:
            count += 1
            sum += movie["rating"]
        else:
            sum = 0

    # Return average 
    return sum/count


def get_most_watched_genre(user_data):

    max_value = 0
    genre_frequencies = {}

    if len(user_data["watched"]) == 0:
        return None
    
    # Create key,value pairs {"genre" : genre_frequencies} in dict.
    for movie in  user_data["watched"]:
        if movie["genre"] in genre_frequencies:
            genre_frequencies[movie["genre"]] += 1
        else:
            genre_frequencies[movie["genre"]] = 1

    # Check for the genre with highest frequencies   
    for key, current_value in genre_frequencies.items():
        if current_value > max_value:
            max_value = current_value
            most_watched = key #retrieve the key with the highest value
    
    return most_watched


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    # ONLY THE USER HAS WATCHED, BUT THE FRIENDS HAVE NOT
    user_unique_watched = []
    friends_watched = []
    
    # Get every movie from friends and add it to a new list
    for friend in user_data["friends"]:
        for movie in friend['watched']:
            friends_watched.append(movie)
    
    # Get every movie from user and add it to a list
    # only if is not in friends_wacthed list
    for movie in user_data["watched"]:
        if movie not in friends_watched:
            user_unique_watched.append(movie)

    return user_unique_watched


def get_friends_unique_watched(user_data):
    # AT LEAST ONE OF THE FRIENDS HAS WATCHED,
    # BUT THE USER HAS NOT

    user_watched = [movie for movie in user_data["watched"]]
    friends_unique_watched = []

    # Get every movie from friends and add it to a new list:
    # only if is not in the movies user has watched
    # AND if it's not already in the list
    for friend in user_data["friends"]:
        for movie in friend['watched']:
            if movie not in user_watched\
            and movie not in friends_unique_watched:
                friends_unique_watched.append(movie)

    return friends_unique_watched
    

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    
    rec_list = []

    # List of movies that at least one friend has watched and user hasn't
    friends_uniques = get_friends_unique_watched(user_data)
    
    # From friends movies add the movie to the list only if 
    # the host is in user subscriptions
    for movie in friends_uniques:
        if movie["host"] in user_data["subscriptions"]:
            rec_list.append(movie)
            
    return rec_list

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    
    user_freq_genre = get_most_watched_genre(user_data)
    friends_unique_movies = get_friends_unique_watched(user_data)
    

    rec_list = []
    
    # Check the movies in friends that correspond to the same genre
    # the user watch the most and add it to a list
    for movie in friends_unique_movies:
        if user_freq_genre in movie.values():
            rec_list.append(movie)

    return rec_list
    

def get_rec_from_favorites(user_data):

    user_only_movies = get_unique_watched(user_data)

    rec_list = []
    
    # Check user unique movies and add them to a list if
    # were marked as favorites
    for movie in user_only_movies:
        if movie in user_data["favorites"]:
            rec_list.append(movie)
            
    return rec_list