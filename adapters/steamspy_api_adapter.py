from requests import get


def get_game_info(game_id: int) -> dict:
    response = get(f'http://steamspy.com/api.php?request=appdetails&appid={game_id}')
    return response.text
