HORROR_1 = {
    "title": "MOVIE_TITLE_1",
    "genre": "GENRE_1",
    "rating": "RATING_1"
}
FANTASY_1 = {
    "title": "The Lord of the Functions: The Fellowship of the Function",
    "genre": "Fantasy",
    "rating": 4.8
}
FANTASY_2 = {
    "title": "The Lord of the Functions: The Two Parameters",
    "genre": "Fantasy",
    "rating": 4.0
}
FANTASY_3 = {
    "title": "The Lord of the Functions: The Return of the Value",
    "genre": "Fantasy",
    "rating": 4.0
}
FANTASY_4 = {
    "title": "The Programmer: An Unexpected Stack Trace",
    "genre": "Fantasy",
    "rating": 4.0
}
ACTION_1 = {
    "title": "The JavaScript and the React",
    "genre": "Action",
    "rating": 2.2
}
ACTION_2 = {
    "title": "2 JavaScript 2 React",
    "genre": "Action",
    "rating": 4.2
}
ACTION_3 = {
    "title": "JavaScript 3: VS Code Lint",
    "genre": "Action",
    "rating": 3.5
}
INTRIGUE_1 = {
    "title": "Recursion",
    "genre": "Intrigue",
    "rating": 2.0
}
INTRIGUE_2 = {
    "title": "Instructor Student TA Manager",
    "genre": "Intrigue",
    "rating": 4.5
}
INTRIGUE_3 = {
    "title": "Zero Dark Python",
    "genre": "Intrigue",
    "rating": 3.0
}
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


def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            break 
    return user_data
 
    
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    
    total_ratings = 0
    number_of_movies = 0
    for movie in user_data["watched"]:
        total_ratings += movie["rating"]
        number_of_movies += 1
        average_rating = total_ratings / number_of_movies
        
    if number_of_movies == 0:
        return 0.0
    return average_rating


# determin most frequent occurence in the watchlist
# key == "genre" a str
# return most frequent watched
# if value of "watched" == empty list get_most_watched_genre return None 
def get_most_watched_genre(user_data):
    
    if user_data['watched'] == []:
        return None
    
    count_genres = {}
    
    for movie in user_data["watched"]:
        genre = movie["genre"]
        print("******move genre*******")
        print(genre)
        if genre in count_genres:
            count_genres[genre] +=1
            print("plus one  of genres******")
            print(count_genres)
        else:
            count_genres[genre] =1
        
          
    most_watched = max(count_genres, key= count_genres.get)
    print("!!! most watched !!!11")
    return most_watched
      
           
          
           
       
        
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    user_watched_movies = user_data["watched"][:]
    friends = user_data["friends"]

    for friend in friends:
        for movie in friend["watched"]:
            if movie in user_watched_movies:
                user_watched_movies.remove(movie)
    return user_watched_movies

def get_friends_unique_watched(user_data):
    user_watched_movies = user_data["watched"]
    friends = user_data["friends"]
    unique_watched = []

    for friend in friends:
        for friend_movie in friend["watched"]:
            if friend_movie not in user_watched_movies and friend_movie not in unique_watched:
                unique_watched.append(friend_movie)
    return unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

