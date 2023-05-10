import numpy as np

value = np.arange(0,10)
weight = [0] * 10
weight[5] = 1
print(np.random.choice(value, 10, weight))