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
    




pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    
]

