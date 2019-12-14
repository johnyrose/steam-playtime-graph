from logic import player_stats_creator, graph_creator, extended_names_unifier, results_filter

if __name__ == '__main__':
    stats = player_stats_creator.create_stats_by_developer()
    stats = extended_names_unifier.unify_extended_names(stats)
    stats = results_filter.filter_results(stats)
    graph_creator.generate_stats_bar_graph(stats)
