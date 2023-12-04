import numpy as np
from queue import Queue

class Algorithm:
    def __init__(self, maze):
        self.maze = maze
        self.result = None
        self.test = 1
        pass
    def BFS(self):
        maze = self.maze

        # BFS algorithm to find the shortest path
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        start = (1, 1)
        end = (maze.shape[0] - 2, maze.shape[1] - 2)
        visited = np.zeros_like(maze, dtype=bool)
        visited[start] = True
        queue = Queue()
        queue.put((start, []))
        while not queue.empty():
            (node, path) = queue.get()
            for dx, dy in directions:
                next_node = (node[0] + dx, node[1] + dy)
                if (next_node == end):
                    # self.result = [(1 ,0),(1, 1)] + path + [next_node] + [(maze.shape[0] - 2, maze.shape[1] - 1)]
                    self.result = path + [next_node] + [(maze.shape[0] - 2, maze.shape[1] - 1)]
                    return
                if (next_node[0] >= 0 and next_node[1] >= 0 and
                        next_node[0] < maze.shape[0] and next_node[1] < maze.shape[1] and
                        maze[next_node] == 0 and not visited[next_node]):
                    visited[next_node] = True
                    queue.put((next_node, path + [next_node]))

    def GetResult(self):
        return self.result
        pass