from typing import Any, Callable, List, Tuple
from match import match
from database import *

# Database doesn't store this sort of publisher information, but these stay until I make one that does work
# def games_by_publisher(matches: List[str]):
#     input = matches[0].lower()
#     input = input.replace(" ", "-")
#     return get_games("publishers=" + input)

# def publisher_by_game(matches: List[str]):
#     input = matches[0].lower()
#     input = input.replace(" ", "-")
#     results = get_games("search=\"" + input + "\"") #Gets a list of games with the input name
#     firstResult = get_game(results["results"][0]["id"]) #Gets the 
#     return firstResult["publisher"] #Gets the publisher of the first result

def esrb_rating_by_game(matches: List[str]):
    """Takes a list of one item, a game, and prints its ESRB rating
    
    Args:
        matches - One string, the name of a game
    
    Returns:
        None
    
    """
    input = matches[0].lower()
    input = input.replace(" ", "-")
    results = get_games("search=\"" + input + "\"") #Gets a list of games with the input name
    firstResult = get_game(results["results"][0]["id"]) #Gets the first result
    print(firstResult["esrb_rating"]["name"])
    
    




pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("What is the ESRB rating for %"), esrb_rating_by_game)
]

