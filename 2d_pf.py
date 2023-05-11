import matplotlib.pyplot as plt
import numpy as np

OBSTACLE_NUM = 5

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])


def measurement():
    # return an array that contains the distance from each obstacle
    distance = [0] * OBSTACLE_NUM
    for i in range(OBSTACLE_NUM):
        disx = point.get_xdata() - obstacleX[i]
        disy = point.get_ydata() - obstacleY[i]
        dis = np.sqrt(disx**2 + disy**2)
        distance[i] = dis[0]
    return distance


def onclick(event):
    print("key=" + str(event.key))
    x = point.get_xdata()
    y = point.get_ydata()
    if (event.key == 'left'):
        point.set_data(x - 0.1, y)
    if (event.key == 'right'):
        point.set_data(x + 0.1, y)
    if (event.key == 'up'):
        point.set_data(x, y + 0.1)
    if (event.key == 'down'):
        point.set_data(x, y - 0.1)
    # measurement 
    distance = measurement()
    print(distance)
    # fig.canvas.draw()
    plt.draw()


point, = ax.plot(5, 5, 'or')
obstacleX = np.random.random((OBSTACLE_NUM,)) * 10
obstacleY = np.random.random((OBSTACLE_NUM,)) * 10
ax.plot(obstacleX, obstacleY, 'ob')
cid = fig.canvas.mpl_connect('key_press_event', onclick)
plt.show()
