# from tests.test_constants import *
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
        # print(movie_dict)
    
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

    user_data["watched"].append(movie)

    #print(user_data)
    return user_data

# print(add_to_watched(user_data, movie))

# print(add_to_watched({"watched": []}, {
#                                         "title": "Happy Feet",
#                                         "genre": "Drama",
#                                         "rating": 5
#                                     }))


def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)

    # print(user_data)
    return user_data

    # exa_data = {
    #     "watchlist": [
    #         {
    #         }
    #     ],
    #     "watched": [
    #         {
    #         }
    #     ]
    # }

    # exa_data["watchlist"] == 0


def watch_movie(user_data, title):

    # watchlist = add_to_watchlist(user_data, movie)
    # watched = add_to_watched(user_data, movie)

    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data
    
    return user_data
    

    #call function add_to_watched 
        #title is string
        #list of "watched movies"
    # if title is in watchlist add movie to watched and return user_data
    # if title is not on watchlist return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    #user_data = {"watched": []}
    if not user_data["watched"]:
        return 0.0
    
    total_rating = 0
    for movie in user_data["watched"]:
        total_rating += movie["rating"] 
            
    average = total_rating / len(user_data["watched"])

    return average


def get_most_watched_genre(user_data):
    genre_count = {"Fantasy": 0, "Intrigue": 0, "Action": 0}

    if not user_data["watched"]:
        return None 
    
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in genre_count:
            genre_count[genre] += 1   
    max_key = max(genre_count, key=genre_count.get)

    return max_key


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):


    movies_not_watched_by_friends = []

    for movie_watched_by_user in user_data["watched"]:
        watched_by_any_friend = False

        # checks if the movie is has been watched by a friend
        for friend in user_data["friends"]:
            if movie_watched_by_user in friend["watched"]:
                watched_by_any_friend = True
                break

        # If no friend has watched it, adds it to the final list
        if not watched_by_any_friend:
            movies_not_watched_by_friends.append(movie_watched_by_user)
    
    print(movies_not_watched_by_friends)
    return movies_not_watched_by_friends

def get_friends_unique_watched(user_data):

    # user_data = {
    #     "watched": [
    #         "FANTASY_1", 
    #         "FANTASY_2", 
    #         "FANTASY_3", 
    #         "ACTION_1", 
    #         "INTRIGUE_1", 
    #         "INTRIGUE_2"
    #         ],  
    #     "friends": [
    #         {
    #             "watched": [
    #                 "FANTASY_1",
    #                 "FANTASY_3",
    #                 "FANTASY_4",
    #                 "HORROR_1",
    #             ]
    #         },
    #         {
    #             "watched": [
    #                 "FANTASY_1",
    #                 "ACTION_1",
    #                 "INTRIGUE_1",
    #                 "INTRIGUE_3",
    #             ]
    #         }
    #     ]
    # }

    movies_watched_by_friends_not_user = []

    # Loops through each friend's watched list
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            # Appends to list if 1) movie is not in the user's watched list and 2) not already in the result list
            if movie not in user_data["watched"] and movie not in movies_watched_by_friends_not_user:
                movies_watched_by_friends_not_user.append(movie)
    
    return movies_watched_by_friends_not_user

# get_friends_unique_watched()
    
    #user_data = {watched: [movies{}]}
    #return a list of dictionaries that represents a list of movies 
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


