import seaborn as sb
import matplotlib.pyplot as plt

i=sb.load_dataset("iris")
sb.boxplot(x='petal_length',y='sepal_length',data=i)
plt.show()