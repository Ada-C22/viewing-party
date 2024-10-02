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
    for i in range(len(user_data["watchlist"])):
        item = user_data["watchlist"][i]

        if item["title"] == title:
            user_data["watched"].append(item)
            user_data["watchlist"].remove(item)

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
    friends_movie_title = set()

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movie_title.add(movie["title"])
    user_unique = []
    for movie in user_data["watched"]:
        if movie["title"] not in friends_movie_title:
            user_unique.append(movie)
    return user_unique

def get_friends_unique_watched(user_data):
    
    user_watched = {movie["title"] for movie in user_data["watched"]}
    
    friends_unique = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in user_watched and movie not in friends_unique:
                friends_unique.append(movie)
    
    return friends_unique
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommended_movies = []
    if "subscriptions" not in user_data or not user_data["subscriptions"]:
        return recommended_movies
        
    for movie in get_friends_unique_watched(user_data):
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
                    
    return recommended_movies
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    
    filtered_recommendations = []
    most_watched_genre = get_most_watched_genre(user_data)

    for movie in get_available_recs(user_data):
        if movie["title"] is None or movie["genre"] is None or movie["rating"] is None :
            return None
        elif movie["genre"] == most_watched_genre:
            filtered_recommendations.append(movie)
    return filtered_recommendations

def get_rec_from_favorites(user_data):

    if "favorites" not in user_data:
        return []
    recommended_movies = []
    for movie in get_unique_watched(user_data):
            if movie in user_data["favorites"]:
                recommended_movies.append(movie)
    return recommended_movies
