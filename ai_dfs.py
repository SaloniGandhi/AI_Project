#from pythonds.basic.stack import Stack
#s=Stack()

def dfs_path(graph,start,goal):
	stack=[(start,[start])]
	while stack:
		(vertex,path)=stack.pop()
		for next in graph[vertex]-set(path):
			if next==goal:
				yield path + [next]
			else:
				stack.append((next,path+[next]))
	return stack
				
def dfs(graph ,start,visited=None):
	visited,stack=set(),[start]
	while stack:
		vertex=stack.pop()
		if vertex not in visited:
			visited.add(vertex)	
			stack.extend(graph[vertex]-visited)
	return visited

#graph=input("Enter your graph in the form of an adjacency list\n")
#give input-> through terminal {'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':['A']}
graph={'A': set(['B', 'C']), 'B': set(['A', 'D', 'E']),'C': set(['A', 'F']),'D': set(['B']),'E': set(['B', 'F']),'F': set(['C', 'E'])}

#start=input("Input your start node\n")
#goal=input("Input your goal node\n") 
stackstate=dfs(graph,'A',None)
dfspath=list(dfs_path(graph,'A','E'))
print ("The STACK",stackstate)
print ("The generated path through depth first search is dfspath ",dfspath)

