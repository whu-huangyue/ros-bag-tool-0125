import numpy as np

a  = np.array([[0, 0, 1, 0.24221], [ -1, 0, 0, 0.16123], [0, -1, 0, -0.16711], [0, 0, 0, 1]])  # 初始化一个非奇异矩阵(数组)
print(np.linalg.inv(a))  # 对应于MATLAB中 inv() 函数

b = np.array([[0, 0, 1, 0.242013], [ -1, 0, 0, -0.16025], [0, -1, 0, -0.16724] ,[0, 0, 0, 1]])

c = np.dot(b, np.linalg.inv(a))

print(c)