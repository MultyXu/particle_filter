"""
==============
Keypress event
==============

Show how to connect to keypress events.

.. note::
    This example exercises the interactive capabilities of Matplotlib, and this
    will not appear in the static documentation. Please run this code on your
    machine to see the interactivity.

    You can copy and paste individual parts, or download the entire example
    using the link at the bottom of the page.
"""
import sys
import numpy as np
import matplotlib.pyplot as plt


def on_press(event):
    print('press', event.key)
    sys.stdout.flush()
    ax.plot(10, 10, 'd')
    if event.key == 'x':
        visible = xl.get_visible()
        xl.set_visible(not visible)
        xl.figure.canvas.draw()


# Fixing random state for reproducibility
np.random.seed(19680801)

fig, ax = plt.subplots()

fig.canvas.mpl_connect('key_press_event', on_press)

# ax.plot(np.random.rand(12), np.random.rand(12), 'go')
xl = ax.set_xlabel('easy come, easy go')
ax.set_title('Press a key')
plt.show()
