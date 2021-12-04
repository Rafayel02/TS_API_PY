from copy import deepcopy

import numpy as np
from django import http
import time
from findpath_lite import gridConvert
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement

grid = gridConvert()


def main():
    print("Esh")


def tester(request):
    a = time.time()

    grid.cleanup()
    print(grid.width)
    scale = 0.08
    startx = int(request.GET.get('sX'))
    starty = int(request.GET.get('sY'))
    sTerm = request.GET.get('sTerm')
    sFloor = request.GET.get('sFloor')
    eObj = request.GET.get('eObj')

    endx = 2964
    endy = 1003
    print(startx)

    start = grid.node(int(startx * scale), int(starty * scale))
    end = grid.node(int(endx * scale), int(endy * scale))

    finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
    path, runs = finder.find_path(start, end, grid)
    print('route time', time.time() - a)
    path = [(int(t[0] * (1 / scale)), int(t[1] * (1 / scale))) for t in path]
    path = np.array(path)
    print(path)
    print(time.time() - a)

    response = http.HttpResponse(np.array(path))

    response.status_code = 200

    return response
