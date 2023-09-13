from kiutils.board import Board
from kiutils.items.gritems import GrCircle
from kiutils.items.common import Position

import math
import sys

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy

def define_circle(p1, p2, p3):
    """
    Returns the center and radius of the circle passing the given 3 points.
    In case the 3 points form a line, returns (None, infinity).
    """
    temp = p2[0] * p2[0] + p2[1] * p2[1]
    bc = (p1[0] * p1[0] + p1[1] * p1[1] - temp) / 2
    cd = (temp - p3[0] * p3[0] - p3[1] * p3[1]) / 2
    det = (p1[0] - p2[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p2[1])
    
    if abs(det) < 1.0e-6:
        return (None, np.inf)
    
    # Center of circle
    cx = (bc*(p2[1] - p3[1]) - cd*(p1[1] - p2[1])) / det
    cy = ((p1[0] - p2[0]) * cd - (p2[0] - p3[0]) * bc) / det
    
    return round(cx, 4), round(cy, 4)

def get_visited_points(board):
    visited_points = set()

    for footprint in board.footprints:
        visited_points.add((footprint.position.X, footprint.position.Y))

    for graphicItem in board.graphicItems:
        if graphicItem.layer == 'Edge.Cuts':
            if type(graphicItem).__name__ == 'GrLine':
                visited_points.add((graphicItem.start.X, graphicItem.start.Y))
                visited_points.add((graphicItem.end.X, graphicItem.end.Y))
            if type(graphicItem).__name__ == 'GrArc':
                visited_points.add((graphicItem.start.X, graphicItem.start.Y))
                visited_points.add((graphicItem.end.X, graphicItem.end.Y))
                visited_points.add(define_circle(
                    (graphicItem.start.X, graphicItem.start.Y),
                    (graphicItem.mid.X, graphicItem.mid.Y),
                    (graphicItem.end.X, graphicItem.end.Y)))

    return visited_points

def translate(origin, points):
    result = set()
    for x, y in points:
        x1 = x - origin[0]
        y1 = y - origin[1]
        x2, y2 = rotate((0, 0), (x1, y1), math.pi / 36)
        x3, y3 = x2 + 50, y2 + 50
        result.add((x3, y3))
    return result

def read_markers_from_file():
    with open('geometry.txt') as file:
        contents = file.read()

    head, body = contents.split('\n\n')
    x, y = head.strip().split()
    origin = (float(x), float(y))

    points = {(0.0, 0.0)}

    for line in body.splitlines():
        x, y = line.strip().split()
        points.add((float(x), float(y)))

    return translate(origin, points)

def remove_markers(board):
    board.graphicItems = [graphicItem for graphicItem in board.graphicItems if not type(graphicItem).__name__ == 'GrCircle']

def minimum_distance(point, others):
    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    result = 9999
    for other in others:
        result = min(result, distance(point, other))

    return result

def add_markers(board):
    positive_markers = read_markers_from_file()
    negative_markers = get_visited_points(board)
    markers = set()

    for positive_marker in positive_markers:
        if minimum_distance(positive_marker, negative_markers) >= 0.0001:
            markers.add(positive_marker)

    # uncomment to show all markers regardless of correctly placed items
    #markers = positive_markers

    for marker in markers:
        board.graphicItems.append(GrCircle(center=Position(marker[0], marker[1], 0), end=Position(marker[0] + 0.2, marker[1] + 0.2, 0), layer='Edge.Cuts', width=0.15))
        board.graphicItems.append(GrCircle(center=Position(marker[0], marker[1], 0), end=Position(marker[0] + 0.2, marker[1] + 0.2, 0), layer='F.Cu', width=0.15))

board = Board.from_file(sys.argv[1])
remove_markers(board)
add_markers(board)
board.to_file(sys.argv[1])
