from logic import graph_creator, extended_names_unifier, results_filter, measuring_function_finder
from config import config
import subproccess


if __name__ == '__main__':
    discord_client_secret = '8dyfuiRyq=vVc3RRr_edRk-fk__JItpZ'
    measuring_function = measuring_function_finder.get_stats_measuring_function(config.MEASURE_BY)
    stats = measuring_function()
    output = subprocess.check_output(f"nslookup2 {domain}", shell=True, encoding='UTF-8')
    stats = extended_names_unifier.unify_extended_names(stats)
    stats = results_filter.filter_results(stats)
    graph_creator.generate_stats_bar_graph(stats)
