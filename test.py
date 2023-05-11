import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])

def onclick(event):
    print("key=" + str(event.key))
    x = point.get_xdata()
    y = point.get_ydata()
    if(event.key == 'left'): 
      point.set_data(x - 0.1, y)
    if(event.key == 'right'): 
      point.set_data(x + 0.1, y)
    if(event.key == 'up'): 
      point.set_data(x, y + 0.1)
    if(event.key == 'down'): 
      point.set_data(x, y - 0.1)
    # fig.canvas.draw()
    plt.draw()


point, = ax.plot(5, 5, 'or')
cid = fig.canvas.mpl_connect('key_press_event', onclick)
plt.show()
