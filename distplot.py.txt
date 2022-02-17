import seaborn as sb
import matplotlib.pyplot as p

i=sb.load_dataset("iris")
sb.displot(x="petal_length",y="sepal_length",data=i)
p.show()