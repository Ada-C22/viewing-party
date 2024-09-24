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
    
    if not title or not genre or not rating:
        return None
    
    try:
        # Checking if user inputs on these parameters are all valid.
        if not isinstance(title, str) or not isinstance(genre, str) \
            or not isinstance(rating, float):
            return None
        else:
            return {"title": title, "genre": genre, "rating": rating}
        
    # very general and we dont intend to reading     
    except Exception as e:
        print(e)
        return None
    
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
    
    try:
        
        user_data["watched"].append(movie)
        return user_data    
    
    except Exception as e:
        print(e)
        
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
    try:
        user_data["watchlist"].append(movies)
        return user_data
    
    except Exception as e:
        print (e)    

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
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

