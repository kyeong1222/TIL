import matplotlib.pyplot as plt
import seaborn as sns

list_x_mean = []
for i in range(50):
    x = np.random.normal(size = 100)
    x_mean = x.mean()
    list_x_mean.append(x_mean)

plt.subplot(121)
sns.distplot(x)
plt.xlim(-5,5)
plt.subplot(122)
sns.distplot(list_x_mean)
plt.xlim(-5,5)
plt.show()
