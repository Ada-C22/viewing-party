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




# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

