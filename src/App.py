import numpy
import random

from src.modules.maze import Maze
from src.modules.algorithm import Algorithm
from src.modules.display import DrawMaze


def main():
    # the Maze size
    dim = 5

    # create maze
    maze = Maze(dim)
    maze.createMaze()

    # use algorithm
    path = Algorithm(
        maze.GetMaze()
    )
    path.BFS()

    # print(path.GetResult())
    # display process
    DrawMaze(
        maze.GetMaze(),
        path.GetResult(),
    )


if __name__ == "__main__":
    main()
