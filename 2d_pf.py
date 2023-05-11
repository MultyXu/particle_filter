import matplotlib.pyplot as plt
import numpy as np

OBSTACLE_NUM = 5
SMAPLE_NUM = 30

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])


def measurement(x, y):
    # return an array that contains the distance from each obstacle
    distance = [0] * OBSTACLE_NUM
    for i in range(OBSTACLE_NUM):
        disx = x - obstacleX[i]
        disy = x - obstacleY[i]
        dis = np.sqrt(disx**2 + disy**2)
        distance[i] = dis[0]
    return distance


def particle_dis():
    particle_distances = []
    for particle in particles:
        particle_distances.append(measurement(particle[0], particle[1]))
    return particle_distances


def create_weight(particles, particle_distances, measurement):
    # if the particle distance matches the mesurement (within certian error)
    # it means it is a good guess so increase the weight
    weight = [0] * SMAPLE_NUM
    # if a particle's distance to each obstacle has a samller difference compare to the measurement, assign higher weight
    for i in range(len(particles)):
        if (0 <= particles[i][0] and particles[i][0] <= 10 and 0 <= particles[i][1] and particles[i][1] <= 10):
            # particle is valid cordinate in the map
            weight[i] = 10
            particle_dis = particle_distances[i]
            for j in range(len(particle_dis)):
                abs_difference = np.abs(particle_dis[j] - measurement[j])
                # if difference is less than 1, the weight actually increase
                if (abs_difference < 0.1):
                    weight[i] /= 0.1
                else:
                    weight[i] /= abs_difference
    # normalizing the weight
    weight = weight / np.sum(weight)
    return weight


def create_accumulative_weight(weight):
    accu_weight = [0] * (len(weight) + 1)
    for i in range(1, len(accu_weight)):
        accu_weight[i] = accu_weight[i - 1] + weight[i - 1]
    return accu_weight


def sample_from_accu_weight(accu_weight, particles):
    new_particles = []
    step = 1 / (SMAPLE_NUM + 2)
    position = step
    for i in range(SMAPLE_NUM):
        index = next(x for x, val in enumerate(accu_weight) if val >= position)
        new_particle = [particles[index][0] + np.random.random_sample() /
                        5 - 0.1, particles[index][1] + np.random.random_sample()/5 - 0.1]
        new_particles.append(new_particle)
    return new_particles


def onclick(event):
    print("key=" + str(event.key))
    x = point.get_xdata()
    y = point.get_ydata()
    # measurement
    distance = measurement(point.get_xdata(), point.get_ydata())
    particle_distances = particle_dis()
    print(distance)
    if (event.key == 'left'):
        point.set_data(x - 0.1, y)
    if (event.key == 'right'):
        point.set_data(x + 0.1, y)
    if (event.key == 'up'):
        point.set_data(x, y + 0.1)
    if (event.key == 'down'):
        point.set_data(x, y - 0.1)

    # fig.canvas.draw()
    plt.draw()


point, = ax.plot(5, 5, 'or')
obstacleX = np.random.random((OBSTACLE_NUM,)) * 10
obstacleY = np.random.random((OBSTACLE_NUM,)) * 10
particles = []
particle_points = []
for i in range(SMAPLE_NUM):
    particle = [np.random.random(1)[0] * 10, np.random.random(1)[0] * 10]
    particle_points.append(ax.plot(particle[0], particle[1], 'oy'))
    particles.append(particle)

print(particles)
ax.plot(obstacleX, obstacleY, 'ob')
cid = fig.canvas.mpl_connect('key_press_event', onclick)
plt.show()
