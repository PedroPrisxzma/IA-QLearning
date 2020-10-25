import sys
import modules

algorithm = sys.argv[1]
entry_file = sys.argv[2]

graph = modules.graph.Graph()
graph.generate_from_file(entry_file)

possible_entry_points = [v for v in graph.possible_entries]

ok = False
result_list = 0
if(algorithm == 'bfs'):
    bfs = modules.bfs.BFS(graph)
    result_list = [bfs.Run(i) for i in possible_entry_points]
    location = 0 # Start node location in the list
    ok = True

elif(algorithm == 'dfs'):
    dfs = modules.dfs.DFS(graph)
    result_list = [dfs.Run(i) for i in possible_entry_points]
    location = 0 # Start node location in the list
    ok = True

elif(algorithm == 'ids'):
    ids = modules.ids.IDS(graph)
    result_list = [ids.Run(i) for i in possible_entry_points]
    location = 0 # Start node location in the list
    ok = True
    
elif(algorithm == 'astar'):
    astart = modules.astar.Astar(graph)
    result_list = [astart.Run(i, graph.goal) for i in possible_entry_points]
    location = -1
    ok = True


if(result_list != 0 and ok):
    final_list = [r for r in result_list if len(r[0]) > 0]
    
    try:
        result = min(final_list, key=lambda x: len(x[0]))
    except:
        print("No result found")

    steps = len(result[0])
    localizations = result[1]
    coordinates = [result[0][location].row, result[0][location].col]
    print(steps, localizations, coordinates)

else:
    print("Algortihm not implemented")
