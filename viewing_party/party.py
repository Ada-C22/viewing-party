# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }

    if title is None or genre is None or rating is None:
        return None
    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    
    return user_data

def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data,title):
    for movies_to_watch in user_data["watchlist"]:
        if title == movies_to_watch["title"]:
            user_data["watched"].append(movies_to_watch)
            user_data["watchlist"].remove(movies_to_watch)
    
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):

    if len(user_data["watched"]) == 0:
        return 0.0
    sum_rating = 0.0
    for movie in user_data["watched"]:
        sum_rating += movie["rating"]   
    avg_rating = float(sum_rating/len(user_data["watched"]))

    return avg_rating

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None
    count_genre = {}
    
    for movie in user_data["watched"]:
        count_genre[movie["genre"]] = count_genre.get(movie["genre"],0) + 1
    
    max_count = 0
    popular_genre = None
    for gerne,count in count_genre.items():
        if count > max_count:
            popular_genre = gerne
            max_count = count
    
    return popular_genre
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_watched_by_user = []
    # Create a flat list of all movies watched by friends
    friend_watched_list = []
    
    for friends_watched in user_data["friends"]:
        for movie in friends_watched["watched"]:
            friend_watched_list.append(movie)
       
    for user_watched in user_data["watched"]:
        if user_watched not in friend_watched_list:
            unique_watched_by_user.append(user_watched)

    return unique_watched_by_user

def get_friends_unique_watched(user_data):
    unique_watched_by_friend = []

    for each_friend_watched in user_data["friends"]:
        for movie in each_friend_watched["watched"]:
            if movie not in user_data["watched"]:
                if movie not in unique_watched_by_friend:
                    unique_watched_by_friend.append(movie)
    
    return unique_watched_by_friend   
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
# INTRIGUE_3b["host"] = "disney+"

# USER_DATA_4 = {
#     "watched": [
#         FANTASY_1b, 
#         FANTASY_2b, 
#         FANTASY_3b, 
#         ACTION_1b, 
#         INTRIGUE_1b, 
#         INTRIGUE_2b
#         ],  
#     "friends":  [
#         {
#             "watched": [
#                 FANTASY_1b,
#                 FANTASY_3b,
#                 FANTASY_4b,
#                 HORROR_1b,
#             ]
#         },
#         {
#             "watched": [
#                 FANTASY_1b,
#                 FANTASY_4b,
#                 ACTION_1b,
#                 INTRIGUE_1b,
#                 INTRIGUE_3b,
#             ]
#         }  
#     ]
# }

# USER_DATA_4["subscriptions"] = ["netflix", "hulu"] 
def get_available_recs(user_data):
    recommended_movie_list = []
    user_watched_titles = {movie["title"] for movie in user_data["watched"]}
    
    for friends_watched_list in user_data["friends"]:
        for movie in friends_watched_list["watched"]:
            if (movie["title"] not in user_watched_titles and 
                movie["host"] in user_data["subscriptions"]
                and movie not in recommended_movie_list):
                recommended_movie_list.append(movie)

    return recommended_movie_list

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

