# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
# if falsy return none
    if not title or not genre or not rating:
        return None
    
# check if parameters are truthy and if so return empty_dict
    return {
        "title": title,
        "genre": genre,
        "rating": rating
    }

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    # Loop through watchlist dict
    for movie in user_data["watchlist"]:
        # check if the tile of movie is in the user_data dict
        if title == movie["title"]:
            # remove the movie from watchlist if user already watched it
            user_data["watchlist"].remove(movie)
            # add movie to watched list if user already watched it
            user_data["watched"].append(movie)
            break # exit the loop once movie is found and moved
    return user_data # return updated dict

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0.0
    
    num_of_ratings = 0
    ratings_total = 0
        
    # for i in range(len(user_data["watched"][0])):
    #     num_of_ratings += 1
    #     ratings_total += user_data["watched"][0]["rating"]

    for movie in user_data["watched"]:
        ratings_total += movie["rating"]
        num_of_ratings += 1
    
    return ratings_total/num_of_ratings

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    
    genre_frequency = {}

    #first for loop tracks amount of times a genre appears
    for movie in user_data["watched"]:
        genre_type = movie["genre"]
        if genre_type in genre_frequency:
            genre_frequency[genre_type] += 1
        else:
            genre_frequency[genre_type] =1
    
    most_watched_genre = None
    highest_genre_count = 0

    #second for loop picks out which genre is the most watched
    for genre, count in genre_frequency.items():
        if count > highest_genre_count:
            highest_genre_count = count
            most_watched_genre = genre

    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_movies_list = []
    total_friends_watched = []

    for movies in user_data["friends"]:
        total_friends_watched += movies["watched"]

    for unique_movies in user_data["watched"]:
        if unique_movies not in total_friends_watched:
            unique_movies_list.append(unique_movies)
    
    return unique_movies_list


def get_friends_unique_watched(user_data):
    unique_movies_list = []
    total_friends_watched = []

    for movies in user_data["friends"]:
        total_friends_watched += movies["watched"]
    
    for unique_movies in total_friends_watched:
        if (unique_movies not in user_data["watched"]) and (not unique_movies in unique_movies_list):
            unique_movies_list.append(unique_movies)
    
    return unique_movies_list

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

