import matplotlib.pyplot as plt
import numpy as np
import threading
import sys

plt.figure(dpi=300, figsize=(24, 8))
sys.setrecursionlimit(1000000)


class Solution(object):
    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        road = []
        mark = [[0] * n for i in range(m)]
        self.dfs(mark, grid, road, 71, 141)
        return road

    # 深度优先搜索
    def dfs(self, mark, grid, road, x, y):
        m = len(grid)
        n = len(grid[0])
        mark[x][y] = 1

        dx = [1, -1, 0, 0]  # 方向数组
        dy = [0, 0, 1, -1]
        # 遍历上下左右四个方向
        for i in range(4):
            newx = dx[i] + x
            newy = dy[i] + y
            if newx < 0 or newx >= m or newy >= n or newy < 0:
                continue
            if mark[newx][newy] == 0 and grid[newx][newy] == 0:
                road.append([x, y, i])
                self.dfs(mark, grid, road, newx, newy)
                road.append([newx, newy, i])


y, x = [], []
with open('./block.txt', "r") as f:
    for line in f.readlines():
        y.append(int(line.split(",")[0]))
        x.append(int(line.split(",")[1]))


def func():
    s = Solution()
    x_new, y_new = [], []
    for x1, y1 in zip(x, y):
        x_new.append(x1)
        y_new.append(y1)

    flag = np.zeros([500, 200])
    a = x_new
    b = y_new
    flag[a, b] = 1

    road = np.array(s.numIslands(flag))

    with open('./result.txt', 'w') as f:
        f.write(str(1) + '\n')
        for r in road:
            if r[2] == 0:
                f.write(
                    '4:' + str(r[0]) + ',' + str(r[1]) \
                    + ':' + str(r[0] - 1) + ',' + str(r[1]) \
                    + ';' + str(r[0]) + ',' + str(r[1]) \
                    + ';' + str(r[0] + 1) + ',' + str(r[1]) + '\n'
                )

            if r[2] == 1:
                f.write(
                    '3:' + str(r[0]) + ',' + str(r[1]) \
                    + ':' + str(r[0] - 1) + ',' + str(r[1]) \
                    + ';' + str(r[0]) + ',' + str(r[1]) \
                    + ';' + str(r[0] + 1) + ',' + str(r[1]) + '\n'
                )

            if r[2] == 2:
                f.write(
                    '1:' + str(r[0]) + ',' + str(r[1]) \
                    + ':' + str(r[0]) + ',' + str(r[1] - 1) \
                    + ';' + str(r[0]) + ',' + str(r[1]) \
                    + ';' + str(r[0]) + ',' + str(r[1] + 1) + '\n'
                )
            if r[2] == 3:
                f.write(
                    '2:' + str(r[0]) + ',' + str(r[1]) \
                    + ':' + str(r[0]) + ',' + str(r[1] - 1) \
                    + ';' + str(r[0]) + ',' + str(r[1]) \
                    + ';' + str(r[0]) + ',' + str(r[1] + 1) + '\n'
                )

        f.write(str(9) + '\n')

    print('~- ' * 10 + '路径长度:' + str(len(road)) + ' ~-' * 10)

    X = []
    Y = []
    for i in range(len(road)):
        X.append(road[i, 0] + 0.5)
        Y.append(road[i, 1] + 0.5)
    num = len(X)
    ax = plt.subplot(111)
    ax.fill_between(np.array([0, 1]), 0, 1, facecolor='red')
    n_x1 = np.array(a)
    n_x2 = np.array(a) + 1
    n_y1 = np.array(b)
    n_y2 = np.array(b) + 1
    for i in range(len(n_x1)):
        ax.fill_between(np.array([n_x1[i], n_x2[i]]), n_y1[i], n_y2[i], facecolor='green')
    for i in range(num - 1):
        ax.arrow(X[i], Y[i], X[i + 1] - X[i], Y[i + 1] - Y[i], length_includes_head=True, head_width=0.15,
                 head_length=0.15, ec='b')
    ax.xaxis.grid(True, which='major')  # major,color='black'
    ax.yaxis.grid(True, which='major')  # major,color='black'
    plt.show()


if __name__ == '__main__':
    threading.stack_size(200000000)
    thread = threading.Thread(target=func)
    thread.start()
