import matplotlib.pyplot as plt

block_y, block_x = [], []
with open('./block.txt', "r") as f:
    for line in f.readlines():
        block_y.append(int(line.split(",")[0]))
        block_x.append(int(line.split(",")[1]))

plt.figure(dpi=300, figsize=(24, 8))
plt.plot(block_x, block_y, color='red', marker='.', linestyle='')
plt.grid(True)
# plt.show()  # 显示图例
plt.savefig('./block.jpg')
