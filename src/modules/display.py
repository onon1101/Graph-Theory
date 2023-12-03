import matplotlib.pyplot as plt
import matplotlib.animation as animation


class DrawMaze:
    @classmethod
    def __init__(self, maze, path):
        self.maze = maze
        self.path = path

        self.showMaze(self)
        pass

    def showMaze(self):
        maze = self.maze
        path = self.path

        fig, ax = plt.subplots(figsize=(10, 10))

        # 設定框架
        fig.patch.set_edgecolor('white')
        fig.patch.set_linewidth(0)

        # 顯示地圖
        ax.imshow(
            maze,
            cmap=plt.cm.binary,
            interpolation='nearest'
        )

        # 顯示走過的路徑
        # if path is not None:
        #     x_coords = [x[1] for x in path]
        #     y_coords = [y[0] for y in path]
        #     ax.plot(
        #         x_coords,
        #         y_coords,
        #         color='red',
        #         linewidth=2,
        #     )

        x, y = [], []
        line, = ax.plot(x, y, color='red')

        def run(data):
            x.append(data[0])
            y.append(data[1])
            line.set_data(y, x)
            # ax.scatter(x, y)

        animate = animation.FuncAnimation(
            fig,
            run,
            frames=path,
            interval=3
        )

        # 顯示進入與離開的箭頭
        ax.arrow(
            0, 1, .4, 0,
            fc='green',
            ec='green',
            head_width=0.3,
            head_length=0.3,
        )

        ax.arrow(
            maze.shape[1] - 1, maze.shape[0] - 2, 0.4, 0,
            fc='blue',
            ec='blue',
            head_width=0.3,
            head_length=0.3
        )

        ax.set_xticks([])
        ax.set_yticks([])

        # animate.save('dist/test.mp4', fps=30)
        animate.save('dist/test.gif')
        plt.show()
