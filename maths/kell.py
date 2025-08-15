import matplotlib.pyplot as mat
import numpy as np

x = np.array(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
y = np.array([41, 37, 29, 39, 24])

mat.bar(x, y)
mat.title("Energy Consumption Weekly")
mat.xlabel("Day")
mat.ylabel("Usage (kWh)")

mat.show()