# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    if title is None or genre is None or rating is None:
        return None
    return {'title': title, 'genre': genre, 'rating': rating}

def add_to_watched(user_data, movie):
    watched_list = user_data["watched"]
    watched_list.append(movie)
    return user_data

def add_to_watchlist(user_data: dict, movie: dict):

    movie_list = user_data["watchlist"]
    movie_list.append(movie)
    return user_data

def watch_movie(user_data, title):
    watchlist = user_data['watchlist']
    watched = user_data['watched']
    for movie in watchlist:
        if title == movie["title"]:
            watched.append(movie)
            watchlist.remove(movie)
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
def get_unique_watched(user_data):
    # user_list
    watched_user_list = []
    for movie in user_data["watched"]:
        watched_user_list.append(movie)

    user_movies_titles = set()
    for movie in watched_user_list:
        user_movies_titles.add(movie["title"])

    # friends_watched_list
    watched_list_of_friends = []
    for movie in user_data["friends"]:
        if "watched" in movie:
            watched_list_of_friends.extend(movie["watched"])

    friends_movies_titles = set()
    for movie in watched_list_of_friends:
        friends_movies_titles.add(movie["title"])


    unwatched_movies = []
    combined_movies_lists = user_movies_titles - friends_movies_titles
    for movie in watched_user_list:
        if movie["title"] in combined_movies_lists:
            unwatched_movies.append(movie)


    return unwatched_movies

def remove_duplicates(list_of_dicts):
    unique_list = []
    seen = set()

    for d in list_of_dicts:
        dict_tuple = tuple(sorted(d.items()))

        if dict_tuple not in seen:
            seen.add(dict_tuple)
            unique_list.append(d)

    return unique_list

def get_friends_unique_watched(user_data):
    # user_list
    watched_user_list = []
    for movie in user_data["watched"]:
        watched_user_list.append(movie)

    user_movies_titles = set()
    for movie in watched_user_list:
        user_movies_titles.add(movie["title"])

    # friends_watched_list
    watched_list_of_friends = []
    for movie in user_data["friends"]:
        if "watched" in movie:
            watched_list_of_friends.extend(movie["watched"])

    watched_list_of_friends = remove_duplicates(watched_list_of_friends)

    friends_movies_titles = set()
    for movie in watched_list_of_friends:
        friends_movies_titles.add(movie["title"])

    unwatched_movies = []
    combined_movies_lists = friends_movies_titles - user_movies_titles
    for movie in watched_list_of_friends:
        if movie["title"] in combined_movies_lists:
            unwatched_movies.append(movie)

    return unwatched_movies
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