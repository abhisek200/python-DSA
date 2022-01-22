class Graph:
    def __init__(self) -> None:
        self.adj_list = {}
    
    def addVertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':' , self.adj_list[vertex])

    def addEdge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def removeEdge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False

my_graph = Graph()
my_graph.addVertex('A')
my_graph.addVertex('B')
my_graph.addVertex('C')

my_graph.addEdge('A','B')
my_graph.addEdge('B','C')
my_graph.addEdge('C','A')

my_graph.print_graph()

print('\n')

my_graph.removeEdge('A','B')

my_graph.print_graph()