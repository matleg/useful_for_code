""" matplotlib logo - from matplotlib!"""
# !/usr/bin/env python
# Import various necessary Python and matplotlib packages
import numpy as np
import matplotlib.cm as cm
from matplotlib.pyplot import figure, show, rc
from matplotlib.patches import Ellipse

# Create a square figure on which to place the plot
fig = figure(figsize=(8, 8))
# Create square axes to hold the circular polar plot
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
# Generate 20 colored, angular wedges for the polar plot
N = 20
theta = np.arange(0.0, 2 * np.pi, 2 * np.pi / N)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)
bars = ax.bar(theta, radii, width=width, bottom=0.0)
for r, bar in zip(radii, bars):
    bar.set_facecolor(cm.jet(r / 10.))
    bar.set_alpha(0.5)
# Using dictionaries, create a color scheme for the text boxes
bbox_args = dict(boxstyle="round, pad=0.9", fc="green", alpha=0.5)
bbox_white = dict(boxstyle="round, pad=0.9", fc="1", alpha=0.9)
patch_white = dict(boxstyle="round, pad=1", fc="1", ec="1")
# Create various boxes with text annotations in them at specific
# x and y coordinates
ax.annotate(" ",
            xy=(.5, .93),

            xycoords='figure fraction',
            ha="center", va="center",
            bbox=patch_white)
ax.annotate('Matplotlib and the Python Ecosystem for Scientific Computing',
            xy=(.5, .95),
            xycoords='figure fraction',
            xytext=(0, 0), textcoords='offset points',
            size=15,
            ha="center", va="center",
            bbox=bbox_args)
ax.annotate('Author and Lead Developer \n of Matplotlib ',
            xy=(.5, .82),
            xycoords='figure fraction',
            xytext=(0, 0), textcoords='offset points',
            ha="center", va="center",
            bbox=bbox_args)
ax.annotate('John D. Hunter',
            xy=(.5, .89),
            xycoords='figure fraction',
            xytext=(0, 0), textcoords='offset points',
            size=15,
            ha="center", va="center",
            bbox=bbox_white)
ax.annotate('Friday November 5th \n 2:00 pm \n1106ME ',
            xy=(.5, .25),
            xycoords='figure fraction',
            xytext=(0, 0), textcoords='offset points',
            size=15,
            ha="center", va="center",
            bbox=bbox_args)
ax.annotate('Sponsored by: \n The Hacker Within, \n'
            'The University Lectures Committee, \n The Department of '
            'Medical Physics\n and \n The American Nuclear Society',
            xy=(.78, .1),
            xycoords='figure fraction',
            xytext=(0, 0), textcoords='offset points',
            size=9,
            ha="center", va="center",
            bbox=bbox_args)

import matplotlib.pyplot as plt

plt.show()
