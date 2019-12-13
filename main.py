from logic import player_stats_creator, graph_creator


if __name__ == '__main__':
    stats = player_stats_creator.create_stats_by_developer()
    graph_creator.generate_stats_bar_graph(stats)
