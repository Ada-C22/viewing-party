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
    # use the .get() method to get the watched list from user_data
    # check to see if the list is empty then return 0.0
    # initialize the total rating and count all movies in the dict
    # loop through each movies in watched_movies to get the ratings
    # add each rating to total_rating
    # calculate the average rating by dividing the total rating by the movie counts
    # return the average rating 

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
    # get the list of titles that the user has watched
    # create a set for titles friends have watched
    # find unique movies friends have watched that the user hasn't watched
    # initialized an empty set to store the titles that the user has watched
    # use for loop to iterate over each movie dicts in the "watched" list
    user_watched_titles = set()
    for movie in user_data["watched"]:
        user_watched_titles.add(movie["title"])
    
    #initialize an empty set to store the movie titles friends have watched
    # use for loop to literate over each friend in the list "friends" in the dict
    # use another for loop to iterate over each movie in the "watched" dict in friends list
    # then add the movie titles to the set
    friends_watched_titles = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_titles.add(movie["title"])

    # initilize ab enpty list to store the unique movies
    # use for loop to iterate over each title in friends_watched_titles
    # check if the title is not in user_watched_titles
    # break once the movie/movies are found
    # unique_friends_watched = []
    # for title in friends_watched_titles:
    #     if title not in user_watched_titles:
    #         for friend in user_data["friends"]:
    #             for movie in friend["watched"]:
    #                 if movie["title"] == title:
    #                     unique_friends_watched.append(movie)
    #                     break     
    
    # return unique_friends_watched


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

