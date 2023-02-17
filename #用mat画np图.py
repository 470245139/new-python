#用mat画np图
import numpy as np
import matplotlib.pyplot as plt

#  以200ms为间隔均匀采样时间
t = np.arange(0., 5., 0.2)

# 红色破折号、蓝色方块和绿色三角形
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
