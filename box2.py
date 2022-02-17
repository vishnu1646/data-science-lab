import matplotlib.pyplot as plt

value1=[72,76,24,40,57]
value2=[62,5,91,25,36]
value3=[23,99,12,78,73]
value4=[99,73,70,16,81]

box_plot_data=[value1,value2,value3,value4]
box=plt.boxplot(box_plot_data,vert=1,patch_artist=True,labels=['course1','course2','course3','course4'],)
colors=['cyan','lightblue', 'lightgreen', 'tan']
for patch,color in zip(box['boxes'],colors):
    patch.set_facecolor(color)
    plt.show()