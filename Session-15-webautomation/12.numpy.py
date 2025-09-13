import numpy as np

prices = np.array([29,99,24,91,19,32,54,67,89])

print("Max Price: ",np.max(prices))
print("Min Price: ",np.min(prices))
print("Average Price: ",np.mean(prices))
print("Price>30 ",prices[prices>30])