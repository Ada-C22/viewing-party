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
          

# ------------- WAVE 2 --------------------

def get_watched_avg_rating(user_data):

    watched_movies = user_data.get('watched', [])

    rating_sum = 0.0
    total_movies = 0

    for movie in watched_movies:
        rating = movie.get('rating')
        if rating is not None:
            rating_sum += rating
            total_movies += 1

    if total_movies == 0:
        return 0.0  

    average_rating = rating_sum / total_movies
    return average_rating
        
def get_most_watched_genre(user_data):

    watched_movie = user_data.get('watched',[])
    
    genre_count = {}
    most_watched_genre = ""
    max_count = 0
     
    for movie in watched_movie:
        genre = movie.get('genre', None)

        if genre:
            if genre not in genre_count:
                genre_count[genre] = 0
            else:           
                genre_count[genre] += 1

        if genre_count[genre] > max_count:
            max_count = genre_count[genre]
            most_watched_genre = genre

    if watched_movie == []:
        return None

    return most_watched_genre
        
               
# ------------- WAVE 3 --------------------

def get_unique_watched(user_data):
    user_unique_watched_movies = []
    watched_movie = user_data.get('watched',[])
    friends = user_data.get('friends',[])
   
    friends_watched_titles = []
    for friend in friends:
        for friend_movie in friend.get('watched', []):
            friends_watched_titles.append(friend_movie['title'])
    for movie in watched_movie:
        if movie['title'] not in friends_watched_titles:
            user_unique_watched_movies.append(movie)    
    return user_unique_watched_movies



        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

