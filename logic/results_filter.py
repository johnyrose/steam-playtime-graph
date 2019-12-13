from config import config


def filter_results(stats: dict) -> dict:
    filters = [
        _improve_company_name_texts,
        _remove_stats_with_insufficient_playtime,
        _filter_stats_by_max_studio_amount
    ]
    for filter_function in filters:
        stats = filter_function(stats)
    return stats


def _remove_stats_with_insufficient_playtime(stats):
    if config.MINIMUM_HOURS:
        keys_to_delete = []
        for key in stats.keys():
            if stats[key] <= config.MINIMUM_HOURS:
                keys_to_delete.append(key)
        for key in keys_to_delete:
            del stats[key]
        return stats


def _filter_stats_by_max_studio_amount(stats):
    if config.MAX_STUDIOS_AMOUNT:
        sorted_stats = {k: v for k, v in sorted(stats.items(), key=lambda current_item: current_item[1])}
        ousted_items = list(sorted_stats)[0:len(stats) - config.MAX_STUDIOS_AMOUNT]
        for item in ousted_items:
            del sorted_stats[item]
        return sorted_stats


def _improve_company_name_texts(stats):
    keys_to_change = []
    for item in stats:
        keys_to_change.append(item)
    for key in keys_to_change:
        new_name = _improve_company_name(key)
        stats[new_name] = stats.pop(key)
    return stats


def _improve_company_name(name):
    split_name = name.split(' ')
    if len(split_name) >= 1:
        name = '\n'.join(split_name)
    return name
