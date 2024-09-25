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
    return user_data after adding movie to watched
    An empty list represents that the user has no movies in their watched list
    user_data = {
        'watched': [{"title": "", "genre": "", "rating": <float>}, {...}, {...}, {...}, {...}, {...}]
        }
    '''

    lod_watched = user_data["watched"]
    lod_watched.append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    '''
    return user_data after adding movie to watchlist
    An empty list represents that the user has no movies in their watchlist
    user_data = {
        'watchlist': [{"title": "", "genre": "", "rating": <float>}, {...}, {...}, {...}, {...}, {...}]
        }
    '''
    lod_watchlist = user_data["watchlist"]
    lod_watchlist.append(movie)
    return user_data

def watch_movie(user_data, title):
    '''
    - if title is in watchlist: remove from watchlist, add to watched, return user data
    - if movie is not in user watchlist, return user data
    user_data = {
        'watched': [{"title": "", "genre": "", "rating": <float>}, {...}, {...}, {...}, {...}, {...}],
        'watchlist': [{"title": "", "genre": "", "rating": <float>}, {...}, {...}, {...}, {...}, {...}]
        }
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
    '''
    return the average rating
    The average rating of an empty watched list is 0.0
    user_data = {
        'watched': [{"title": "", "genre": "", "rating": <float>}, {...}, {...}, {...}, {...}, {...}]
        }
    '''

    lod_watched = user_data["watched"]
    total_rating = 0
    
    if lod_watched == []:
        return 0.0
    for movie in lod_watched:
        total_rating += movie["rating"]
    
    avg_rating = total_rating/len(lod_watched)
    return avg_rating
        

def get_most_watched_genre(user_data):
    '''
    return the genre that is the most frequently watched
    If the value of "watched" is an empty list, get_most_watched_genre should return None.
    user_data = {
        'watched': [{"title": "", "genre": "", "rating": <float>}, {...}, {...}, {...}, {...}, {...}]
        }
    '''

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
    Return a list of dictionaries, that represents a list of movies that:
    -the user has watched, but none of their friends have watched. (user movies) - (friends movies)
    user_data = {
        'watched': [{...}, {...}, {...}, {...}, {...}, {...}], 
        friends': [{'watched': [..{},{},{}..], {'watched': [..{},{},{}..]
        }
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
    Return a list of dictionaries, that represents a list of movies that:
    - aleast one of the user's friends have watched, but the user has not watched aka (friends movies) - (user movies)
    user_data = {
        'watched': [{...}, {...}, {...}, {...}, {...}, {...}], 
        friends': [{'watched': [..{},{},{}..], {'watched': [..{},{},{}..]
        }
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
    '''
    user_data= {
        "subscriptions": [ "","","" ],
        "watched": [ {}, {}, {} ],
        "friends": [ {"watched": [...{},{}...] }, {"watched": [...{},{}...] }]
        }
    '''
    
    lod_unique_friends_movie = get_friends_unique_watched(user_data)

    lod_recommended_movies = []
    for movie in lod_unique_friends_movie:
        if movie["host"] in user_data["subscriptions"]:
            lod_recommended_movies.append(movie)

    return lod_recommended_movies


# wave 5

def get_new_rec_by_genre(user_data):    
    '''
    Return the list of recommended movies....A movie should be added to this list if and only if:
    -The user has not watched it
    -At least one of the user's friends has watched
    -The "genre" of the movie is the same as the user's most frequent genre
    '''
    # return lod of movies friends have watched but not user
    lod_unique_friends_movie = get_friends_unique_watched(user_data)

    # get user's most freq genre
    user_freq_genre = get_most_watched_genre(user_data)

    lod_recommended_movies = []
    for movie in lod_unique_friends_movie:
        if movie["genre"] == user_freq_genre:
            lod_recommended_movies.append(movie)

    return lod_recommended_movies

def get_rec_from_favorites(user_data):
    '''
    user_data= {
        "favorites": [ {}, {}, {} ],
        "watched": [ {}, {}, {} ],
        "friends": [ {"watched": [...{},{}...] }, {"watched": [...{},{}...] }]
        }
    '''
    # list of movies only the user has seen (not any of the friends)
    lod_user_unique_movies = get_unique_watched(user_data)

    lod_recommended_movies = []
    for movie in lod_user_unique_movies:
        if movie in user_data["favorites"]:
            lod_recommended_movies.append(movie)

    return lod_recommended_movies


