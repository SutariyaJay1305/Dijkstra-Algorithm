# Dijkstra's Shortest Path Algorithm

This program demonstrates Dijkstra's algorithm to find the shortest path in a graph.

## Instructions

To run the program, follow these steps:

1. Make sure you have Python installed on your system.
2. Download or clone this repository.
3. Navigate to the directory where you downloaded the files.
4. Run the program using the following command:
    ```
    python dijkstra.py
    ```

## Documentation

This program implements Dijkstra's algorithm to find the shortest path in a weighted graph. It takes an adjacency matrix as input and calculates the shortest distances from a given source vertex to all other vertices.

### Insights

- Dijkstra's algorithm is a greedy algorithm that finds the shortest path from a single source vertex to all other vertices in a weighted graph.
- The algorithm works by maintaining a set of vertices whose shortest distance from the source is already known.
- It iteratively selects the vertex with the minimum distance from the source among the vertices not yet processed, updates the distances of its adjacent vertices, and adds it to the set of processed vertices.
- The process continues until all vertices are processed.

### Implemented Features

- Graph class with methods for initializing the graph, computing shortest paths, and displaying results.
- The program takes an adjacency matrix as input.
- It prints the shortest distances from a given source vertex to all other vertices.

### Results

The program output displays the shortest distances from the source vertex:
Vertex   Distance from Source
0                0
1                4
2                12
3                19
4                21
5                11
6                9
7                8
8                14
