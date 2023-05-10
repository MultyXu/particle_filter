import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

np.random.seed(478301)

fig, ax = plt.subplots()

xpoints = np.arange(0, 100)
ypoints = np.random.randint(0, 20, 100)
ax.plot(xpoints, ypoints, "o-")
# np.random.choice(xpoints, 100, [0.01] * 100)
inital_particles = np.arange(0, 100)
ax.plot(inital_particles, [40] * 100, 'o')


# plane, = ax.plot(0,0,"o")
def filter(frame, particles):
    measurement = ypoints[frame]
    weight = [0] * 100
    likely_num = 0
    for p in particles:
        if (ypoints[p] == measurement):
            # this particle looks good
            likely_num += 1
            weight[p] = 1
    dis_num = 1 / likely_num
    # generate probability density
    print(dis_num)
    # for i in range(len(weight)):
    #     if (weight[i] == 1):
    #         weight[i] = dis_num
    # generate new particles
    print(weight)
    particles = np.random.choice(xpoints, 100, weight)
    return particles

particles = filter(0, inital_particles)

def animate(frame):
    # if(frame < 100):
    #   plane.set_data(frame,30)
    #   plane.set_color("r")
    # return plane,
    ax.clear()
    global particles
    ax.plot(particles, [40] * len(particles), "o")
    ax.plot(xpoints, ypoints, color='b', marker='o')
    ax.plot(frame, 30, color="r", marker="o")
    particles = filter(frame, particles)
    while (99 in particles):
      particles = np.delete(particles, np.where(particles == 99))
    for i in range(len(particles)):
        particles[i] += 1


# plane_y = 30
# plane_x = 10 # from 0 to 99
ani = animation.FuncAnimation(
    fig, animate, interval=100, frames=100, repeat=False)

# plt.plot(20, 30, "o:r")
plt.show()
