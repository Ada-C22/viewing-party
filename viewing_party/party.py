import pytest

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    if title and genre and rating:
            return {
                "title": title,
                "genre": genre,
                "rating": rating
            }
    return None


def add_to_watched(user_data, movie):
    if movie not in movie:
         user_data['watched'] = []
         
    else:
         user_data['watched'].append(movie)
    
    return user_data
    

def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data,title):
    movie_to_move = None
    for movie in user_data['watchlist']:
        if movie['title'] == title:
            movie_to_move = movie
            break
          
    if movie_to_move:
        user_data['watchlist'].remove(movie_to_move)
        user_data['watched'].append(movie_to_move)
    
    return user_data
          
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

