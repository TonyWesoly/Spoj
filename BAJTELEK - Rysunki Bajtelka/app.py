import enum

class Position_of_point(enum.Enum):
    Inside = 1
    Outside = 2
    On_poligon = 3


class Vector_2d:
    def __init__(self,x,y):
        self.x = x
        self.y = y

#  @return: > 0: Query point lies on left of the line.
#           = 0: Query point lies on the line.
#           < 0: Query point lies on right of the line.
def substitude_point_in_line(pt1, pt2, query_point):
    return ((query_point.y - pt1.y) * (pt2.x - pt1.x)) - ((query_point.x - pt1.x) * (pt2.y - pt1.y))

#  @return  = 1: query_point lies inside the polygon.
#           = 0: query_point lies on the polygon.
#           =-1: query_point lies outside the polygon.
def is_point_inside_poligon(query_point, vertices):
    wn = 0
    num_sides_of_poligon = len(vertices)

    for i in range(num_sides_of_poligon):
        point_in_line = substitude_point_in_line(vertices[i],vertices[(i + 1) % num_sides_of_poligon], query_point)
        
        if point_in_line == 0:
            return Position_of_point.On_poligon