import sys
import modules

algorithm = sys.argv[1]
entry_file = sys.argv[2]

graph = modules.graph.Graph()
graph.generate_from_file(entry_file)

possible_entry_points = [v for v in graph.possible_entries] #Not needed for TP2 possibly, must check

ok = False



if(ok):
    PrintResult()
else:
    print("Algortihm not implemented")


def PrintResult():
    return("Not Yet Implemented")