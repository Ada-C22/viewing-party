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

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

