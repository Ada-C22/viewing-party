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
    
    for movie in user_data["watched"]:
        ratings_total += movie["rating"]
        num_of_ratings += 1
    
    return ratings_total/num_of_ratings
    

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_movies = []
# loop through each user movie
    for user_movie in user_data["watched"]:
        is_movie_unique = True

# loop through each friend
        for friend in user_data["friends"]:
            # loop through each friend movie
            for friend_movie in friend["watched"]:
                # check if friend movie matches user movie
                if user_movie["title"] == friend_movie["title"]:
                    is_movie_unique = False
# if movie is unique after loop then add movie to unique movie list
        if is_movie_unique:
            unique_movies.append(user_movie)

    return unique_movies


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

