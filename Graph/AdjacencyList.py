class Graph:
    def __init__(self, vertex_count):
        """
        Initialize the graph with a given number of vertices.
        
        :param vertex_count: Number of vertices in the graph.
        """
        self.vertex_count = vertex_count
        # Create an adjacency list where each vertex has an empty list of neighbors
        self.adj_list = {vertex: [] for vertex in range(vertex_count)}

    def add_edge(self, start_vertex, end_vertex, weight=1):
        """
        Add an edge between two vertices with an optional weight.
        
        :param start_vertex: The starting vertex of the edge.
        :param end_vertex: The ending vertex of the edge.
        :param weight: The weight of the edge (default is 1).
        :raises ValueError: If the vertex indices are out of range.
        """
        if 0 <= start_vertex < self.vertex_count and 0 <= end_vertex < self.vertex_count:
            # Add the edge to both vertices since it's an undirected graph
            self.adj_list[start_vertex].append((end_vertex, weight))
            self.adj_list[end_vertex].append((start_vertex, weight))
        else:
            raise ValueError("Invalid Vertex: Vertex index out of range.")

    def remove_edge(self, start_vertex, end_vertex, weight=None):
        """
        Remove an edge between two vertices. If weight is specified, only remove the edge with that weight.
        
        :param start_vertex: The starting vertex of the edge.
        :param end_vertex: The ending vertex of the edge.
        :param weight: The weight of the edge to remove (optional).
        :raises ValueError: If the vertex indices are out of range.
        """
        if 0 <= start_vertex < self.vertex_count and 0 <= end_vertex < self.vertex_count:
            if weight is None:
                # Remove all edges between start_vertex and end_vertex
                self.adj_list[start_vertex] = [(vertex, w) for (vertex, w) in self.adj_list[start_vertex] if vertex != end_vertex]
                self.adj_list[end_vertex] = [(vertex, w) for (vertex, w) in self.adj_list[end_vertex] if vertex != start_vertex]
            else:
                # Remove only the edge with the specified weight
                self.adj_list[start_vertex] = [(vertex, w) for (vertex, w) in self.adj_list[start_vertex] if not (vertex == end_vertex and w == weight)]
                self.adj_list[end_vertex] = [(vertex, w) for (vertex, w) in self.adj_list[end_vertex] if not (vertex == start_vertex and w == weight)]
        else:
            raise ValueError("Invalid Vertex: Vertex index out of range.")

    def has_edge(self, start_vertex, end_vertex, weight=None):
        """
        Check if there is an edge between two vertices. If weight is specified, check for that specific weight.
        
        :param start_vertex: The starting vertex of the edge.
        :param end_vertex: The ending vertex of the edge.
        :param weight: The weight of the edge to check for (optional).
        :return: True if the edge exists, False otherwise.
        :raises ValueError: If the vertex indices are out of range.
        """
        if 0 <= start_vertex < self.vertex_count and 0 <= end_vertex < self.vertex_count:
            if weight is None:
                # Check if there is any edge between start_vertex and end_vertex
                return any(vertex == end_vertex for (vertex, w) in self.adj_list[start_vertex])
            else:
                # Check if there is an edge with the specified weight
                return any(vertex == end_vertex and w == weight for (vertex, w) in self.adj_list[start_vertex])
        else:
            raise ValueError("Invalid Vertex: Vertex index out of range.")

    def print_adj_list(self):
        """
        Print the adjacency list of the graph.
        """
        print("Adjacency List:")
        for vertex, value in self.adj_list.items():
            print(f"V{vertex}: {value}")


# Example usage of the Graph class
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(3, 4)

# Print the adjacency list
g.print_adj_list()

# Check if an edge exists between vertex 1 and 2
print(g.has_edge(1, 2))  # Output: True

# Remove the edge between vertex 1 and 2
g.remove_edge(1, 2)

# Print the adjacency list after removal
g.print_adj_list()

# Check again if an edge exists between vertex 1 and 2
print(g.has_edge(1, 2))  # Output: False