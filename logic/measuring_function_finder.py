from logic import player_stats_creator
from typing import Callable


measuring_stats_dict = {
    "developer": player_stats_creator.create_stats_by_developer,
    "publisher": player_stats_creator.create_stats_by_publisher
}


def get_stats_measuring_function(measure_by: str) -> Callable:
    try:
        return measuring_stats_dict[measure_by]
    except KeyError:
        raise Exception(f'Cannot measure by parameter "{measure_by}", must be one of the '
                        f'following: {list(measuring_stats_dict.keys())}')
