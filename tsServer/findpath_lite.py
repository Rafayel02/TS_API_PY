import cv2 as cv
import numpy as np
import time
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import sys

b = time.time()

np.set_printoptions(threshold=sys.maxsize)
filename = r"C:\Users\User\Downloads/0.08b_1.png"
scale = 0.08
startx = 1637
starty = 782
endx = 2964
endy = 1003

im = cv.imread(filename, cv.IMREAD_GRAYSCALE)

grid = Grid(matrix=im)



print('full time', time.time() - b)


def gridConvert():
    print("Ezoo")
    grid = Grid(matrix=im)
    return grid
