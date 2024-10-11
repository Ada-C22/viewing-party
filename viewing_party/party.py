# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
# if falsy return none
    if not title or not genre or not rating:
        return None
    
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
    
    ratings_total = 0

    for movie in user_data["watched"]:
        ratings_total += movie["rating"]
    
    return ratings_total/len(user_data["watched"])

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

#HELPER FUNCTION: creates list of movies friends have watched without any duplicate code#
def get_friends_movies(user_data):
        #loops through values of key 'friends' in user data, and friends_movies is added to movies_all_friends_watched set to make sure each movie is unique
    movies_all_friends_watched = []

    for friends_movies in user_data["friends"]:
        for movie in friends_movies["watched"]:
            if movie not in movies_all_friends_watched:
                movies_all_friends_watched.append(movie)

    return movies_all_friends_watched


def get_unique_watched(user_data):
    user_movies_list = []
    total_friends_movies_watched = get_friends_movies(user_data)
    
    #loops through values of key 'watched' in user_data to get movies watched
    for user_movies in user_data["watched"]:
        if user_movies not in total_friends_movies_watched:
            user_movies_list.append(user_movies)
    
    return user_movies_list


def get_friends_unique_watched(user_data):
    unique_movies_list = []
    total_friends_watched = get_friends_movies(user_data)
    
    #loops through movies in the total_friends_watched list to compare (in the if statement) if the movie is not in the user's watched list and hasn't appeared in the unique_movies_list (checks for duplicates) to then append the unique movie
    for movies in total_friends_watched:
        if movies not in user_data["watched"]:
            unique_movies_list.append(movies)
    
    return unique_movies_list

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    #calling get_friends_unique_watched from wave 3 
    unique_movies_from_friends = get_friends_unique_watched(user_data)
    recommendations = []

    for movies in unique_movies_from_friends:
        if movies["host"] in user_data["subscriptions"]:
            recommendations.append(movies)
    return recommendations


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    #use existing function (get_most_watched_genre) to get the user's most frequently watched genre
    most_frequent_genre = get_most_watched_genre(user_data)

    #use existing function (get_friends_unique_watched) to get friends most frequently watched movies
    unique_movies_from_friends = get_friends_unique_watched(user_data)
    recommendations = []

    if not most_frequent_genre:
        return []
    
    #iterates through list of movies by most watched genre
    for movies in unique_movies_from_friends:
        if movies["genre"] == most_frequent_genre:
            recommendations.append(movies)
    return recommendations


def get_rec_from_favorites(user_data):
    #use existing function (get_unique_watched) to get user's watched movies
    unique_watched_movies = get_unique_watched(user_data)
    recommendations = []

    #iterates through user's favorite movies in unique_watched_movies 
    for movies in user_data["favorites"]:
        if movies in unique_watched_movies:
            recommendations.append(movies)
    return recommendations