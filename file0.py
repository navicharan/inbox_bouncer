from collections import defaultdict
import heapq

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, node1, node2, weight):
        self.graph[node1].append((node2, weight))
        self.graph[node2].append((node1, weight))

    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        queue = [(0, start)]

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(queue, (new_distance, neighbor))

        return distances

# Example Usage
# graph = Graph()
# graph.add_edge('A', 'B', 1)
# graph.add_edge('B', 'C', 2)
# graph.add_edge('A', 'C', 4)
# distances = graph.dijkstra('A')
# print(distances)