from config import config
from adapters import steam_api_adapter, steamspy_api_adapter


def create_stats_by_developer() -> dict:
    profile_id = steam_api_adapter.get_player_id(config.PROFILE_NAME, config.STEAM_API_KEY)
    games = steam_api_adapter.get_owned_games(profile_id, config.STEAM_API_KEY)
    devs_dict = {}
    for game_stats in games:
        game_info = steamspy_api_adapter.get_game_info(game_stats['appid'])
        if game_info['developer'] not in devs_dict:
            devs_dict[game_info['developer']] = 0
        devs_dict[game_info['developer']] += game_stats['playtime_forever']
    return devs_dict
