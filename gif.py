import os
import random

import imageio
import matplotlib.pyplot as plt


# get some data to plot
x = range(1, 8)
ys = [random.choices(range(100), k=7) for _ in range(10)]

# create each plot and save it as an image
filenames = []
for ind, y in enumerate(ys):
    # plot data as bar charts
    plt.bar(x, y)

    # create file name and append it to a list
    filename = f"{ind}.png"
    filenames.append(filename)

    # repeat frame a few times so that the gif changes more slowly
    for i in range(5):
        filenames.append(filename)

    # save frame
    plt.savefig(filename)
    plt.close()

# use those individual image files to create a gif
with imageio.get_writer("mygif.gif", mode="I") as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

# Remove files leaving only the gif
for filename in set(filenames):
    os.remove(filename)