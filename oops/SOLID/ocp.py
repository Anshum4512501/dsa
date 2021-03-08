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
class Filter:
    @abstractclassmethod
    def filter(self,item,spec):
        pass

class ColorSpecification(Specification):
    def __init__(self,color) -> None:
        self.color = color
        

    def is_satisfied(self, item):

        return self.color == item.color
class SizeSpecification(Specification):
    def __init__(self,size) -> None:
        self.size = size
        

    def is_satisfied(self, item):

        return self.size == item.size

class BetterFilter(Filter):
    def filter(self,items,spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item
            


apple = Product('Apple', Color.GREEN, Size.SMALL)
tree = Product('Tree', Color.GREEN, Size.LARGE)
house = Product('House', Color.BLUE, Size.LARGE)

products = [apple,tree,house]
spec = ColorSpecification(Color.GREEN)
bf = BetterFilter()
bf.filter(products,spec)