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
    temp_user_data = copy.deepcopy(user_data)
    watch_list = temp_user_data["watchlist"]
    watched = temp_user_data["watched"]
    test = False

    for i in range(0, len(user_data["watchlist"])):
        watch_list_title = watch_list[i]["title"]
        if watch_list_title == title:
          watched.append(watch_list[i])
          test = i

    if test:
        del watch_list[test]

    return temp_user_data


# janes_data = {
#     "watchlist": [{
#         "title": "MOVIE_TITLE_1",
#         "genre": "GENRE_1",
#         "rating": "RATING_1"
#     },{
#         "title": "MOVIE_TITLE_2",
#         "genre": "GENRE_1",
#         "rating": "RATING_1"
#     }],

#     "watched": []
# }

# updated_data = watch_movie(janes_data, "MOVIE_TITLE_1")

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
