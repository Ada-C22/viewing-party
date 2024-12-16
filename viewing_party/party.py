# ------------- WAVE 1 --------------------
# create dictionary with following key value pairs. 
import pprint
import operator as op


def create_movie(title, genre, rating):
    if not validate_data(title,str):
        return None
    if not validate_data(genre,str):
        return None
    if not validate_data(rating,float):
        return None
    movie_dictionary = {"title": title, "genre": genre, "rating": rating }
    return movie_dictionary


def add_to_watched(user_data,movie):
    watched_list = user_data["watched"]
    watched_list.append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    watch_list = user_data["watchlist"]
    watch_list.append(movie)
    return user_data
    pass

def watch_movie(user_data, movie):
    watch_list = user_data["watchlist"]
    print("watch list :", user_data["watchlist"])
    print("watched list :", user_data["watched"])
    watched_list = user_data["watched"]

    for to_watch_movie in watch_list: 
        movie_name = to_watch_movie["title"]
        if movie_name == movie:
            watch_list.remove(to_watch_movie)
            watched_list.append(to_watch_movie)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    watched_movies = user_data["watched"]
    count_movies_watched = len(watched_movies)
    sum_ratings = 0
    if count_movies_watched == 0: 
        return 0.0
    for movie in watched_movies:
        movie_rating = movie["rating"]
        sum_ratings += movie_rating
    return sum_ratings / count_movies_watched

def get_most_watched_genre(user_data):
    genre_dict = {}
    watched_movies = user_data["watched"]
    top_genre = None
    top_genre_count = 0
    for movie in watched_movies:
        genre = movie["genre"]
        if genre not in genre_dict.keys():
            genre_dict.update({genre:1})
        else: 
            genre_dict[genre] += 1
    for genre_name, genre_count in genre_dict.items(): 
        if genre_count > top_genre_count: 
            top_genre = genre_name
            top_genre_count = genre_count
    return top_genre
        

        
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_watched = []
    my_movies = user_data.get("watched")
    for my_movie in my_movies:
        found = False
        for friend in user_data.get("friends"):
            if my_movie in friend.get("watched"):
                found = True
        if found == False:
            unique_watched.append(my_movie)
    
    return unique_watched
    

def get_friends_unique_watched(user_data):
    unique_watched = []
    my_movies = user_data.get("watched")
    
    for friends in user_data.get("friends"):
        for friend_movie in friends.get("watched"):
            if friend_movie not in my_movies and friend_movie not in unique_watched: 
                unique_watched.append(friend_movie)
    
    return unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    movie_recs = []
    unique_movies=get_friends_unique_watched(user_data)
    for movie in unique_movies:
        movie_host = movie.get("host")
        if movie_host in user_data["subscriptions"]:
            movie_recs.append(movie)
    return movie_recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    new_rec_by_genre = []
    if user_data["watched"] == []:
        return new_rec_by_genre
    most_watched_genre = get_most_watched_genre(user_data)
    unreviewed_recs = get_friends_unique_watched(user_data)
    for movie in unreviewed_recs:
        movie_genre = movie["genre"]
        if movie_genre == most_watched_genre:
            new_rec_by_genre.append(movie)
    return new_rec_by_genre

def get_rec_from_favorites(user_data):
    favorites = user_data["favorites"]
    unique_watched = get_unique_watched(user_data)
    unique_watched_set = set()
    for movie in unique_watched:
        unique_watched_set.add(movie["title"])
    rec_from_favorites_list = []
    for favorite_movie in favorites:
        if favorite_movie["title"] in unique_watched_set:
            rec_from_favorites_list.append(favorite_movie)

    return rec_from_favorites_list

def validate_data(data_input,type_needed):
    data_type = type(data_input)
    if data_type != type_needed: 
        return False
    return True