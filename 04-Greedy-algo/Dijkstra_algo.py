INF= float("infinity")


graph = {
    "U": {"V": 6, "W": 7},
    "V": {"U": 6, "X": 10},
    "W": {"U": 7, "X": 1},
    "X": {"W": 1, "V": 10}
}


print(graph)

unvisited_min_distances= {vertex: INF for vertex in graph}

print(unvisited_min_distances)

visited_vertices ={}



current_vertex='U'

unvisited_min_distances[current_vertex]


while len(unvisited_min_distances) > 0:
    current_vertex, current_distance = sorted(unvisited_min_distances.items(), key=lambda x: x[1])[0]

    for neighbour, neighbour_distance in graph[current_vertex].items():
        print(neighbour,neighbour_distance)
     