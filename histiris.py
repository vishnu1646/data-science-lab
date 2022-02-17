import seaborn as sb
import matplotlib.pyplot as plt

i=sb.load_dataset("iris")
sb.histplot(data=i,x="petal_length",bins=5)
plt.show()