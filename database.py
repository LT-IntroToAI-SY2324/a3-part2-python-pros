import http.client
import json

KEY = "7bbe453c5d1a4898943e72969588c96a"

conn = http.client.HTTPSConnection("rawg-video-games-database.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "c1f3560e9dmshfdc1351948c8ed1p108ee4jsn0bcb17954627",
    'X-RapidAPI-Host': "rawg-video-games-database.p.rapidapi.com"
}

def request(url):
    conn.request("GET", url, headers=headers)
    res = conn.getresponse().read().decode("utf-8")
    data = json.loads(res)
    return data


def get_games(params):
    return request(f"/games?key={KEY}&{params}")


def get_game(id):
    return request(f"/games/{id}?key={KEY}")


def get_platforms(details):
    platforms = details["platforms"]
    if len(platforms) == 1:
        return platforms[0]["platform"]["name"]

    listed_platforms = []
    for i in range(len(platforms) - 1):
        listed_platforms.append(platforms[i]["platform"]["name"])
    listed_platforms.append(f'and {platforms[len(platforms) - 1]["platform"]["name"]}')

    return ", ".join(listed_platforms)


def print_game_details(details):
    name = details["name"]
    released = details["released"]
    updated = details["updated"]
    rating = details["rating"]
    rating_top = details["rating_top"]
    ratings_count = details["ratings_count"]
    platforms = get_platforms(details)
    website = details["website"]
    description = details["description"][:200] + "..."

    output = f"""{name} is a video game released on {released}, with its last update on {updated}. It has a rating of {rating} out of {rating_top} based on {ratings_count} reviews and is available on platforms such as {platforms}. {f"You can find more information on its official website linked here: {website}. " if website else ""}{description}... blah blah blah, you get the point."""
    print(output)


def print_list_of_games(details):
    print(f'There are {details["count"]} results, but here are the first {len(details["results"])}.')
    for game in details["results"]:
        print(game["name"])


# games_data = get_games("search=\"rocket-league\"")
# print_list_of_games(games_data)
# game_data = get_game(games_data["results"][0]["id"])
# print_game_details(game_data)