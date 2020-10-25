class Vertex(object):
    def __init__(self,  index, row, col, value, color=None):
        self.index = int(index)
        self.value = value
        self.color = color
        self.row = int(row)
        self.col = int(col)
        self.PathCost = int(0)
        self.HeuristicCost = int(0)
        self.TotalCost = int(0)
        self.steps = 0

class Graph(object):

    def __init__(self):
        self.graph_dict = {}
        self.vertex_list = []
        self.possible_entries = []

    def generate_from_file(self, file):
        with open(file) as f:
            result = []
            for line in f:
                if(('*' in line) or ('$' in line) or ('.' in line) or ('#' in line)):
                    result.append(list(line.replace(" ", "").rstrip()))
                else:
                    result.append(list(line.split(" ")))
            
            self.rows = int(result[0][0])
            self.cols = int(result[0][1])
            self.steps = int(result[0][2])
            self.vertex_count = 0
            row_count = 0
            for line in result[1:]:
                col_count = 0
                for character in line:
                    vertex = Vertex(self.vertex_count, row_count, col_count, character)

                    if(character == '$'):
                        self.goal = vertex

                    self.add_vertex(vertex)

                    self.vertex_list.append(vertex)

                    if( (vertex.row == 0 or 
                        vertex.col == 0 or 
                        vertex.row == self.rows-1 or 
                        vertex.col == self.cols-1) and 
                        vertex.value not in ['*', '$']):
                        
                        self.possible_entries.append(vertex)

                    self.vertex_count += 1
                    col_count += 1
                    
                row_count += 1
                
            for vertex in self.vertex_list:
                left_border = False
                right_border = False
                if(vertex.index % self.cols == 0):
                    left_border = True
                elif((vertex.index + 1) % self.cols == 0):
                    right_border = True
                    
                if(vertex.row > 0 and vertex.row < self.rows-1):
                    self.add_edge(vertex, self.vertex_list[vertex.index - self.cols])
                    self.add_edge(vertex, self.vertex_list[vertex.index + self.cols])

                elif(vertex.row == 0):
                    self.add_edge(vertex, self.vertex_list[vertex.index + self.cols])
                elif(vertex.row == self.rows-1):
                    self.add_edge(vertex, self.vertex_list[vertex.index - self.cols])

                if(left_border):
                    self.add_edge(vertex, self.vertex_list[vertex.index + 1])
                elif(right_border):
                    self.add_edge(vertex, self.vertex_list[vertex.index - 1]) 
                else:
                    self.add_edge(vertex, self.vertex_list[vertex.index - 1])
                    self.add_edge(vertex, self.vertex_list[vertex.index + 1])

    def vertices(self): 
        for vertex in self.graph_dict.keys():
            print("Key: {}".format(vertex.index), "Row: {}".format(vertex.row), 
                    "Value: {}".format(vertex.value))

    def edges(self):
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
        else:
            self.graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        edges = []
        for vertex in self.vertex_list:
            for neighbour in self.graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex.index, neighbour.index})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res


if __name__ == "__main__":

    graph = Graph()
    graph.generate_from_file("test.txt")

    print("Vertices of graph:")
    graph.vertices()

    print("Edges of graph:")
    print(graph.edges())

