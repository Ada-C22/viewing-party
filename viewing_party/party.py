# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    pass

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

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

