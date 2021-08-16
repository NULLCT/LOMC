import sys
import copy
import math
import itertools
import collections
import heapq
import decimal

sys.setrecursionlimit(10**9)


def main():
    n, q = map(int, input().split())
    li = list(list() for i in range(n))
    for i in range(n - 1):
        a, b = map(int, input().split())
        li[a - 1].append(b - 1)
        li[a - 1].append(1)
        li[b - 1].append(a - 1)
        li[b - 1].append(1)

    resli = dijkstra(li)

    for i in range(q):
        c, d = map(int, input().split())
        if abs(resli[c - 1] - resli[d - 1]) % 2 == 0:
            print("Town")
        else:
            print("Road")


def dijkstra(adjacencyList):
    placeFlag = list(False for _ in range(len(adjacencyList)))
    placeArray = list(float("inf") for _ in range(len(adjacencyList)))
    roadHeap = list()

    nowPlace = 0
    nowDistance = 0
    placeArray[0] = 0

    while False in placeFlag:
        placeFlag[nowPlace] = True

        for i in range(0, len(adjacencyList[nowPlace]), 2):
            currentDistance = placeArray[nowPlace]
            destination = adjacencyList[nowPlace][i]
            distance = adjacencyList[nowPlace][i + 1]
            placeArray[destination] = min(placeArray[destination],
                                          placeArray[nowPlace] + distance)

            if placeFlag[destination] is False:
                heapq.heappush(roadHeap,
                               Road(currentDistance, destination, distance))

        while roadHeap:
            candidateRoad = heapq.heappop(roadHeap)
            if placeFlag[candidateRoad.destination] is False:
                nowPlace = candidateRoad.destination
                break

    return placeArray


class Road:
    currentDistance = int()
    destination = int()
    distance = int()

    def __init__(self, currentDistance, destination, distance):
        self.currentDistance = currentDistance
        self.destination = destination
        self.distance = distance

    def __lt__(self, other):
        return self.currentDistance + self.distance < other.currentDistance + other.distance


main()
