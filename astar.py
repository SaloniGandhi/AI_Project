import graph_input as Data

def aStarSearch(graph, start, goal):
    frontier = Data.PriorityQueue()
    frontier.put(start)
    came_from = {}
    cost_so_far = {}
    came_from[start.label] = None
    cost_so_far[start.label] = 0
    
    while frontier.len > 0:
        current = frontier.pop()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current.label):
            new_cost = cost_so_far[current.label] + graph.cost(current.label, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + graph.hvaluetable[current.label]
                s = Data.State(current, priority, graph.neighbors(next), next)
                frontier.put(s)
                came_from[next] = current.label
    
    return came_from, cost_so_far, current
    
graph_data = {'nodes':5, 'weight':True, 'adj_l': {'S': [('A', 1), ('B', 4)], 'A': [('B', 2), ('C', 5), ('G', 12)], 'B': [('C', 2)], 'C': [('G', 3)], 'G': []}, 'ss': 'S', 'gs': ['G']}
graph = Data.Graph(graph_data)
graph.hvaluetable = {'S': 7, 'A': 6, 'B': 2, 'C': 1, 'G': 0}

startState = Data.State(None, 7, None, graph.ss)
goalState = Data.State(None, 0, None, graph.gs[0])
cameFrom, costSoFar, result = aStarSearch(graph, startState, goalState)
res = [result]
while result.parent != None:
	result = result.parent
	res.insert(0, result)
	
print(' -> '.join([i.label for i in res]))

