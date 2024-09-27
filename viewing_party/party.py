# ------------- WAVE 1 --------------------
# Refactored
def create_movie(title, genre, rating):
    if not (title and genre and rating):
        return None
    return {'title': title, 'genre': genre, 'rating': rating}

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data: dict, movie: dict):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
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

    num_movies = 0
    sum = 0.0
    average_rating = 0.0

    while num_movies < len(user_data['watched']):
        sum += user_data['watched'][num_movies]['rating']
        num_movies += 1

    average_rating = sum / num_movies

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
    for movie in user_data['watched']:
        genre = movie['genre']
        if genre in count:
            count[genre] += 1
        else:
            count[genre] = 1

    max_count = 0
    for genre, genre_count in count.items():
        if genre_count > max_count:
            max_count = genre_count
            most_watched_genre = genre

    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
# Refactored
def get_unique_watched(user_data):
    user_watched_list = list(user_data["watched"])

    friends_watched_list = []
    for friend in user_data["friends"]:
        friends_watched_list += friend["watched"]

    unique_watched = []
    for movie in user_watched_list:
        if movie not in friends_watched_list:
            unique_watched.append(movie)

    return unique_watched

def remove_duplicates(list_of_dicts):
    unique_list = []
    seen = set()

    for d in list_of_dicts:
        dict_tuple = tuple(d.items())

        if dict_tuple not in seen:
            seen.add(dict_tuple)
            unique_list.append(d)

    return unique_list

def get_friends_unique_watched(user_data):
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