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
        disy = y - obstacleY[i]
        dis = np.sqrt(disx**2 + disy**2)
        distance[i] = dis
    return distance


def particle_dis():
    # an array that store the distance to each obstacle
    particle_distances = []
    for particle in particles:
        particle_distances.append(measurement(particle[0], particle[1]))
    return particle_distances


def create_weight(particles, particle_distances, measurement):
    # if the particle distance matches the mesurement (within certian error)
    # it means it is a good guess so increase the weight
    # if the particle is not within map boundry, we set the weight to be 0
    # which means it has no chance to be picked for resampling 
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
        # random sample around the original particle
        new_particle = [particles[index - 1][0] + (np.random.random_sample(
        ) - 0.5)/5, particles[index - 1][1] + (np.random.random_sample() - 0.5)/5]
        new_particles.append(new_particle)
        position += step
    return new_particles


def move_particles(dx, dy, particles):
    for particle in particles:
        particle[0] += dx
        particle[1] += dy
    return particles


def onclick(event):
    global particles, particle_points
    print("key=" + str(event.key))
    x = point.get_xdata()
    y = point.get_ydata()
    # measurement
    distance = measurement(point.get_xdata(), point.get_ydata())
    # the distance of each particle to every obstacle
    particle_distances = particle_dis()
    # create the wegit for each particle according to the measurment
    weight = create_weight(particles, particle_distances, distance)
    # create accumulative weight for uniform sampling
    accu_weight = create_accumulative_weight(weight)
    # generate new particles to replace the old once
    particles = sample_from_accu_weight(accu_weight, particles)

    # print(distance)
    # process key board input to move the robot and particles
    if (event.key == 'left'):
        point.set_data(x - 0.1, y)
        particles = move_particles(-0.1, 0, particles)
    if (event.key == 'right'):
        point.set_data(x + 0.1, y)
        particles = move_particles(0.1, 0, particles)
    if (event.key == 'up'):
        point.set_data(x, y + 0.1)
        particles = move_particles(0, 0.1, particles)
    if (event.key == 'down'):
        point.set_data(x, y - 0.1)
        particles = move_particles(0, -0.1, particles)
    # update the particle position in the plot
    for i in range(len(particle_points)):
        particle_points[i].set_data(particles[i][0], particles[i][1])

    # fig.canvas.draw()
    plt.draw()


point, = ax.plot(5, 5, 'or', zorder=10)
obstacleX = np.random.random((OBSTACLE_NUM,)) * 10
obstacleY = np.random.random((OBSTACLE_NUM,)) * 10
particles = []  # sotre (x,y) pair of the position of the particle
particle_points = []  # an instance of the ploted particle
for i in range(SMAPLE_NUM):
    particle = [np.random.random(1)[0] * 10, np.random.random(1)[0] * 10]
    p_point, = ax.plot(particle[0], particle[1], 'oy', zorder=5)
    particle_points.append(p_point)
    particles.append(particle)

print(particles)
ax.plot(obstacleX, obstacleY, 'ob', zorder=7)
cid = fig.canvas.mpl_connect('key_press_event', onclick)
plt.show()
