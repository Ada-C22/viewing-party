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

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

