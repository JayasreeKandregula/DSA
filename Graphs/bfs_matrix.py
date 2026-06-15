class BFS:
    def bfsSearch(self, matrix, start):
        size = len(matrix)
        queue = []
        visited = [0]* size
        queue.append(start)
        while len(queue)!=0:
            node_index = queue.pop(0)
            visited[node_index] = 1
            print(node_index)
            for j in range(len(matrix[node_index])):
                if matrix[node_index][j] == 1 and visited[j]==0:
                    queue.append(j)
            






matrix = [[0,1,1,0,0,0], [1,0,0,1,1,1],[1,0,0,0,0,0], [0,1,0,0,0,0],[0,1,0,0,0,0],[0,1,0,0,0,0]]
matrix2 = [[0,1,0,1,0,0],[1,0,0,0,1,0], [0,0,1,0,0,0], [1,0,1,0,0,1],[0,1,0,0,0,0],[0,0,1,0,0,0]]
start =1
BFS().bfsSearch(matrix2, start)

