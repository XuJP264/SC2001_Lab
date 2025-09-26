import matplotlib
matplotlib.use('Agg')  # 非交互式后端，避免 GUI 崩溃
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.savefig("test_plot.png")
plt.close()
