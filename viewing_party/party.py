# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {}
    if title and genre and rating:
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie
    else:
        return None
    
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data    

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)

    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    # an empty watched list is 0.0
    if not user_data["watched"]:
        return 0.0
    # caculate total rating
    total_rating = 0
    for movie in user_data["watched"]:
        total_rating += movie["rating"]

    avg_rating = total_rating / len(user_data["watched"])

    return avg_rating

def get_most_watched_genre(user_data):
    # an empty list return None
    if not user_data["watched"]:
        return None
    
    most_genre = {}
    # bulid a dict for genre count
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in most_genre:
            most_genre[genre] +=1
        else:
            most_genre[genre] =1
    # use max to find the most one
    return max(most_genre, key=most_genre.get)


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    friends_title = []
    # loop each friend
    for friend in user_data["friends"]:
        # check movies watched by friends
        for movie in friend["watched"]:
            # add movie titles to list
            friends_title.append(movie["title"])

    unique_watched = []

    for movie in user_data["watched"]:
        if movie["title"] not in friends_title:  
            unique_watched.append(movie) 

    return unique_watched

def get_friends_unique_watched(user_data):
    user_title = []
    for movie in user_data["watched"]:
        user_title.append(movie["title"])

    friends_unique_watched = []
    # through each friend's movie record
    for friend in user_data["friends"]: 
        # through every movie friends watched
        for watched_movie in friend["watched"]: 
            # check movie title is not in the list by the user and friends
            if watched_movie["title"] not in user_title\
            and watched_movie not in friends_unique_watched:
                    # if not, add movie to friend's uniquely 
                    friends_unique_watched.append(watched_movie)
            
    return friends_unique_watched


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    # build a empty recommendations
    recommendations = []
    # thourgh each movie 
    for movie in get_friends_unique_watched(user_data):
        # check if host in subscriptions
        if movie['host'] in user_data["subscriptions"]:
            # add that one in list
            recommendations.append(movie)

    return recommendations


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recommendations = []

    if get_most_watched_genre(user_data) is None:
        return recommendations
    
    for friend in user_data["friends"]:
        for watched_movie in friend["watched"]:
            if watched_movie not in user_data["watched"]:
                if watched_movie["genre"] in get_most_watched_genre(user_data):
                    if watched_movie not in recommendations:
                        recommendations.append(watched_movie)
    return recommendations

def get_rec_from_favorites(user_data):
    recommendations = []
    friends_title = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_title.append(movie["title"])

    for movie in user_data["favorites"]: 
        if movie["title"] not in friends_title :
            recommendations.append(movie)
    return recommendations