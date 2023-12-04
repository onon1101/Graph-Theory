import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy

x = numpy.array([1])
y = numpy.array([1])

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

        fig, ax = plt.subplots(figsize=(12, 12))

        # fig.patch.set_facecolor('#666666')

        # 設定框架
        # fig.patch.set_edgecolor('#fff')
        fig.patch.set_linewidth(0)

        maze = numpy.array(maze)
        maze[maze==0] = 2
        maze[maze==1] = 0
        maze[maze==2] = 1

        # 顯示地圖
        ax.imshow(
            maze,
            # cmap=plt.cm.binary,
            interpolation='nearest',
            vmin=0,
            vmax=4,
            # cmap="#440154"
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
            maze.shape[1] - 1, maze.shape[0] - 2, -0.4, 0,
            fc='blue',
            ec='blue',
            head_width=0.3,
            head_length=0.3
        )

        # line, = ax.plot(x, y, color='red')

        PathNumpy = numpy.array([[1, 1]])

        last_elem = [1,1]

        for elem in path:
            Temp = numpy.linspace(
                last_elem,
                elem,
                8,
            )
            # print(Temp)
            PathNumpy = numpy.append(
                PathNumpy,
                Temp,
                axis=0
            )
            last_elem = elem

        # print(PathNumpy)
        XpathNumpy = PathNumpy.T[0]
        YpathNumpy = PathNumpy.T[1]
        color = XpathNumpy + YpathNumpy
        scat = ax.scatter(XpathNumpy, YpathNumpy, edgecolors='none', alpha=1,
                          # s=2400,
                          marker='s')
        def run(data):
            global y
            global x

            y = numpy.append(y, data[1])
            x = numpy.append(x, data[0])
            scat.set_offsets(numpy.c_[y, x])
            scat.set_color(
                '#59c764'
            )

        # 生成動畫
        animate = animation.FuncAnimation(
            fig,
            run,
            # frames=path,
            frames=PathNumpy,
            interval=30

        )

        ax.set_xticks([])
        ax.set_yticks([])

        # animate.save('dist/test.mp4', fps=30)
        animate.save('dist/test.gif')

        plt.show()
