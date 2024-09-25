import copy
#----------WAVE01-------------
MOVIE_TITLE_1 = "It Came from the Stack Trace"
GENRE_1 = "Horror"
RATING_1 = 3.5

#----------WAVE02-------------
HORROR_1 = {
    "title": MOVIE_TITLE_1,
    "genre": GENRE_1,
    "rating": RATING_1
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
USER_DATA_2 = {
    "watched": [
        FANTASY_1, 
        FANTASY_2, 
        FANTASY_3, 
        ACTION_1, 
        INTRIGUE_1, 
        INTRIGUE_2
        ],    
}

USER_DATA_2b = {
    "watched": [
        INTRIGUE_1,
        FANTASY_2,
        ACTION_1,
        FANTASY_1,
        FANTASY_3,
        INTRIGUE_2,
    ]
}

#-----WAVE 3--------
USER_DATA_3 = copy.deepcopy(USER_DATA_2)
USER_DATA_3["friends"] =  [
        {
            "watched": [
                FANTASY_1,
                FANTASY_3,
                FANTASY_4,
                HORROR_1,
            ]
        },
        {
            "watched": [
                FANTASY_1,
                ACTION_1,
                INTRIGUE_1,
                INTRIGUE_3,
            ]
        }
    ]  

#-----WAVE 4--------

HORROR_1b = copy.deepcopy(HORROR_1)
FANTASY_1b = copy.deepcopy(FANTASY_1)
FANTASY_2b = copy.deepcopy(FANTASY_2)
FANTASY_3b = copy.deepcopy(FANTASY_3)
FANTASY_4b = copy.deepcopy(FANTASY_4)
ACTION_1b = copy.deepcopy(ACTION_1)
ACTION_2b = copy.deepcopy(ACTION_2)
ACTION_3b = copy.deepcopy(ACTION_3)
INTRIGUE_1b = copy.deepcopy(INTRIGUE_1)
INTRIGUE_2b = copy.deepcopy(INTRIGUE_2)
INTRIGUE_3b = copy.deepcopy(INTRIGUE_3)

HORROR_1b["host"] = "netflix"
FANTASY_1b["host"] = "netflix"
FANTASY_2b["host"] = "netflix"
FANTASY_3b["host"] = "amazon"
FANTASY_4b["host"] = "hulu"
ACTION_1b["host"] = "amazon"
ACTION_2b["host"] = "amazon"
ACTION_3b["host"] = "hulu"
INTRIGUE_1b["host"] = "hulu"
INTRIGUE_2b["host"] = "disney+"
INTRIGUE_3b["host"] = "disney+"

USER_DATA_4 = {
    "watched": [
        FANTASY_1, 
        FANTASY_2, 
        FANTASY_3, 
        ACTION_1, 
        INTRIGUE_1, 
        INTRIGUE_2
        ],  
    "friends":  [
        {
            "watched": [
                FANTASY_1,
                FANTASY_3,
                FANTASY_4,
                HORROR_1b,
            ]
        },
        {
            "watched": [
                FANTASY_1,
                FANTASY_4,
                ACTION_1,
                INTRIGUE_1,
                INTRIGUE_3,
            ]
        }  
    ]
}

USER_DATA_4["subscriptions"] = ["netflix", "hulu"]  


#----WAVE 5-----------

USER_DATA_5 = copy.deepcopy(USER_DATA_4)

USER_DATA_5["favorites"] = [
    FANTASY_1b, 
    FANTASY_2b, 
    INTRIGUE_1b,
    INTRIGUE_2b
    ]

#----Functions that return clean data for each test----

def clean_wave_2_data():
    return copy.deepcopy(USER_DATA_2)

def clean_wave_2b_data():
    return copy.deepcopy(USER_DATA_2b)

def clean_wave_3_data():
    return copy.deepcopy(USER_DATA_3)

def clean_wave_4_data():
    return copy.deepcopy(USER_DATA_4)

def clean_wave_5_data():
    return copy.deepcopy(USER_DATA_5)
# ------------- WAVE 1 --------------------

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

def get_most_watched_genre(user_data):
    
    if user_data['watched'] == []:
        return None
    
    count_genres = {}
    
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in count_genres:
            count_genres[genre] +=1
        else:
            count_genres[genre] =1
              
    most_watched = max(count_genres, key= count_genres.get)
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

def get_available_recs(user_data):
           
    recommended_title = []
    
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie["host"] in user_data["subscriptions"]:
                if movie not in recommended_title:
                    recommended_title.append(movie)
    return recommended_title
                  
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    rec_pool = get_friends_unique_watched(user_data)
    user_watched = user_data["watched"]
    genre_count = dict()

    for movie in user_watched:
        if movie["genre"] in genre_count:
            genre_count[movie["genre"]] += 1
        else:
            genre_count[movie["genre"]] = 1
    
    fav_genre = ""
    fav_genre_count = 0
    for genre, count in genre_count.items():
        if count > fav_genre_count:
            fav_genre = genre
            fav_genre_count = count

    recommendations = []
    for movie in rec_pool:
        if movie["genre"] == fav_genre:
            recommendations.append(movie)
    return recommendations

def get_rec_from_favorites(user_data):


    favorites = user_data["favorites"]

    friends_watched = get_friends_unique_watched(user_data)    
    print(f"{favorites=}", "\n")
    print(f"{friends_watched=}", "\n")

    for movie in friends_watched:
        if movie in favorites:
            favorites.remove(movie)
    
    print(f"{favorites=}", "\n")
    return favorites

print(get_rec_from_favorites(USER_DATA_5))



