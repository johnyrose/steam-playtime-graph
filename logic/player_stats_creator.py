from config import config
from adapters import steam_api_adapter, steamspy_api_adapter


def _create_stats_by_common_game_info_attribute(games: list, attribute: str) -> dict:
    stats_dict = {}
    for game_stats in games:
        game_info = steamspy_api_adapter.get_game_info(game_stats['appid'])
        if game_info[attribute] not in stats_dict:
            stats_dict[game_info[attribute]] = 0
        stats_dict[game_info[attribute]] += game_stats['playtime_forever']
    return stats_dict


def _get_games_list() -> list:
    profile_id = steam_api_adapter.get_player_id(config.PROFILE_NAME, config.STEAM_API_KEY)
    games = steam_api_adapter.get_owned_games(profile_id, config.STEAM_API_KEY)
    return games


def create_stats_by_developer() -> dict:
    games = _get_games_list()
    devs_dict = _create_stats_by_common_game_info_attribute(games, attribute='developer')
    return devs_dict


def create_stats_by_publisher() -> dict:
    games = _get_games_list()
    punlishers_dict = _create_stats_by_common_game_info_attribute(games, attribute='publisher')
    return punlishers_dict
