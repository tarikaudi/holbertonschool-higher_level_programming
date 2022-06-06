#!/usr/bin/python3
"""triangle cl"""


from models.base import Base


class Rectangle(Base):
    """"rectanglw class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

 @property
    def width(self):
        """getter widht"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter witdth"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter heig"""
        return self.__height

    @height.setter
    def height(self, value):
        """heig setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """getter x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """return area"""
        return self.__width * self.__height

    def display(self):
        """function display"""
        if self.__height == 0 or self.__width == 0:
            print()
        else:
            if self.__y >= 1:
                for i in range(self.__y):
                    print()
            for f in range(self.__height):
                print(' ' * self.__x + '#' * self.__width)

    def __str__(s):
        """rec rep"""
        return (
            f"[Rectangle] ({s.id}) {s.__x}/{s.__y} - {s.__width}/{s.__height}"
            )

