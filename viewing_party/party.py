
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



