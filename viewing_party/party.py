# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    """
    Create a dictionary representing a movie
    
    Parameters:
        title(str): the title of movie
        genre (str): the genre of movie
        rating (float): the rating of movie
    
    Returns:
        dict: with keys "title", "genre", "rating" if all arguments are truthy
        None: if any of arguments are falsy
    """

    # Psuedocode: 
    if title or genre or rating is None:
        return None
    
    try:
        # Checking if user inputs on these parameters are all valid.
        title = str(title)
        genre = str(genre)
        rating = float(rating)
        
        return {"title": title, "genre": genre, "rating": rating}
        
    except ValueError and TypeError as e:
        print(e)
        return None
    
print(create_movie(None,"None", 3.5))
   
   
    
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

