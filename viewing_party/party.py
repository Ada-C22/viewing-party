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

    #loops through values of key 'friends' in user data, and is appended to total_friends_watched list
    for movies in user_data["friends"]:
        total_friends_watched += movies["watched"]

    #loops through values of key 'watched' in user_data to get movies watched
    for unique_movies in user_data["watched"]:
        #if statement compares movies in total_friends_watched list to what the user has watched, any unique movie gets appended to unique_movies_list
        if unique_movies not in total_friends_watched:
            unique_movies_list.append(unique_movies)
    
    return unique_movies_list


def get_friends_unique_watched(user_data):
    unique_movies_list = []
    total_friends_watched = []

    #loops through values of key 'friends' in user data, and is appended to total_friends_watched list
    for movies in user_data["friends"]:
        total_friends_watched += movies["watched"]
    
    #loops through movies in the total_friends_watched list to compare (in the if statement) if the movie is not in the user's watched list and hasn't appeared in the unique_movies_list (checks for duplicates) to then append the unique movie
    for unique_movies in total_friends_watched:
        if (unique_movies not in user_data["watched"]) and (not unique_movies in unique_movies_list):
            unique_movies_list.append(unique_movies)
    
    return unique_movies_list

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    # list titles of movies the user has already watched 
    user_watched_list = []
    for movie in user_data["watched"]:
        user_watched_list.append(movie["title"])
    
    # list that has rec movies
    recommendations = []

    # loop through each friend
    for friend in user_data["friends"]:
        # loop through their moviees
        for friend_movie in friend["watched"]:
            # check if user hasn't watched the movie and if host (streaming services) is also under user
            if (friend_movie["title"] not in user_watched_list and friend_movie["host"] in user_data["subscriptions"] and friend_movie not in recommendations):
                recommendations.append(friend_movie)

    return recommendations


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    #get user's most frequently watched genre
    genre_count = {}
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in genre_count:
            genre_count[genre] += 1
        else:
            genre_count[genre] = 1

# Find the most frequent genre
    most_frequent_genre = None
    max_count = 0

    for genre, count in genre_count.items():
        if count > max_count:
            most_frequent_genre = genre
            max_count = count
    if most_frequent_genre is None:
        return []
    
    # list of movies user has already watched
    user_watch = []
    for movie in user_data["watched"]:
        user_watch.append(movie["title"])
    
    #movie needs to be added to recommeneded list if they haven't watched it but one of their friends watched it
    recommended_list = []
    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            if friend_movie["genre"] == most_frequent_genre and friend_movie["title"] not in user_watch and friend_movie not in recommended_list:
                recommended_list.append(friend_movie)
    #returns list of recommended movies
    return recommended_list

def get_rec_from_favorites(user_data):
    # check friends movies
    friends_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie["title"])
    #add movie to list if it's user's favorite and not in friends list
    recommended_movies = []
    for favorite_movie in user_data["favorites"]:
        if favorite_movie["title"] not in friends_watched:
            recommended_movies.append(favorite_movie)    
    # return list of recommended movies
    return recommended_movies