class Graph:
    """
    A class to represent a graph using an adjacency matrix.
    
    Attributes:
        vertex_count (int): Number of vertices in the graph.
        adj_matrix (list of list): Adjacency matrix to store edges.
    """
    def __init__(self, vertex_count):
        """
        Initialize the graph with a given number of vertices.
        
        Args:
            vertex_count (int): Number of vertices in the graph.
        """
        self.vertex_count = vertex_count
        self.adj_matrix = [[0] * vertex_count for _ in range(vertex_count)]

    def add_edge(self, start_vertex, end_vertex, weight=1):
        """
        Add an edge between two vertices with an optional weight.
        
        Args:
            start_vertex (int): Starting vertex of the edge.
            end_vertex (int): Ending vertex of the edge.
            weight (int): Weight of the edge (default is 1).
        
        Raises:
            ValueError: If the vertices are invalid.
        """
        if 0 <= start_vertex < self.vertex_count and 0 <= end_vertex < self.vertex_count:
            self.adj_matrix[start_vertex][end_vertex] = weight
            self.adj_matrix[end_vertex][start_vertex] = weight
        else:
            raise ValueError("Invalid Vertex")

    def remove_edge(self, start_vertex, end_vertex):
        """
        Remove an edge between two vertices.
        
        Args:
            start_vertex (int): Starting vertex of the edge.
            end_vertex (int): Ending vertex of the edge.
        
        Raises:
            ValueError: If the vertices are invalid.
        """
        if 0 <= start_vertex < self.vertex_count and 0 <= end_vertex < self.vertex_count:
            self.adj_matrix[start_vertex][end_vertex] = 0
            self.adj_matrix[end_vertex][start_vertex] = 0
        else:
            raise ValueError("Invalid Vertex")

    def has_edge(self, start_vertex, end_vertex):
        """
        Check if there is an edge between two vertices.
        
        Args:
            start_vertex (int): Starting vertex of the edge.
            end_vertex (int): Ending vertex of the edge.
        
        Returns:
            bool: True if there is an edge, False otherwise.
        
        Raises:
            ValueError: If the vertices are invalid.
        """
        if 0 <= start_vertex < self.vertex_count and 0 <= end_vertex < self.vertex_count:
            return self.adj_matrix[start_vertex][end_vertex] != 0
        else:
            raise ValueError("Invalid Vertex")

    def print_adj_matrix(self):
        """
        Print the adjacency matrix of the graph.
        """
        print("Adjacency Matrix:")
        for row_list in self.adj_matrix:
            print(' '.join(map(str, row_list)))

if __name__ == "__main__":
    obj = Graph(5)
    obj.add_edge(0, 1)
    obj.add_edge(1, 2)
    obj.add_edge(1, 3)
    obj.add_edge(2, 3)
    obj.add_edge(2, 4)
    obj.print_adj_matrix()