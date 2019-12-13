from config import config


def filter_results(stats: dict) -> dict:
    if config.MINIMUM_HOURS:
        stats = _remove_stats_with_insufficient_playtime(stats)
    if config.MAX_STUDIOS_AMOUNT:
        stats = _filter_stats_by_max_studio_amount(stats)
    return stats


def _remove_stats_with_insufficient_playtime(stats):
    keys_to_delete = []
    for key in stats.keys():
        if stats[key] <= config.MINIMUM_HOURS:
            keys_to_delete.append(key)
    for key in keys_to_delete:
        del stats[key]
    return stats


def _filter_stats_by_max_studio_amount(stats):
    sorted_stats = {k: v for k, v in sorted(stats.items(), key=lambda current_item: current_item[1])}
    ousted_items = list(sorted_stats)[0:len(stats) - config.MAX_STUDIOS_AMOUNT]
    for item in ousted_items:
        del sorted_stats[item]
    return sorted_stats
