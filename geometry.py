import math

EPSILON = 1e-15


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({} {})".format(self.x, self.y)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def round(self):
        return Point(round(self.x), round(self.y))

    def distance(self, p):
        return math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)

    def distance2(self, p):
        """square of the distance"""
        return (self.x - p.x) ** 2 + (self.y - p.y) ** 2

    def closest(self, a, b):
        """ return the closest point on the line a-b"""
        da = b.y - a.y
        db = a.x - b.x
        c1 = da * a.x + db * a.y
        c2 = -db * self.x + da * self.y
        det = da * da + db * db
        if det != 0:
            cx = (da * c1 - db * c2) / det
            cy = (da * c2 + db * c1) / det
        else:  # The point is already on the line
            cx = self.x
            cy = self.y
        return Point(cx, cy)


# TODO : same with an angle ?


class Vector(object):
    def __init__(self, vx, vy):
        self.v = (vx, vy)
        self.vx = vx
        self.vy = vy
        self.length = abs(self)
        self.norm = self
        if abs(self.length - 1) > EPSILON and self.length != 0:
            self.norm = Vector(self.vx / self.length, self.vy / self.length)

    def __str__(self):
        return "({} {})".format(self.vx, self.vy)

    def __abs__(self):
        return math.sqrt(self.vx ** 2 + self.vy ** 2)

    def round(self):
        return Vector(round(self.vx), round(self.vy))
