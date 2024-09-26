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

    user_data["watched"].append(movie)

    #print(user_data)
    return user_data

# print(add_to_watched(user_data, movie))

print(add_to_watched({"watched": []}, {
                                        "title": "Happy Feet",
                                        "genre": "Drama",
                                        "rating": 5
                                    }))


def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)

    # print(user_data)
    return user_data




    exa_data = {
        "watchlist": [
            {
            }
        ],
        "watched": [
            {
            }
        ]
    }

    exa_data["watchlist"] == 0


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
    #if there are no movies then return 0.0
    #find average of ratings 
  
    if not user_data["watched"]:
        return 0.0
    
    total_rating = 0
    for movie in user_data["watched"]:
        total_rating += movie["rating"] 
            
    average = total_rating / len(user_data["watched"])

    return average

  #find the most watched genre 
def get_most_watched_genre(user_data):
    genre_count = {"Fantasy": 0, "Intrigue": 0, "Action": 0} #change method so that other genres can be included

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

# def get_unique_watched(user_data):

    #user_data = {watched: [movies{}]}
    #return a list of dictionaries that represents a list of movies 
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_functions(user_data):
    
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

