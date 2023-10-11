from typing import Any, Callable, List, Tuple
from match import match
from database import *

# Database doesn't store this sort of publisher information, but these stay until I make one that does work
def developers_by_game(matches: List[str]):
    input = matches[0].lower()
    input = input.replace(" ", "-")
    search_result = get_games(f"search=\"{input}\"")["results"][0]
    developers = request(f"/games/{search_result['id']}/development-team?key={KEY}")
    print(developers)


# def publisher_by_game(matches: List[str]):
#     input = matches[0].lower()
#     input = input.replace(" ", "-")
#     results = get_games("search=\"" + input + "\"") #Gets a list of games with the input name
#     firstResult = get_game(results["results"][0]["id"]) #Gets the 
#     return firstResult["publisher"] #Gets the publisher of the first result


pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("who developed %"), developers_by_game),
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
