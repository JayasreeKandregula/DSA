#BFS is level order traversal - where we have visited array with size of no.of nodes in graph and we start
# with any node as starting point we print the node, and run loop to its corresponding row and add
# all the neighbours its connected to and visited of that neighbour should be zero.

class BFS:
    def __init__(self, matrix):
        self.size = len(matrix)
        self.visited = [0]*self.size
    def bfsSearch(self, matrix, start):
        size = len(matrix)
        queue = []
        queue.append(start)
        while len(queue)!=0:
            node_index = queue.pop(0)
            self.visited[node_index] = 1
            print(node_index)
            for j in range(len(matrix[node_index])):
                if matrix[node_index][j] == 1 and self.visited[j]==0:
                    queue.append(j)
            






matrix = [[0,1,1,0,0,0], [1,0,0,1,1,1],[1,0,0,0,0,0], [0,1,0,0,0,0],[0,1,0,0,0,0],[0,1,0,0,0,0]]
matrix2 = [[0,1,0,1,0,0],[1,0,0,0,1,0], [0,0,1,0,0,0], [1,0,1,0,0,1],[0,1,0,0,0,0],[0,0,1,0,0,0]]
start =1
BFS(matrix2).bfsSearch(matrix2, start)

#for graphs having multiple components
print("mutliple components graph/n")
matrix2 = [[0,1,1,0,0,0,0,0,0],[1,0,0,1,0,0,0,0,0], [1,0,0,0,0,0,0,0,0], [0,1,0,0,1,0,0,0,0], [0,0,0,1,0,1,1,0,0], [0,0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0,0], [0,0,0,0,0,0,0,0,1], [0,0,0,0,0,0,0,1,0]]
obj = BFS(matrix2)
for i in range(len(obj.visited)):
    if obj.visited[i] !=1:
        obj.bfsSearch(matrix2, i)

