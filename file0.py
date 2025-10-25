from heapq import heappush, heappop

def min_spanning_tree(graph):
    visited = set()
    min_tree = []
    start_node = next(iter(graph))
    visited.add(start_node)
    heap = [(cost, start_node, next_node) for next_node, cost in graph[start_node]]
    heapify(heap)

    while heap:
        cost, src, dest = heappop(heap)
        if dest not in visited:
            visited.add(dest)
            min_tree.append((src, dest, cost))
            for next_node, next_cost in graph[dest]:
                if next_node not in visited:
                    heappush(heap, (next_cost, dest, next_node))
    return min_tree

# Example Usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2)],
    'C': [('A', 4), ('B', 2)]
}

minimum_spanning_tree = min_spanning_tree(graph)
print(minimum_spanning_tree)