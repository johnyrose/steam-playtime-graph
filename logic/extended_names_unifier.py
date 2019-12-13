def unify_extended_names(stats):
    checked_keys = []
    for key in stats:
        if key not in checked_keys:
            extended_keys = _find_all_extended_keys(stats, key)
            for extended_key in extended_keys:
                stats[key] += stats[extended_key]
            checked_keys += extended_keys
    for key in checked_keys:
        del stats[key]
    return stats


def _find_all_extended_keys(stats, origin_key):
    extended_keys = []
    for key in stats:
        if origin_key in key and key != origin_key:
            extended_keys.append(key)
    return extended_keys
