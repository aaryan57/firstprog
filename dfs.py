def dfs(graph, start, goal, visited=None, path=None, open_list=None, closed_list=None):
    if visited is None:
        visited=set()
    if path is None:
        path=[]
    if open_list  is None:
        open_list=[]
    if closed_list is None:
        closed_list=[]

    visited.add(start)
    open_list.append(start)
    path=path+[start]

    print("current node",start)
    print("open list",open_list)
    print("closed list",closed_list)

    if start==goal:
        return path

    for neighbour in graph[start]:
        if neighbour not in visited:
            new_path=dfs(graph,neighbour,goal,visited,open_list,closed_list)
            if new_path:
                return new_path

    open_list.remove(start)
    closed_list.append(start)

    return None

graph = {
    'A': ['B', 'C','D'],
    'B': ['E', 'F'],
    'C': ['G','H'],
    'D':[],
    'E':[],
    'F':[],
    'G':[],
    'H':[]
}

start_node=int(input("enter start node"))
goal_node=int(input("enter goal"))
print("dfs")
open_list = []
closed_list = []
path = dfs(graph, start_node, goal_node, open_list=open_list, closed_list=closed_list)
if path:
    print("Path from", start_node, "to", goal_node, ":", ' -> '.join(path))
else:
    print("Path from", start_node, "to", goal_node, "not found.")
    print("Open List after DFS:", open_list)
    print("Closed List after DFS:", closed_list)