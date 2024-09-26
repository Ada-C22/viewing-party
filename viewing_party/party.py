# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    if title and genre and rating:
        return {
            "title": title,
            "genre": genre,
            "rating": rating
        }
    else: 
        return None

def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data,  movie):

    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):

    for i in range(len(user_data["watchlist"])):
        if title == user_data["watchlist"][i]["title"]:
            user_data["watched"].append(user_data["watchlist"][i])
            user_data["watchlist"].remove(user_data["watchlist"][i])

    return user_data
        

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):

    watched_movies = user_data.get("watched", [])

    if not watched_movies:
        return 0.0
    
    total_rating = 0.0
    all_movies = len(watched_movies)

    for movie in watched_movies:
        total_rating += movie["rating"]

    avg_rating = total_rating / all_movies

    return avg_rating

def get_most_watched_genre(user_data):

    most_watched_genre = user_data.get("watched", [])

    if not most_watched_genre:
        return None
    
    all_genre = {}

    for item in most_watched_genre:
        genre = item.get("genre")
        if genre in all_genre:
            all_genre[genre] += 1
        else:
            all_genre[genre] = 1

    most_watched = None
    highest_count = 0

    for genre, count in all_genre.items():
        if count > highest_count:
            highest_count = count
            most_watched = genre

    return most_watched
    

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):

    user_watched = user_data["watched"]
    user_watched_titles = set()

    for movie in user_watched:
        user_watched_titles.add(movie["title"])
    
    friends_watched_titles = set()

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_titles.add(movie["title"])

    unique_watched = []

    for movie in user_watched:
        if movie["title"] not in friends_watched_titles:
            unique_watched.append(movie)

    return unique_watched

def get_friends_unique_watched(user_data):

    user_watched_titles = set()
    for movie in user_data["watched"]:
        user_watched_titles.add(movie["title"])
    
    friends_watched_titles = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_titles.add(movie["title"])

    friends_unique_watched = []
    friends_unique_watched_titles = friends_watched_titles - user_watched_titles
    
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie['title'] in friends_unique_watched_titles:
                friends_unique_watched.append(movie)
                friends_unique_watched_titles.remove(movie['title'])
    
    return friends_unique_watched
                
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):

    recommended_movies = []
    unique_movies = get_friends_unique_watched(user_data)
    
    for unique_movie in unique_movies:
        for subscription in user_data["subscriptions"]:
            if subscription == unique_movie["host"]:
                recommended_movies.append(unique_movie)
    
    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):

    most_watched_genre = get_most_watched_genre(user_data)
    friends_unique_watched_list = get_friends_unique_watched(user_data)
    new_rec_by_genre = []

    if not user_data["watched"]:
        return new_rec_by_genre

    for movie in friends_unique_watched_list:
        if movie["genre"] in most_watched_genre:
            new_rec_by_genre.append(movie)

    return new_rec_by_genre

def get_rec_from_favorites(user_data):
    unique_watched = get_unique_watched(user_data)
    fav_movies_list = user_data["favorites"]
    recommended_movies = []

    if not user_data["favorites"]:
        return recommended_movies
    
    for fav_movie in fav_movies_list:
        if fav_movie in unique_watched:
            recommended_movies.append(fav_movie)
            
    return recommended_movies





