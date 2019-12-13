from matplotlib import pyplot as plt
import numpy


def generate_stats_bar_graph(player_stats: dict):
    keys = player_stats.keys()
    hours = player_stats.values()
    keys_nums = numpy.arange(len(keys))
    plt.xticks(keys_nums, keys)
    plt.title("Hours by Developer")
    plt.ylabel("Hours")
    plt.xlabel("Developer")
    plt.bar(keys_nums, hours)
    plt.show()
