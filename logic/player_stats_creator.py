from config import config
from adapters import steam_api_adapter, steamspy_api_adapter
from logic.get_game_info_thread import GameInfoFinder


def _get_games_info(games: list) -> dict:
    threads = []
    for game in games:
        threads.append(GameInfoFinder(game['appid']))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    games_info = {}
    for thread in threads:
        games_info[thread.game_info['appid']] = thread.game_info
    return games_info


def _create_stats_by_common_game_info_attribute(games: list, attribute: str) -> dict:
    games_info = _get_games_info(games)
    stats_dict = {}
    for game_stats in games:
        game_info = games_info['appid']
        if game_stats['playtime_forever'] != 0:
            if game_info[attribute] not in stats_dict:
                stats_dict[game_info[attribute]] = 0
            stats_dict[game_info[attribute]] += game_stats['playtime_forever'] / 60
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
    publishers_dict = _create_stats_by_common_game_info_attribute(games, attribute='publisher')
    return publishers_dict
