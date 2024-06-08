import heapq


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))


def dijkstra(graph, start_vertex):
    distances = {vertex: float("infinity") for vertex in range(graph.vertices)}
    distances[start_vertex] = 0
    priority_queue = [(0, start_vertex)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph.graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


g = Graph(6)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 1)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 3)
g.add_edge(1, 4, 20)
g.add_edge(2, 3, 8)
g.add_edge(3, 4, 7)
g.add_edge(3, 5, 6)
g.add_edge(4, 5, 1)

distances = dijkstra(g, 0)
print("Найкоротші шляхи від вершини 0 до інших:")
for vertex in range(g.vertices):
    print(f"Вершина {vertex}: {distances[vertex]}")
