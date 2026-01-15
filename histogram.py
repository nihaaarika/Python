import matplotlib.pyplot as plt
import numpy as np

# Unimodal distribution
np.random.seed(0)
data_unimodal = np.random.normal(loc=0, scale=1, size=1000)
plt.figure(figsize=(10, 4))
plt.hist(data_unimodal, bins=30, edgecolor='black')
plt.title('Unimodal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()


# Bimodal distribution
np.random.seed(1)
data_bimodal1 = np.random.normal(loc=-2, scale=1, size=500)
data_bimodal2 = np.random.normal(loc=2, scale=1, size=500)
data_bimodal = np.concatenate((data_bimodal1, data_bimodal2))
plt.figure(figsize=(10, 4))
plt.hist(data_bimodal, bins=30, edgecolor='black')
plt.title('Bimodal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()


# Multimodal distribution (3 modes)
np.random.seed(2)
data_multimodal1 = np.random.normal(loc=-3, scale=0.8, size=300)
data_multimodal2 = np.random.normal(loc=0, scale=1.2, size=400)
data_multimodal3 = np.random.normal(loc=3, scale=0.9, size=300)
data_multimodal = np.concatenate((data_multimodal1, data_multimodal2, data_multimodal3))
plt.figure(figsize=(10, 4))
plt.hist(data_multimodal, bins=30, edgecolor='black')
plt.title('Multimodal Distribution (3 modes)')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
