from typing import Any, Callable, List, Tuple
from match import match
from database import *

def developers_by_game(matches: List[str]): # Doesn't work. From research, ID is pk. But that would mean this should work.
    input = matches[0].lower()
    input = input.replace(" ", "-")
    search_result = get_games(f"search=\"{input}\"")["results"][0]
    developers = request(f"/games/{search_result['id']}/development-team?key={KEY}")
    print(developers)


def description_by_game(matches: List[str]):
    input = matches[0].lower()
    input = input.replace(" ", "-")
    results = get_games("search=\"" + input + "\"") # Gets a list of games with the input name
    firstResult = get_game(results["results"][0]["id"]) # Gets the first result
    print_game_details(firstResult)


def platforms_by_game(matches: List[str]):
    input = matches[0].lower()
    input = input.replace(" ", "-")
    results = get_games("search=\"" + input + "\"") # Gets a list of games with the input name
    firstResult = get_game(results["results"][0]["id"]) # Gets the first result
    platforms = get_platforms(firstResult)
    print(f"{firstResult['name']} can be played on {platforms}.")


def games_by_genre(matches: List[str]):
    input = matches[0].lower()
    input = input.replace(" ", "-")
    results = get_games("genres=" + input) # Gets a list of games with the input genre
    print_list_of_games(results)


def esrb_rating_by_game(matches: List[str]):
    """Takes a list of one item, a game, and prints its ESRB rating
    
    Args:
        matches - One string, the name of a game
    
    Returns:
        None
    
    """
    input = matches[0].lower()
    input = input.replace(" ", "-")
    results = get_games("search=\"" + input + "\"") # Gets a list of games with the input name
    firstResult = get_game(results["results"][0]["id"]) # Gets the first result
    name = firstResult["name"]
    rating = firstResult["esrb_rating"]
    if not rating:
        print(name + " does not have an official ESRB rating.")
        return
    print(name + " is rated " + rating["name"])


def rating_by_game(matches:List[str]):
    """Takes a list of one item, a game, and prints its rating (score)
    
    Args:
        matches - One string, the name of a game
    
    Returns:
        None
    
    """
    input = matches[0].lower()
    input = input.replace(" ", "-")
    results = get_games("search=\"" + input + "\"") # Gets a list of games with the input name
    firstResult = get_game(results["results"][0]["id"]) # Gets the first result
    print(firstResult["name"] + " has a rating of " + str(firstResult["rating"]) + " out of 5")


def playtime_by_game(matches: List[str]):
    """Takes a list of one item, a game, and prints its average playtime
    
    Args:
        matches - One string, the name of a game
    
    Returns:
        None
    
    """
    input = matches[0].lower()
    input = input.replace(" ", "-")
    results = get_games("search=\"" + input + "\"") # Gets a list of games with the input name
    firstResult = get_game(results["results"][0]["id"]) # Gets the first result
    print(firstResult["name"] + " has an average playtime of " + str(firstResult["playtime"]) + " hours")


def release_date_by_game(matches: List[str]):
    """Takes a list of one item, a game, and prints its release date
    
    Args:
        matches - One string, the name of a game
    
    Returns:
        None
    
    """
    input = matches[0].lower()
    input = input.replace(" ", "-")
    results = get_games("search=\"" + input + "\"") # Gets a list of games with the input name
    firstResult = get_game(results["results"][0]["id"]) # Gets the first result
    print(firstResult["name"] + " was released on " + firstResult["released"])


pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what is the esrb rating for %"), esrb_rating_by_game),
    (str.split("what is the rating for %"), rating_by_game),
    (str.split("what is % rated"), rating_by_game),
    (str.split("what is the average playtime for %"), playtime_by_game),
    (str.split("when was % released"), release_date_by_game),
    (str.split("what platforms are available for %"), platforms_by_game),
    (str.split("give me a list of games with the % genre"), games_by_genre),
    (str.split("what is %"), description_by_game),
    (str.split("describe %"), description_by_game),
    # (str.split("who developed %"), developers_by_game),
]

def search_pa_list(src: List[str]) -> List[str]:
    for pattern in pa_list:
        matched = match(pattern[0], src)
        if matched == None: continue
        return pattern[1](matched)
    return ["I don't understand"]


def query_loop() -> None:
    print("Welcome to the RAWG video game database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            search_pa_list(query)
        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")


query_loop()
