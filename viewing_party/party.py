# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {}

    if not title or not genre or not rating:
        print(None)
        return None
    else:
        movie_dict['title'] = title
        movie_dict['genre'] = genre
        movie_dict['rating'] = rating
        print(movie_dict)
    
    return movie_dict


def add_to_watched(user_data, movie):
    # user_data 
    # empty list = no movies wathced
    # user_data = {
    #     "watched" : [
    #         {
    #             "title": "Title A",
    #             "genre": "Horror",
    #             "rating": 3.5
    #         },
    #         {
    #             "title": "Title A",
    #             "genre": "Horror",
    #             "rating": 3.5
    #         },
    #         {
    #             "title": "Title A",
    #             "genre": "Horror",
    #             "rating": 3.5
    #         }
    #     ]
    # }
    # return the user_data

    user_data = {
        "watched": []
    }

    user_data["watched"].append(movie)

    # print(user_data)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data = {
        "watchlist": []
    }

    user_data["watchlist"].append(movie)

    # print(user_data)
    return user_data

def watch_movie(user_data, title):
    pass

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

