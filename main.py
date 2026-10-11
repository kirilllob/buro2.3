import os
from dotenv import load_dotenv
import requests


def get_games(api_key):
    url = f"https://api.rawg.io/api/games"
    params = {
        "key" : api_key,
        "genres" : "strategy",
        "page_size" : 10,
        "metacritic" : "65, 100",
        "tags" : "multiplayer"
    }
    response = requests.get(url,params=params)
    response.raise_for_status()
    games = response.json()["results"]
    return games


def get_screens(game_pk, api_key):
    url = f"https://api.rawg.io/api/games/{game_pk}/screenshots"
    params = {
        "key" : api_key
     }
    response = requests.get(url,params=params)
    response.raise_for_status()
    screens = response.json()["results"]
    return screens


def get_stores(game_pk, api_key):
    url = f"https://api.rawg.io/api/games/{game_pk}/stores"
    params = {
        "key" : api_key
     }
    response = requests.get(url,params=params)
    response.raise_for_status()
    stores = response.json()["results"]
    return stores


def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    games = get_games(api_key)
    for game in games:
        game_name = game["name"]
        game_released = game["released"]
        game_slug = game["slug"]
        screens = get_screens(game_slug, api_key)
        stores = get_stores(game_slug, api_key)
        game_url = f"https://api.rawg.io/api/games{game_slug}"
        print(f"""
            Название игры : {game_name}
            Дата выхода : {game_released}
            Ссылка на игру : {game_url}
            Скриншоты игры  : 
        """)
        for screen in screens:
            game_screen = screen["image"]
            print(game_screen)
        print("ссылки на магазины:")
        for store in stores:
            game_stores = store["url"]
            print(game_stores)


if __name__ == "__main__":
    main()