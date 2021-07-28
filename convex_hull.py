"""
Finding Convex Hull

Gift wrapping or Jarvis's algorithm

Reference: https://www.geeksforgeeks.org/convex-hull-set-1-jarviss-algorithm-or-wrapping/
"""

from dataclasses import dataclass
import cv2
import numpy as np


@dataclass
class Point:
    x: int
    y: int


def orientation(p, q, r):
    val = (r.x - q.x) * (p.y - q.y) - (r.y - q.y) * (p.x - q.x)
    if val == 0:
        return 0
    if val > 0:
        return 1
    return 2


def find_convex_hull(points):
    n = len(points)
    convex_hull_points = []
    left_most_point = 0
    for ind, p in enumerate(points):
        if p.x < points[left_most_point].x:
            left_most_point = ind
    hull_point = left_most_point
    while True:
        convex_hull_points.append(points[hull_point])
        next_point = (hull_point + 1) % n
        for i in range(n):
            if orientation(points[hull_point], points[i], points[next_point]) == 2:
                next_point = i
        hull_point = next_point
        if hull_point == left_most_point:
            break
    return convex_hull_points


def plot(points):
    cv2.namedWindow('output', cv2.WINDOW_NORMAL)
    img = np.ones((600, 600, 3)) * 255
    convex_hull_points = find_convex_hull(points=points)
    for p in points:
        img = cv2.circle(img, (p.x, p.y), 1, (0, 0, 255), -1)
    for ind, _ in enumerate(convex_hull_points):
        start_point = (convex_hull_points[ind].x, convex_hull_points[ind].y)
        end_point = (convex_hull_points[(ind + 1) % len(convex_hull_points)].x, convex_hull_points[(ind + 1) % len(convex_hull_points)].y)
        img = cv2.line(img, start_point, end_point, (0, 255, 0), 1)
    cv2.imshow('output', img)
    cv2.waitKey(0)


if __name__ == "__main__":
    points = []
    points.append(Point(0, 300))
    points.append(Point(20, 200))
    points.append(Point(10, 100))
    points.append(Point(150, 10))
    points.append(Point(300, 10))
    points.append(Point(200, 10))
    points.append(Point(30, 150))
    points.append(Point(300, 120))
    points.append(Point(110, 20))
    points.append(Point(310, 300))
    points.append(Point(510, 100))
    print(points)
    plot(points)
