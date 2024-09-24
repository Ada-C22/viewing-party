# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    '''If those three attributes are truthy, then return a dictionary. This dictionary should...
    Have three key-value pairs, with specific keys
    The three keys should be "title", "genre", and "rating"
    The values of these key-value pairs should be appropriate values
    If title is falsy, genre is falsy, or rating is falsy, this function should return None'''

    # create dict
    movie_dict = {}

    # falsy case
    # even if one is falsy, the whole cond will return NONE
    if not title or not genre or not rating:
        return None
    
    movie_dict["title"] = title
    movie_dict["genre"] = genre
    movie_dict["rating"] = rating

    return movie_dict

def add_to_watched(user_data, movie):
    '''
    the value of user_data will be a dictionary with a key "watched", and a value which is a list of dictionaries representing the movies the user has watched
    An empty list represents that the user has no movies in their watched list
    in this case, user_data represents movies we have watched
    user_data = {"watched": [...list of movie_dict watched...]}
    '''

    list_of_watched_movie_dict = user_data["watched"]
    list_of_watched_movie_dict.append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    '''
    the value of user_data will be a dictionary with a key "watchlist", and a value which is a list of dictionaries representing the movies the user wants to watch
    An empty list represents that the user has no movies in their watchlist
    user_data = {"watchlist": [...list of movie_dict wanting to watch...]}
    '''
    list_of_watchlist_dict = user_data["watchlist"]
    list_of_watchlist_dict.append(movie)
    return user_data

def watch_movie(user_data, title):
    '''
    - user_data: dictionary with a "watchlist" and a "watched" keys
        - values are list of dict of movies that are wither watched or on watchlist
    - title: string, rep. title of movie user watched

    - if title is in watchlist: remove from watchlist, add to watched, return user data
    - if movie is not in user watchlist, return user data
    '''

    list_of_watchlist_dict = user_data["watchlist"]
    list_of_watched_movie_dict = user_data["watched"]
    # returns [ {movie_dict} , {movie_dict} , ...]

    for movie_dict in list_of_watchlist_dict:
        if movie_dict["title"] == title:
            # remove from watchlist
            list_of_watchlist_dict.remove(movie_dict)
            # add to watched
            list_of_watched_movie_dict.append(movie_dict)
            # exit loop early if found
            break
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    '''
    the value of user_data will be a dictionary with a "watched" list of movie dictionaries
    This represents that the user has a list of watched movies
    Calculate the average rating of all movies in the watched list
    The average rating of an empty watched list is 0.0
    return the average rating
    user_data = {"watched": [...list of movie_dict watched...]}
    '''
    list_of_watched_movie_dict = user_data["watched"]

    # if the list is empty/falsy
    if not list_of_watched_movie_dict:
        return 0.0

    rating_sum = 0
    for movie_dict in list_of_watched_movie_dict:
        rating = movie_dict["rating"]
        rating_sum += rating
    return rating_sum/len(list_of_watched_movie_dict)

    # what if the movie_dict has no rating

def get_most_watched_genre(user_data):
    '''
    the value of user_data will be a dictionary with a "watched" list of movie dictionaries. Each movie dictionary has a key "genre".
    This represents that the user has a list of watched movies. Each watched movie has a genre.
    The values of "genre" is a string.
    Determine which genre is most frequently occurring in the watched list
    return the genre that is the most frequently watched
    If the value of "watched" is an empty list, get_most_watched_genre should return None.
    '''
    list_of_watched_movie_dict = user_data["watched"]

    # if the list is empty/falsy
    if not list_of_watched_movie_dict:
        return None
    
    # # used list comprehension to create the list of movie genre strings
    # genres = [movie_dict["genre"] for movie_dict in list_of_watched_movie_dict]

    # initialize dict
    genre_count_dict = {}

    for movie_dict in list_of_watched_movie_dict:
        genre = movie_dict["genre"]
        count = genre_count_dict.get(genre,0)
        genre_count_dict[genre] = count + 1
    
    max_genre = None
    max_count = 0

    for genre, count in genre_count_dict.items():
        if count > max_count:
            max_count = count
            max_genre = genre
    return max_genre



    







