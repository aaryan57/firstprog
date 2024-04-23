def dls(graph, start, goal, max_depth, depth=0, visited =None, path = None, open_list=None, closed_list=None):
    if visited is None:
        visited=set()
    if path is None:
        path = []
    if open_list  is None:
        open_list = []
    if closed_list is None:
        closed_list = []


    visited.add(start)
    open_list.append(start)
    path =path + [start]

    print("current node",start)
    print("open list",open_list)
    print("closed list",closed_list)


    if start==goal:
        return path

    if depth> max_depth:
        return None

    for neighbour in graph[start]:
        if neighbour not in visited:
            new_path= dls(graph,neighbour,goal, max_depth, depth, visited, path,open_list,closed_list)
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

start_node = input("Enter the start node: ").strip().upper()
goal_node = input("Enter the goal node: ").strip().upper()
max_depth = int(input("Enter the maximum depth: ").strip())

print("DLS Path:")
open_list = []
closed_list = []
if start_node not in graph or goal_node not in graph:
    print("Start node or goal node not found in the graph.")
else:
    path = dls(graph, start_node, goal_node, max_depth, open_list=open_list, closed_list=closed_list)
    if path:
        print("Path from", start_node, "to", goal_node, ":", ' -> '.join(path))
    else:
        print("Path from", start_node, "to", goal_node, "not found.")
        print("Open List after DFS:", open_list)
        print("Closed List after DFS:", closed_list)