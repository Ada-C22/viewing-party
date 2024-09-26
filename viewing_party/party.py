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
    
    #count occurences of each genre
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
        
               
               
    


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

a = {'watched': [{'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8}, 
             {'title': 'The Lord of the Functions: The Two Parameters', 'genre': 'Fantasy', 'rating': 4.0}, 
             {'title': 'The Lord of the Functions: The Return of the Value', 'genre': 'Fantasy', 'rating': 4.0}, 
             {'title': 'The JavaScript and the React', 'genre': 'Action', 'rating': 2.2}, 
             {'title': 'Recursion', 'genre': 'Intrigue', 'rating': 2.0}, 
             {'title': 'Instructor Student TA Manager', 'genre': 'Intrigue', 'rating': 4.5}],
  'friends': [
    {'watched': [
        {'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8}, 
        {'title': 'The Lord of the Functions: The Return of the Value', 'genre': 'Fantasy', 'rating': 4.0}, 
        {'title': 'The Programmer: An Unexpected Stack Trace', 'genre': 'Fantasy', 'rating': 4.0}, 
        {'title': 'It Came from the Stack Trace', 'genre': 'Horror', 'rating': 3.5}]}, 
    {'watched': [
        {'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8}, 
        {'title': 'The JavaScript and the React', 'genre': 'Action', 'rating': 2.2}, 
        {'title': 'Recursion', 'genre': 'Intrigue', 'rating': 2.0}, 
        {'title': 'Zero Dark Python', 'genre': 'Intrigue', 'rating': 3.0}]
        }
    ]
}

#get a list of title in watched 
#get a list of title in friends 
#compare two list




def get_friends_unique_watched(user_data):
    friends_unique_watched = {}
    

   
    user_watched_movie = user_data.get('watched',[])
    print(user_watched_movie)

    #for movie in user_data['watched']:
    #    user_watched_movie_titles.append(movie['title'])
    
    #print(user_watched_movie_titles)

    print("---------")

    friends_watched_movie_titles = []
    for movie in user_data['friends']:
        #friends_watched_movie_titles.append(movie['title'])
        friends_watched_movie = movie['watched']
    
    friends_unique_watched = set(friends_watched_movie) - set(user_watched_movie)

    print("---------")
    print(friends_watched_movie)
    
    

   
    
    return friends_unique_watched
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

