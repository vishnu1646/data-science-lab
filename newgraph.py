import matplotlib.pyplot as plt
x=[1,2,3]
y=[5,7,4]
plt.plot(x,y,label="first line")
x2=[1,2,3]
y2=[10,11,14]
plt.plot(x2,y2,label="second line")
plt.xlabel("plot no")
plt.ylabel("important variables")
plt.title("new graph")
plt.legend()
plt.show()