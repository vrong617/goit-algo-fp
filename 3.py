import heapq


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))

    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0

        priority_queue = [(0, start)]
        heapq.heapify(priority_queue)

        predecessors = {vertex: None for vertex in self.graph}

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances, predecessors

    def print_shortest_path(self, start, end, predecessors):
        path = []
        current_vertex = end
        while current_vertex is not None:
            path.append(current_vertex)
            current_vertex = predecessors[current_vertex]
        path = path[::-1]

        print(f"Найкоротший шлях від {start} до {end}: {' -> '.join(map(str, path))}")


def main():
    graph = Graph()
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 1)
    graph.add_edge(2, 1, 2)
    graph.add_edge(1, 3, 1)
    graph.add_edge(2, 3, 5)
    graph.add_edge(3, 4, 3)

    start_vertex = 0
    distances, predecessors = graph.dijkstra(start_vertex)

    print("Найкоротші відстані від вершини 0:")
    for vertex, distance in distances.items():
        print(f"Вершина {vertex}: {distance}")

    graph.print_shortest_path(start_vertex, 4, predecessors)


if __name__ == "__main__":
    main()
