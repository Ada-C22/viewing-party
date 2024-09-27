# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    '''
    Creates a dictionary representing a movie with the given title, genre,
    and rating.

    Parameters:
        title (str): Movie title
        genre (str): Movie genre
        rating (float): Movie rating

    Returns:
        user_data (dict): A dictionary with the movie's title, genre, and
        rating, or None if any of the inputs are falsy.
    '''
    if not (title and genre and rating):
        return None
    return {'title': title, 'genre': genre, 'rating': rating}

def add_to_watched(user_data, movie):
    '''
    Adds a movie to the user's watched list.

    Parameters:
        user_data (dict): A dictionary containing the user's data,
        including a "watched" key.
        movie (dict): A dictionary representing the movie to be added to
        the user's "watched" list.

    Returns:
        user_data (dict): The updated user_data with the movie added to
        the "watched" list.
    '''
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    '''
    Adds a movie to the user's watchlist.

    Parameters:
        user_data (dict): A dictionary containing the user's data,
        including a "watchlist" key.
        movie (dict): A dictionary representing the movie to be added to
        the user's watchlist.
    Returns:
        user_data (dict): The updated user_data with the movie added to
        the "watchlist" list.
    '''
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    '''
    Moves a movie from the user's watchlist to the watched list if the
    movie title is found.

    Parameters:
        user_data (dict): A dictionary containing the user's data,
        including "watchlist" and "watched" keys.
        title (str): The title of the movie to move from the watchlist
        to the watched list.
    Returns:
        user_data (dict): The updated user_data with the movie added to
        the "watchlist" list.
    '''
    for movie in user_data['watchlist']:
        if title == movie["title"]:
            user_data['watched'].append(movie)
            user_data['watchlist'].remove(movie)
            break
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    '''
    Calculates the average rating of all movies watched by the user.

    Parameter:
    user_data (dict): A dictionary with a "watched" list of movie
    dictionaries. Each movie dictionary contains information on the 
    genre, rating, and title of the movie.

    Returns:
    (float): The average rating of all movies in the watched list, 0.0
    if the list is empty.
    '''
    if not user_data['watched']:
        return 0.0
    
    total_ratings = 0.0
    for movie in user_data['watched']:
        total_ratings += movie['rating']

    average_rating = total_ratings / len(user_data['watched'])
    return average_rating

def get_most_watched_genre(user_data):
    '''
    Determines the genre most frequently watched by the user.
    
    Parameter:
        user_data (dict): A dictionary with a "watched" list of movie 
        dictionaries. Each movie dictionary contains information on the
        genre, rating, and title of the movie.

    Returns:
        most_watched_genre (string): The genre most frequently watched by
        the user, None if the list is empty.
    '''
    if not user_data['watched']:
        return None
    
    count = {}
    most_watched_genre = None
    max_count = 0

    for movie in user_data['watched']:
        genre = movie['genre']
        count[genre] = count.get(genre, 0) + 1

        if count[genre] > max_count:
            max_count = count[genre]
            most_watched_genre = genre

    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    '''
    Retrieves a list of movies that the user has watched, but their 
    friends have not.

    Parameters:
        user_data (dict): A dictionary containing the user's watched
        movies and their friends' watched movies. The key "watched" 
        corresponds to a list of movies for the user, and the key
        "friends" maps to a list of dictionaries representing individual
        friends, each with "watched" keys

    Returns:
        unique_watched (list): A list of dictionaries representing movies
        that have been watched by the user but not their friends.
    '''
    user_watched_list = list(user_data["watched"])

    friends_watched_list = []
    for friend in user_data["friends"]:
        friends_watched_list += friend["watched"]

    unique_watched = []
    for movie in user_watched_list:
        if movie not in friends_watched_list:
            unique_watched.append(movie)

    return unique_watched

def get_friends_unique_watched(user_data):
    '''
    Retrieves a list of movies that the user's friends have watched, but
    the user has not.

    Parameters:
        user_data (dict): A dictionary containing the user's watched
        movies and their friends' watched movies. The key "watched" 
        corresponds to a list of movies for the user, and the key
        "friends" maps to a list of dictionaries representing individual
        friends, each with "watched" keys

    Returns:
        unique_watched (list): A list of dictionaries representing movies
        that have been watched by the user's friends but not them.
    '''
    user_watched_list = list(user_data["watched"])

    friends_watched_list = []
    for friend in user_data["friends"]:
        friends_watched_list += friend["watched"]

    unique_watched = []
    for movie in friends_watched_list:
        if movie not in user_watched_list:
            unique_watched.append(movie)

    unique_watched = remove_duplicates(unique_watched)

    return unique_watched

def remove_duplicates(list_of_dicts):
    '''
        Removes duplicate dictionaries from a list based on their contents.

        Parameters:
            list_of_dicts (list): A list of dictionaries from which
            duplicates should be removed.

        Returns:
            unique_list (list): A list of unique dictionaries. Preserves
            the order of occurrence.
    '''
    unique_list = []
    seen = set()

    for d in list_of_dicts:
        dict_tuple = tuple(d.items())

        if dict_tuple not in seen:
            seen.add(dict_tuple)
            unique_list.append(d)

    return unique_list
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    friends_user_data = get_friends_unique_watched(user_data)
    user_rec_movie_data = []
    for movie in friends_user_data:
        if movie["host"] in user_data["subscriptions"]:
            user_rec_movie_data.append(movie)
    return user_rec_movie_data

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    '''
    Compiles a list of recommended movies for the user. Movies added to
    this list will match the user's most frequent genre, will have been
    watched by at least one of the user's friends, and will not have been
    watched yet by the user.

    Parameters:
        user_data (dict): A dictionary with a "watched" list of movie
        dictionaries. Each movie dictionary contains information on the 
        genre, rating, and title of the movie.
    Returns:
        recs_by_genre (list): A list of dictionaries that represents a 
        list of movies recommended for the user.
    '''
    if not user_data['watched']:
        return []
        
    for friend in user_data['friends']:
        is_friends_empty = True
        if friend['watched']:
            is_friends_empty = False
            break
    if is_friends_empty:
        return []
    
    recs_by_genre = []
    available_recs = get_available_recs(user_data)
    most_watched_genre = get_most_watched_genre(user_data)

    for rec in available_recs:
        if rec['genre'] == most_watched_genre:
            is_rec_found = False
            for movie in user_data['watched']:
                if rec['title'] == movie['title']:
                    is_rec_found = True
                    break
            if not is_rec_found:
                recs_by_genre.append(rec)

    return recs_by_genre

def get_rec_from_favorites(user_data):
    # user_data['favorites'] = list of movie dictionaries
    # ^ user's favorite movies
    # list recommended movies. include if
    ## movie is in user's favorites
    ## no friends have watched it

    if not user_data['favorites']:
        return []
    elif not user_data['friends']:
        return user_data['favorites']

    friends_watched_set = set()
    for friend in user_data['friends']:
        for movie in friend['watched']:
            friends_watched_set.add(movie['title'])

    favorites_recommended = []
    for favorite in user_data['favorites']:
        if favorite['title'] not in friends_watched_set:
            favorites_recommended.append(favorite)

    return favorites_recommended