
# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}
    if not title or not genre or not rating:
        return None
    else:
        new_movie ["title"] = title
        new_movie ["genre"] = genre
        new_movie ["rating"] = rating
    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"] += [movie]
    return user_data
    
def add_to_watchlist(user_data, movie):
    user_data["watchlist"] += [movie]
    return user_data

def watch_movie(user_data, title):
    for data in user_data["watchlist"]:
        if data["title"] == title:
            user_data["watchlist"].remove(data)
            user_data["watched"].append(data)
            break
    return user_data
    
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum_ratings = 0 
    if len(user_data["watched"]) == 0:
        return 0
    for watched_movie in user_data["watched"]: 
        sum_ratings += watched_movie["rating"]
    return sum_ratings / len(user_data["watched"])

def get_most_watched_genre(user_data):
    genre_dict = {}
    for movie in user_data["watched"]:
        if movie["genre"] in genre_dict:
            genre_dict[movie["genre"]] += 1
        else:
            genre_dict[movie["genre"]] = 1

    most_common_genre = None
    most_common_count = 0 

    for movie_genre, count in genre_dict.items():
        if count > most_common_count:
            most_common_genre = movie_genre
            most_common_count = count

    return most_common_genre



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def is_movie_watched_by_friend(user_watched_movie, friends):
    for friend in friends:
        for friend_watched_movie in friend["watched"]:
            if user_watched_movie["title"].lower() == friend_watched_movie["title"].lower():
                return True
    return False

def is_movie_watched_by_user(friend_watched_movie, user_watched_movies_list):
    for user_watched_movie in user_watched_movies_list:
        if user_watched_movie["title"].lower() == friend_watched_movie["title"].lower():
                return True
    return False

def is_movie_in_movie_list(movie_title, movie_dict_list):
    for movie_dict in movie_dict_list:
        if movie_title.lower() == movie_dict["title"].lower():
            return True
    return False

def get_unique_watched(user_data):
    watched_list = user_data["watched"]
    friends = user_data["friends"]
    movies_watched_by_user_only_list = []

    for watched_movie in watched_list:
        if is_movie_in_movie_list(watched_movie["title"], movies_watched_by_user_only_list):
            continue
        if not is_movie_watched_by_friend(watched_movie, friends):
            movies_watched_by_user_only_list.append(watched_movie)
    
    return movies_watched_by_user_only_list

def get_friends_unique_watched(user_data):
    watched_list = user_data["watched"]
    friends = user_data["friends"]
    movies_watched_by_friend_only_list = []

    for friend in friends:
        for friend_watched_movie in friend["watched"]:
            if is_movie_in_movie_list(friend_watched_movie["title"], movies_watched_by_friend_only_list):
                continue
            if not is_movie_watched_by_user(friend_watched_movie, watched_list):
                    movies_watched_by_friend_only_list.append(friend_watched_movie)
    
    return movies_watched_by_friend_only_list

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------


def get_available_recs(user_data):
    recommendations = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie in recommendations:
                continue
            
            elif movie in user_data["watched"]:
                continue
            
            elif movie["host"] not in user_data["subscriptions"]:
                continue
            
            else: 
                recommendations.append(movie)

    return recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    
    favorite_genre = get_most_watched_genre(user_data)
    
    recommended_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["genre"] != favorite_genre: 
                continue
            
            elif movie in recommended_movies:
                continue

            elif movie in user_data["watched"]:
                continue

            else: 
                recommended_movies.append(movie)
    return recommended_movies

