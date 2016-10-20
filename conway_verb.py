################################################################################
# conway.py
#
# Author: electronut.in
# 
# Description:
#
# A simple Python/matplotlib implementation of Conway's Game of Life.
################################################################################

import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

N = 100
ON = 1
OFF = 0
vals = [ON, OFF]

# populate grid with random on/off - more off than on
grid = np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

def update(data):
  global grid
  newGrid = grid.copy()

  # Berechne Verschiebungen
  grid2 = np.roll(grid, 1, axis=1)
  grid3 = np.roll(grid2, 1, axis=1)

  # Hilfsvariable
  added = grid + grid2 + grid3

  # 1+2+3 + hoch(hoch(1+2+3)) + hoch(1+3)
  total = added + np.roll(added, -2, axis=0) + np.roll(grid + grid3, -1, axis=0) 
  total = np.roll(total, -1, axis=1) # links
  total = np.roll(total, 1, axis=0) # runter

  newGrid[(newGrid ==  ON) & ((total < 2) | (total > 3))] = OFF;
  newGrid[(newGrid == OFF) & (total == 3)] = ON;

  # update data
  mat.set_data(newGrid)
  grid = newGrid
  return [mat]
 

# set up animation
fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, update, interval=50,
                              save_count=50)
plt.show()

