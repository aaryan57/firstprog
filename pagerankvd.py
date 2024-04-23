import numpy as np
damping_factor=0.85
max_iterations=100
tolerance=1e-5
def calculate_pagerank(adjacency_matrix):
num_pages = len(adjacency_matrix)
teleport_prob = (1 - damping_factor) / num_pages
# Initialize PageRank scores with equal probabilities
pagerank = np.full(num_pages, 1.0 / num_pages)
for _ in range(max_iterations):
new_pagerank = np.zeros(num_pages)
for i in range(num_pages):
for j in range(num_pages):
if adjacency_matrix[j][i] == 1:
num_links_on_page_j = sum(adjacency_matrix[j])
new_pagerank[i] += damping_factor * (pagerank[j] /
num_links_on_page_j)
new_pagerank[i] += teleport_prob
# Check for convergence
if np.sum(np.abs(new_pagerank - pagerank)) < tolerance:
return new_pagerank
pagerank = new_pagerank
return pagerank
graph = np.array([
[0, 1, 1, 0],
[1, 0, 0, 1],
[0, 1, 0, 0],
[0, 0, 1, 0]
])
pagerank_scores = calculate_pagerank(graph)
for i, score in enumerate(pagerank_scores):
print(f'Page {i + 1}: {score:.4f}')