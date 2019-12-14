from threading import Thread
from adapters import steamspy_api_adapter


class GameInfoFinder(Thread):
    def __init__(self, app_id: int):
        Thread.__init__(self)
        self.app_id = app_id
        self.game_info = None

    def run(self):
        self.game_info = steamspy_api_adapter.get_game_info(self.app_id)
