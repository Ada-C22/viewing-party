# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    """
    Create a dictionary representing a movie
    
    Parameters:
        title(str): the title of movie
        genre (str): the genre of movie
        rating (float): the rating of movie
    
    Returns:
        dict: with keys "title", "genre", "rating" if all arguments are truthy
        None: if any of arguments are falsy
    """
    
    if not title or not genre or rating is None:
        return None
    
    # Checking if user inputs on these parameters are all valid.
    if not isinstance(title, str) or not isinstance(genre, str) \
        or not isinstance(rating, float) or not isinstance(rating, int):
        return None
    else:
        return {"title": title, "genre": genre, "rating": rating}

    
def  add_to_watched(user_data, movie):
    """
    Add a movie to user's watched list
    
    Parameters:
        user_data (dict): with a key "watched" 
        and values is a list of dictionaries movies they have watched
        or empty list represent no movies have watched
        movie (dict): {
                "title": "Title A",
                "genre": "Horror",
                "rating": 3.5
            }
    
    Return:
        user_data ("watched" list of movies)
    """

    user_data["watched"].append(movie)
    return user_data    


def add_to_watchlist(user_data, movies):
    """
    Add a movie to user's watchlist
    
    Parameters:
        user_data (dict): with a key "watchlist" 
        and values is a list of dictionaries movies user wants to watch
        or empty list represent no movies in watchlist
        movie (dict): {
                "title": "Title A",
                "genre": "Horror",
                "rating": 3.5
            }
    
    Return:
        user_data (watchlist of movies)
    """
    user_data["watchlist"].append(movies)
    return user_data
 
    
def watch_movie(user_data, title):
    """
    Parameters:
        user_data (dict): with two keys "watchlist" and "watched" 
        
        title (str): represent title of movie user has watched
    Return:
        if title is in a movie in user's watchlist:
            remove from watchlist
            add to watched
            return user_data
        if not in watchlist:
            return user_data
    """  
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watchlist"].remove(movie) 
            user_data["watched"].append(movie)
        
    return user_data


# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    """
    function calculate and return average rating
    
    Parameters:
        user_data (dict): "watched" list of movie dictionaries.
        
    Notes:
        if average rating of empty watched list if 0.0
    
    Returns:
        Average rating (float)        
    """
    total_rating = 0
    movies = 0
    for movie in user_data["watched"]:
        movies += 1
        total_rating += movie["rating"]
        
    if movies > 0:    
        average_rating = total_rating/movies   
    else:
        average_rating = 0.0   

    return average_rating

def get_most_watched_genre(user_data):
    """
    Get the most frequently watched genre from user's watched movies
    
    Parameter:
        user_data (dict): 
            the key "watched" is a list of dictionaries, where each dictionary represent a movie
            each movie dict contains a key "genre" (str)
    Returns:
        str: the genre that user watched frequently
        None: if "watched" list is empty
    """
    genres_count = {} # map from genre to count

    # Return None if there is no value in "watched."
    if user_data["watched"] == []:
        return None
    
    # Add and count the genres found. 
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre not in genres_count:
            genres_count[genre] = 1
        else:
            genres_count[genre] += 1
            
    max_rate = 0
    most_frequent_genre = None
    # Comparing the rates and returning the most frequenty genre.
    for key, rate in genres_count.items():
        if rate > max_rate:
            most_frequent_genre = key
            max_rate = rate    
    
    # using max() to get the max count in genere_count dictionary       
    # most_frequent_genre = max(genres_count, key=genres_count.get) 
    # If use max(dictionary), max() looks only at the keys of the dictionary, not the values.
	# If the keys are strings, max() will return the key that comes last alphabetically   
               
    return most_frequent_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_friends_watched(user_data):
    """
    Helper function to get list of all movies that friends have watched
    """
    friends_watched= []
    
    for friend in user_data["friends"]:
        friends_watched.extend(friend["watched"])
        
    return friends_watched


def get_unique_watched(user_data):
    """
    This function determines which movies the user has watched 
    but none of the friends have watched.
    
    Parameters:
        user_data(dict): has two keys:
            "watched": List of movie dictionaries the user has watched, each with a "title".
            "friends": List of friends, each having a "watched" list of movie dictionaries.

    Returns:
        list of dict of movies.
    """
    
    user_watched = user_data["watched"]
    friends_watched = get_friends_watched(user_data)
    
    unique_watched = []

    for movie in user_watched:
        if movie not in friends_watched:
            unique_watched.append(movie)

    return unique_watched


def get_friends_unique_watched(user_data):
    """
    This function determines which movies the user has not watched 
    but at least one of the friends have watched.
    
    Parameters:
        user_data(dict): has two keys:
            "watched": List of movie dictionaries the user has watched, each with a "title".
            "friends": List of friends, each having a "watched" list of movie dictionaries.

    Returns:
        list of dict of unique movies.
    """
    
    user_watched = user_data["watched"]
    friends_watched = get_friends_watched(user_data)

    unique_friends_watched = []

    for movie in friends_watched:
        if movie not in user_watched and movie not in unique_friends_watched:
            unique_friends_watched.append(movie)
    
    return unique_friends_watched


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------


def get_available_recs (user_data):
    """
    Return a list of recommended movies based on the user's subscriptions 
        and their's friends watched movies
        
    Parameters:
        user_data (dict): has two keys:
            "subscriptions": List of streaming services the user has access to
            "friends": List of friends, each having a "watched" list of movie dictionaries, 
                each movie has a "host"
    
    Returns:
        list of dict of movies
    """
    
    user_watched = user_data["watched"]
    friends_watched = get_friends_watched(user_data)
  
    recommended_movies = []
    for movie in friends_watched:
        if movie not in user_watched and movie["host"] in user_data["subscriptions"] \
            and movie not in recommended_movies:
            recommended_movies.append(movie)
    
    return recommended_movies   
           
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    """
    Determine a list of recommended movies
    
    Parameters:
        user_data (dict)
    Notes:
        user has not watched that movie
        at leats one of user's friends has watched it
        "genre" == user's frequent genre
    Returns:
        recomemded movies (list)
    """
    
    user_watched = user_data["watched"]
    friends_watched = get_friends_watched(user_data)
    most_frequenty_genre = get_most_watched_genre(user_data)
    
    # Returns a list of recommended movies based in user's most frequently watched genre.
    recommended_movies = []
    for movie in friends_watched:
        if movie not in user_watched and \
            movie["genre"] == most_frequenty_genre and\
            movie not in recommended_movies:

            recommended_movies.append(movie)
    
    return recommended_movies  


def get_rec_from_favorites(user_data):
    """
    Determine a list of recommended movies
    
    Parameters:
        user_data (dict): "favorites" field contain a favorite list of movie dictionaries of user
    Notes:
        movie in user's "favorites"
        non of user's friends have watched it
        
    Returns:
        recomemded movies (list)
    """
    user_watched = user_data["watched"]
    friends_watched = get_friends_watched(user_data)

    # Loop through user favorites movies and creates a list of recommended movies. 
    recommended_movies = []

    for movie in user_watched:
        if movie in user_data["favorites"] and\
        movie not in friends_watched:
            recommended_movies.append(movie)

    return recommended_movies
