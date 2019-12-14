from requests import get
from config import config
import json


def get_game_info(game_id: int) -> dict:
    response = get(f'{config.STEAMSPY_URL}/api.php?request=appdetails&appid={game_id}')
    response.raise_for_status()
    return json.loads(response.text)
