# to avoid naming confusing
# "lod" in lod_<var.name> means list of dict
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

    lod_watched = user_data["watched"]
    lod_watched.append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    '''
    the value of user_data will be a dictionary with a key "watchlist", and a value which is a list of dictionaries representing the movies the user wants to watch
    An empty list represents that the user has no movies in their watchlist
    user_data = {"watchlist": [...list of movie_dict wanting to watch...]}
    '''
    lod_watchlist = user_data["watchlist"]
    lod_watchlist.append(movie)
    return user_data

def watch_movie(user_data, title):
    '''
    - user_data: dictionary with a "watchlist" and a "watched" keys
        - values are list of dict of movies that are wither watched or on watchlist
    - title: string, rep. title of movie user watched

    - if title is in watchlist: remove from watchlist, add to watched, return user data
    - if movie is not in user watchlist, return user data
    '''

    lod_watchlist = user_data["watchlist"]
    lod_watched = user_data["watched"]
    # returns [ {movie_dict} , {movie_dict} , ...]

    for movie_dict in lod_watchlist:
        if movie_dict["title"] == title:
            # remove from watchlist
            lod_watchlist.remove(movie_dict)
            # add to watched
            lod_watched.append(movie_dict)
            # exit loop early if found
            break

    return user_data


#wave 2 

def get_watched_avg_rating(user_data):
    """
    the value of user_data will be a dictionary with a "watched" list of movie dictionaries
    This represents that the user has a list of watched movies
    Calculate the average rating of all movies in the watched list
    The average rating of an empty watched list is 0.0
    return the average rating
    user_data = {"watched": [...list of movie_dict watched...]}
    """

    lod_watched = user_data["watched"]
    total_rating = 0
    
    if lod_watched == []:
        return 0.0
    for movie in lod_watched:
        total_rating += movie["rating"]
    
    avg_rating = total_rating/len(lod_watched)
    return avg_rating
        

def get_most_watched_genre(user_data):
    """
    the value of user_data will be a dictionary with a "watched" list of movie dictionaries. Each movie dictionary has a key "genre".
    This represents that the user has a list of watched movies. Each watched movie has a genre.
    The values of "genre" is a string.
    Determine which genre is most frequently occurring in the watched list
    return the genre that is the most frequently watched
    If the value of "watched" is an empty list, get_most_watched_genre should return None.
    """

    lod_watched = user_data["watched"]
    genre_count = {}


    if lod_watched == []:
        return None
    for movie in lod_watched:
        genre = movie["genre"] # assigning value of genre to variable "genre"
        count = genre_count.get(genre, 0)
        genre_count[genre] = count + 1

    # Determine the most frequent
    max_count = 0
    frequent_genre = None

    for key, value in genre_count.items():
        if value > max_count:
            max_count = value
            frequent_genre = key
    return frequent_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    '''
    the value of user_data will be a dictionary with a "watched" list of movie dictionaries, and a "friends"
    This represents that the user has a list of watched movies and a list of friends
    The value of "friends" is a list
    Each item in "friends" is a dictionary. This dictionary has a key "watched", which has a list of movie dictionaries.
    Each movie dictionary has a "title".
    Determine which movies the user has watched, but none of their friends have watched.
    Return a list of dictionaries, that represents a list of movies
    user_data = {'watched': [{...}, {...}, {...}, {...}, {...}, {...}], 
    friends': [{'watched': [..{},{},{}..], {'watched': [..{},{},{}..]
                                                                                                 v [{'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8}, {'title': 'The Lord of the Functions: The Return of the Value', 'genre': 'Fantasy', 'rating': 4.0}, {'title': 'The Programmer: An Unexpected Stack Trace', 'genre': 'Fantasy', 'rating': 4.0}, {'title': 'It Came from the Stack Trace', 'genre': 'Horror', 'rating': 3.5}]   
    '''
    titles_friends_watched = set()

    for friend_movie_dict in user_data["friends"]:
        for movie in friend_movie_dict["watched"]:
            titles_friends_watched.add(movie["title"])
    
    # unique list of movies user's watched but not their friends
    list_unique_movies = []
    for movie in user_data["watched"]:
        if movie["title"] not in titles_friends_watched:
            list_unique_movies.append(movie)
            
    return list_unique_movies

def get_friends_unique_watched(user_data):
    '''
    user_data = {'watched': [{...}, {...}, {...}, {...}, {...}, {...}], 
    friends': [{'watched': [..{},{},{}..], {'watched': [..{},{},{}..]
    '''

    list_titles_watched = set()
    for movie in user_data["watched"]:
        list_titles_watched.add(movie["title"])

    list_friends_unique_movie = []
    for friend in user_data["friends"]:
        for movie_dict in friend["watched"]:
            if movie_dict["title"] not in list_titles_watched and movie_dict not in list_friends_unique_movie:
                list_friends_unique_movie.append(movie_dict)

    return list_friends_unique_movie


    
# Wave 4
def get_available_recs(user_data):
    """user_data= {
        "subscriptions": ["", "", ""],
        "watched": [ {}, {}, {} ],
        "friends": [ {"watched": [...{},{}...] }, {"watched": [...{},{}...] }]
            },
    """ 
    
    lod_unique_friends_movie = get_friends_unique_watched(user_data)

    lod_recommended_movies = []
    for movie in lod_unique_friends_movie:
        if movie["host"] in user_data["subscriptions"]:
            lod_recommended_movies.append(movie)

    return lod_recommended_movies








# # -----------------------------------------
# # ------------- WAVE 5 --------------------
# # -----------------------------------------

