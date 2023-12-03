import numpy
import random

class Maze:
    @classmethod
    def __init__(self, dim=0):
        self.dim = dim
        self.maze = None
        pass

    def createMaze(self) -> None:
        # maze = [
        #     [0, 1, 1, 1, 1],
        #     [0, 1, 1, 1, 0],
        #     [0, 1, 0, 1, 0],
        #     [0, 1, 1, 1, 0],
        #     [1, 1, 1, 1, 0],
        # ]
        """
        說明：定義 數字0 通道
        數字1 為牆壁
        :return:
        """

        dim, maze = self.dim, self.maze

        # 畫一個初始化元素都是 1 的矩陣
        maze = numpy.ones((
                dim * 2 + 1,
                dim * 2 + 1
            )
        )

        # 定義開始的點是通道的類型
        x, y = (0, 0)
        maze[2 * x + 1, 2 * y + 1] = 0

        stack = [(x, y)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while len(stack) > 0:

            x, y = stack[-1]
            random.shuffle(directions)

            for dx, dy in directions:

                nx, ny = x + dx, y + dy
                if (
                        nx >= 0 and
                        ny >= 0 and
                        nx < dim and
                        ny < dim and
                        maze[2 * nx + 1, 2 * ny + 1] == 1
                ):
                    maze[2 * nx + 1, 2 * ny + 1] = 0
                    maze[2 * x + 1 + dx, 2 * y + 1 + dy] = 0
                    stack.append((nx, ny))
                    break

            else:
                stack.pop()

        # Create an entrance and an exit
        maze[1, 0] = 0
        maze[-2, -1] = 0

        self.maze = maze

    def GetMaze(self):
        return self.maze
