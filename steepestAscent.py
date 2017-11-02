import graph_input as Data

graph_data = {'nodes':5, 'weight':False, 'adj_l': {'A': ['B', 'C'], 'B': ['E'], 'C': ['D'], 'D': ['E'], 'E': []}, 'ss': 'A', 'gs': ['E']}
graph = Data.Graph(graph_data)
graph.hvalue_table = {'A': 1, 'B': 2, 'C': 4, 'D': 5, 'E': 10}

def hill(start, maxim, path):
    maxh = maxim
    max_node = ''
    while(start not in graph.gs):
        path.append(start)
        children = graph.neighbors(start)
        for i in children:
            if graph.hvalue_table[i] > maxh:
                maxh = graph.hvalue_table[i]
                max_node = i
            if(max_node in graph.gs):
                path.append(max_node)
                return
            if len(graph.neighbors(i)) == 0:
                print("Found local maxima at: ")
                print(max_node)
                print("Local maxima: ")
                print(maxh)
                #print(start)
                return
        start = max_node
start = graph.ss
visited = []
visited.append(start)
path = []
#path.append(start)
maxim = graph.hvalue_table[start]
hill(start,maxim, path)
print("Path: ")
print(' -> '.join([i for i in path]))
