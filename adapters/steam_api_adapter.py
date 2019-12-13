from steamwebapi.api import ISteamUser, IPlayerService


def get_player_id_from_profile_name(profile_name: str, steam_api_key: str) -> int:
    user_info = ISteamUser(steam_api_key=steam_api_key)
    steamid = user_info.resolve_vanity_url(profile_name)['response']['steamid']
    return steamid

