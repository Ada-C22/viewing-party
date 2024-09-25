import copy
# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    new_movie = {
            "title": title,
            "genre": genre,
            "rating": rating
            }
    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    # for data in user_data.keys():
    #     user_data[data].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    # for data in user_data.keys():
    #     user_data[data].append(movie)

    return user_data


def watch_movie(user_data, title):

    watch_list = user_data["watchlist"]
    watched = user_data["watched"]

    for movie in watch_list:
        if isinstance(movie, list):
            #add Horror_1 "watched"
            #remove movie_to_watch "watchlist"
            if title in movie:
                watched.append(title)
                watch_list.remove(title)

        elif isinstance(movie, dict):
            if movie["title"] == title:
                watched.append(movie)
                watch_list.remove(movie)
                break
    print(user_data)    
    return user_data


HORROR_1 = {
    "title": "MOVIE_TITLE_1",
    "genre": "GENRE_1",
    "rating": "RATING_1"
}
movie_to_watch = HORROR_1
janes_data = {
        "watchlist": [
            "FANTASY_1",
            movie_to_watch
        ],
        "watched": ["FANTASY_2"]
    }

updated_data = watch_movie(janes_data, movie_to_watch["title"])

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
