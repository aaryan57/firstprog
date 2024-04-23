from collections import deque


def bfs(graph, start, goal):
    queue = deque([start])
    visited = {start: None}
    open_list = []
    closed_list = []

    while queue:
        node = queue.popleft()
        open_list.append(node)
        if node == goal:
            return construct_path(visited, start, goal), open_list, closed_list
        closed_list.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited[neighbor] = node
                open_list.append(neighbor)
                queue.append(neighbor)
    return None, open_list, closed_list


def construct_path(visited, start, goal):
    path = []
    while goal is not None:
        path.append(goal)
        goal = visited[goal]
    return list(reversed(path))

    # FOR GRAPH
    # graph = {
    #     'A': ['B', 'C'],
    #     'B': ['D', 'E'],
    #     'C': ['F'],
    #     'D': [],
    #     'E': ['F'],
    #     'F': []
    # }


graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': [''],
    'E': [],
    'F': [],
    'G': [],
    'H': []
}

start_node = input("Enter the start node: ").strip().upper()
goal_node = input("Enter the goal node: ").strip().upper()

print("BFS Path:")
if start_node not in graph or goal_node not in graph:
    print("Start node or goal node not found in the graph.")
else:
    path, open_list, closed_list = bfs(graph, start_node, goal_node)
    if path:
        print("Path from", start_node, "to", goal_node, ":", ' -> '.join(path))
    else:
        print("Path from", start_node, "to", goal_node, "not found.")
    print("Open List:", open_list)
    print("Closed List:", closed_list)