# ------------- WAVE 1 --------------------
# create dictionary with following key value pairs. 
import pprint


def create_movie(title, genre, rating):
    if title is None: 
        return None
    elif genre is None: 
        return None
    elif rating is None: 
        return None
    movie_dictionary= {"title": title, "genre": genre, "rating": rating }
    return movie_dictionary


def add_to_watched(user_data,movie):
    watched_list=user_data["watched"]
    watched_list.append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    watch_list=user_data["watchlist"]
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
    if watched_movies == []:
        return None
    for movie in watched_movies:
        genre = movie["genre"]
        if genre not in genre_dict.keys():
            genre_dict.update({genre:1})
        else: 
            genre_dict[genre] += 1
    for genre_name, genre_count in genre_dict.items(): 
        if top_genre is None: 
            top_genre = genre_name
            top_genre_count = genre_count
        elif genre_count > top_genre_count: 
            top_genre = genre_name
        else: 
            continue
    return top_genre
        

        
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_watched = []
    my_movies = user_data.get("watched")
    friends_movie_list = join_friends_list(user_data)

    for my_movie in my_movies:
        if my_movie not in friends_movie_list and my_movie not in unique_watched:
            unique_watched.append(my_movie)

    return unique_watched
    

def get_friends_unique_watched(user_data):
    unique_watched = []
    my_movies = user_data.get("watched")
    friends_movie_list = join_friends_list(user_data)

    for friends_movie in friends_movie_list:
        if friends_movie not in my_movies and friends_movie not in unique_watched:
                unique_watched.append(friends_movie)
    return unique_watched

def join_friends_list(user_data):
    friends_list = user_data.get("friends")
    friends_movie_list = []
    for friend in friends_list:
        for movie in friend["watched"]:
            friends_movie_list.append(movie)
    return friends_movie_list


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
    joined_friends_list = join_friends_list(user_data)
    if user_data["watched"] == [] or joined_friends_list == []:
        return new_rec_by_genre
    

    most_watched_genre = get_most_watched_genre(user_data)
    unreviewed_recs = get_available_recs(user_data)
    for movie in unreviewed_recs:
        movie_genre = movie["genre"]
        if movie_genre == most_watched_genre:
            new_rec_by_genre.append(movie)

    return new_rec_by_genre

def get_rec_from_favorites(user_data):
    favorites = user_data["favorites"]
    joined_friends_list = join_friends_list(user_data)
    rec_from_favorites_list = []

    print(joined_friends_list)
    for movie in favorites:
        if movie not in joined_friends_list: 
            rec_from_favorites_list.append(movie)
            print(movie)

    return rec_from_favorites_list