from enum import Enum
from abc import abstractclassmethod
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL  = 1 
    MEDUIM = 2
    LARGE = 3


class Product:
    def __init__(self,name,color,size):
        self.name = name 
        self.color = color
        self.size = size



class ProductFilter:
    def filter_by_color(self,products,color):
        for product in products:
            if product.color == color:
                yield product

    def filter_by_size(self,products,size):
        for product in products:
            if product.size == size:
                yield product

class Specification:
    @abstractclassmethod
    def is_satisfied(self,item):
        pass

product_one = Product("Apple","Green",1)
