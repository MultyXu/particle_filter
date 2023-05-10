import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


mpl.rcParams['animation.ffmpeg_path'] = "/Users/multyxu/Desktop/Programming/ffmpeg"
# np.random.seed(478301)

# global variables that uses accross the programe
SMAPLE_NUM = 30
STEP_NUM = 30
fig, ax = plt.subplots()
# weight = [10] * 10
particles = np.arange(0, STEP_NUM)


# moutain parameters
xpoints = np.arange(0, STEP_NUM)
ypoints = np.random.randint(0, 20, STEP_NUM)
ax.plot(xpoints, ypoints, "o-")
# np.random.choice(xpoints, 100, [0.01] * 100)
ax.plot(particles, [40] * len(particles), 'o')


def filter(frame, particles):
    measurement = ypoints[frame]
    weight = [0] * STEP_NUM
    for p in particles:
        # update the weight of each particle
        # can add some noise to make the simulation better
        if (0 <= p and p < len(particles)):
            weight[p] = 10
            if (ypoints[p] == measurement):
                # this particle looks good
                weight[p] *= 10
            else:
                weight[p] = np.sqrt(weight[p])
        else:
            # if the particle is out of bound, never choose it
            pass
    print("The weight of particles in time " + str(frame) + ": " + str(weight))

    # find the normalized weight
    total_weight = np.sum(weight)
    normalized_weight = weight / total_weight
    print("Normalized weight: " + str(normalized_weight))

    # construct the accumulative weight
    accu_weight = [0] * (len(particles) + 1)
    for i in range(1, (len(particles) + 1)):
        accu_weight[i] = accu_weight[i - 1] + normalized_weight[i - 1]
    print("Accumulative weight: " + str(accu_weight))

    # resample new particles according to the weight
    # we sample 10 particles this time, first and last is not considered (0 & 1)
    interval = 1 / (SMAPLE_NUM + 2)
    position = interval
    new_particles = [0] * SMAPLE_NUM
    for i in range(SMAPLE_NUM):
        index = next(x for x, val in enumerate(accu_weight) if val >= position)
        new_particles[i] = particles[index - 1]
        position += interval
    print("Old particles: " + str(particles))
    particles = new_particles
    print("New particles: " + str(particles))

    # particles = np.random.choice(xpoints, 10, weight)
    print("\n")
    return particles

def animate(frame):
    # if(frame < 100):
    #   plane.set_data(frame,30)
    #   plane.set_color("r")
    # return plane,
    print("frame: " + str(frame))
    if (frame != 0):
      ax.clear()
      global particles
      ax.plot(particles, [40] * len(particles), "o")
      ax.plot(xpoints, ypoints, color='b', marker='o')
      ax.plot(frame - 1, 30, color="r", marker="o")
      particles = filter(frame - 1, particles)
      while (STEP_NUM - 1 in particles):
          particles = np.delete(particles, np.where(particles == STEP_NUM - 1))
      for i in range(len(particles)):
          particles[i] += 1
      print(particles)


# plane_y = 30
# plane_x = 10 # from 0 to 99
ani = animation.FuncAnimation(
    fig, animate, interval=1000, frames=STEP_NUM + 1, repeat=False)

# FFwriter = animation.PillowWriter(fps=3)
FFwriter = animation.FFMpegWriter(fps=3)
file = "/Users/multyxu/Desktop/Programming/particle_filter/1d_particle_filter.mp4"
ani.save(file, writer = FFwriter)
# plt.plot(20, 30, "o:r")
# plt.show()
