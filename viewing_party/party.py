# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
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
    # if user_data["watchlist"][0]["title"] == title:
    #     user_data["watchlist"][0].pop(title)
    #     user_data["watched"].append(title)
    #     user_data["watchlist"] = []
    #     return user_data
    # return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    num_of_ratings = 0
    ratings_total = 0
    if not user_data["watched"]:
        return 0.0
        
    for i in range(len(user_data["watched"][0])):
        num_of_ratings += 1
        ratings_total += user_data["watched"][0]["rating"]
    
    return ratings_total/num_of_ratings
    

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

