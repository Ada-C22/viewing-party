# ------------- WAVE 1 --------------------
#
def create_movie(title, genre, rating):
    
    if title and genre and rating:
        return {
            "title": title,
            "genre": genre,
            "rating": rating,
        }
    else:
        return None
# print(create_movie("movie_title", "comedy", "5"))
# user_data:
# {"watched": [movies] 
#  "watchlist": [movies]} <-- add here a movie
# add movie to 'watched' list from the user dict

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data
   
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data
    # print(user_data)   

# usr = {
#         "watched": [
#             "FANTASY_1",    
#             "FANTASY_3",
#             "FANTASY_4",
#             "HORROR_1",
#         ]
#     ,
#         "watchlist": [
#             "FANTASY_2",
#             "ACTION_2",
#             "INTRIGUE_2",
#             "INTRIGUE_2",
#         ]
#     }

# add_to_watchlist( usr, "soe " )


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

