# DFS traversal is like preoder traversal -  where you have visited array with size as no.of nodes in
# graph. And print the node first and mark it as visited and run loop thorugh neighbouring nodes and
# run dfssearch to the neighbouring nodes who are not visited.

class DFS:
    def __init__(self, matrix):
        self.size = len(matrix)
        self.visited = [0]*self.size
    def dfsSearch(self, matrix, start):
        self.visited[start] = 1
        print(start+1)
        for i in range(len(matrix)):
            if matrix[start][i] == 1 and self.visited[i] == 0:
                self.dfsSearch(matrix,i)

matrix = [[0,1,1,0,0,0,0],[1,0,0,1,0,0,0], [1,0,0,0,0,0,0], [0,1,0,0,1,0,0], [0,0,0,1,0,1,1], [0,0,0,0,1,0,0],[0,0,0,0,1,0,0]]
obj = DFS(matrix)
obj.dfsSearch(matrix, 3)


#Graph having 2 components
matrix2 = [[0,1,1,0,0,0,0,0,0],[1,0,0,1,0,0,0,0,0], [1,0,0,0,0,0,0,0,0], [0,1,0,0,1,0,0,0,0], [0,0,0,1,0,1,1,0,0], [0,0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0,0], [0,0,0,0,0,0,0,0,1], [0,0,0,0,0,0,0,1,0]]
obj = DFS(matrix2)
for i in range(len(obj.visited)):
    if obj.visited[i] !=1:
        obj.dfsSearch(matrix2, i)





