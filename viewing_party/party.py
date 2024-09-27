# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    '''
    Creates a dictionary representing a movie with the given title, genre,
    and rating.
    '''
    if not (title and genre and rating):
        return None
    return {'title': title, 'genre': genre, 'rating': rating}

def add_to_watched(user_data, movie):
    '''
    Adds a movie to the user's watched list.
    '''
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    '''
    Adds a movie to the user's watchlist.
    '''
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, title):
    '''
    Moves a movie from the user's watchlist to the watched list if the
    movie title is found.
    '''

    for movie in user_data['watchlist']:
        if title == movie['title']:
            user_data['watched'].append(movie)
            user_data['watchlist'].remove(movie)
            break
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    '''
    Calculates the average rating of all movies watched by the user. If
    no movies are watched, returns 0.0.
    '''
    total_ratings = 0.0

    if not user_data['watched']:
        return total_ratings
    
    for movie in user_data['watched']:
        total_ratings += movie['rating']

    return total_ratings / len(user_data['watched'])

def get_most_watched_genre(user_data):
    '''
    Determines the genre most frequently watched by the user. Returns
    None if no movies are watched.
    '''
    if not user_data['watched']:
        return None
    
    genre_count = {}
    for movie in user_data['watched']:
        genre = movie['genre']
        genre_count[genre] = genre_count.get(genre, 0) + 1

    most_watched_genre = None
    max_count = 0
    for genre, count in genre_count.items():
        if count > max_count:
            max_count = count
            most_watched_genre = genre

    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    '''
    Retrieves a list of movies that the user has watched, but their 
    friends have not.
    '''
    friends_watched_list = get_friends_watched_list(user_data)
    return get_unique_list(user_data['watched'], friends_watched_list)

def get_friends_unique_watched(user_data):
    '''
    Retrieves a list of movies that the user's friends have watched, but
    the user has not.
    '''
    friends_watched_list = get_friends_watched_list(user_data)
    unique_watched_list = get_unique_list(friends_watched_list, user_data['watched'])
    
    unique_movies_list = []
    movies_seen = set()

    for movie in unique_watched_list:
        movie_tuple = tuple(movie.items())
        if movie_tuple not in movies_seen:
            movies_seen.add(movie_tuple)
            unique_movies_list.append(movie)

    return unique_movies_list


def get_friends_watched_list(user_data):
    '''
        Retrieves a list of all movies watched by the user's friends.
    '''
    return ([movie for friend in user_data['friends']
            for movie in friend['watched']])

def get_unique_list(source_list, exclusion_list):
    '''
    Returns a list of items found in the source list, excluding those 
    from the exclusion list.
    '''
    return [item for item in source_list if item not in exclusion_list]

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    '''
    Retrieves a list of recommended movies that friends have watched and
    are available on the streaming services the user has access to.
    '''
    friends_unique_watched = get_friends_unique_watched(user_data)

    return ([movie for movie in friends_unique_watched
                if movie['host'] in user_data['subscriptions']])

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    '''
    Compiles a list of recommended movies for the user. Movies added to
    this list will match the user's most frequent genre, will have been
    watched by at least one of the user's friends, and will not have been
    watched yet by the user.
    '''
    if (not user_data['watched'] or not any(friend['watched']
            for friend in user_data['friends'])):
        return []

    available_recs = get_available_recs(user_data)
    most_watched_genre = get_most_watched_genre(user_data)

    return ([rec for rec in available_recs
                if rec['genre'] == most_watched_genre
                and not any(movie['title'] == rec['title']
                for movie in user_data['watched'])])

def get_rec_from_favorites(user_data):
    '''
    Compiles a list of recommended movies from the user's favorites that
    no friends have watched.
    '''

    if not user_data['favorites']:
        return []
    
    if not user_data['friends']:
        return user_data['favorites']

    friends_watched_titles = ({
        movie['title'] for friend in user_data['friends']
        for movie in friend['watched']
    })

    rec_from_favorites = ([
        favorite for favorite in user_data['favorites']
        if favorite['title'] not in friends_watched_titles
    ])

    return rec_from_favorites