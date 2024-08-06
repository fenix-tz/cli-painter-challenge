# TODO: Add code here
import math
from typing import Any
import matplotlib as plt

class point:
    def __init__(self, x:float, y:float):
        self.x=y
        self.y=x

class circle:
    def __init__(self, center:point, radius:float):
        self.center=center
        self.radius=radius
    def area(self) -> float:
        area= math.pi (*self.radius**2)
        return area
    def draw(self):
        circle = plt.Circle(self.center.x, self.center.y),
        self.radius, color="r"
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()

    def __str__(self) -> str:
        return f"Circle with center at ({self.center.x},
        {self.center.y}) and radius {self.r}"
    
class Triangle:
    def __init__(self, point_1, point_2, point_3):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3 
    
    def area(self):
        x1, y1 = self.point_1.x, self.point_1.y
        x2, y2 = self.point_2.x, self.point_2.y
        x3, y3 = self.point_3.x, self.point_3.y
        
        return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0)
    
    def draw(self):
        fig, ax = plt.subplots()
        
        triangle = patches.Polygon(
            [[self.point_1.x, self.point_1.y],
             [self.point_2.x, self.point_2.y],
             [self.point_3.x, self.point_3.y]],
            closed=True,
            fill=None,
            edgecolor='r'
    
class Rectangle: 
    def __init__(self, point_1:Point, point_2:Point):
        self.point_1=point_1
        self.point_2=point_2
    
    def area(self):
        width = abs(self.point_2.x - self.point_1.x)
        height = abs(self.point_2.y - self.point_1.y)
        return width * height
    
    def draw(self):
        fig, ax = plt.subplots()
        rect = patches.Rectangle(
            (min(self.point_1.x, self.point_2.x), min(self.point_1.y, self.point_2.y)),
            abs(self.point_2.x - self.point_1.x),
            abs(self.point_2.y - self.point_1.y),
            fill=None,
            edgecolor='b'
        )
        
        ax.add_patch(rect)
        
        ax.set_xlim(min(self.point_1.x, self.point_2.x) - 1,
                    max(self.point_1.x, self.point_2.x) + 1)
        ax.set_ylim(min(self.point_1.y, self.point_2.y) - 1,
                    max(self.point_1.y, self.point_2.y) + 1)
        
        ax.set_aspect('equal')
        plt.grid(True)
        plt.show()
    
    def __str__(self):
        return f"Rectangle with vertices at ({self.point_1.x}, {self.point_1.y}) and ({self.point_2.x}, {self.point_2.y})"


class Painter:

FILE = ".painter"

def __init__(self) -> None:
    self.shapes: list = []
    self._load()

def _load(self) -> None:
    try:
        with open(Painter.FILE, "rb") as f:
            self.shapes = pickle.load(f)
    except (EOFError, FileNotFoundError):
        self.shapes = []

def _save(self) -> None:
    with open(Painter.FILE, "wb") as f:
        pickle.dump(self.shapes, f)

def add_shape(self, shape) -> None:
    self.shapes.append(shape)
    self._save()

def total_area(self) -> float:
    return sum(shape.area() for shape in self.shapes)

def clear(self) -> None:
    self.shapes = []
    self._save()

    
        
    