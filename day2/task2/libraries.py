import matplotlib.pyplot as plt
import numpy as np


variables = ['A', 'B', 'C', 'D', 'E']
values = np.random.randint(1, 10, size=5)

plt.bar(variables, values, color='b')

plt.title('Bar Plot of different variables')
plt.xlabel('Variables')
plt.ylabel('Value')

plt.show()
