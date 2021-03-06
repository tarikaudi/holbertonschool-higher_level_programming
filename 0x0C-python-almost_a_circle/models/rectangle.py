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

    def update(self, *args, **kwargs):
        """function"""
        i = 0
        if args is not None and len(args) != 0:
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.__width = arg
                if i == 2:
                    self.__height = arg
                if i == 3:
                    self.__x = arg
                if i == 4:
                    self.__y = arg
                i += 1
        else:
            if kwargs is not None and len(kwargs) != 0:
                for key, value in kwargs.items():
                    """print(f"{key}:{value}")"""
                    if key == "id":
                        self.id = value
                    if key == "width":
                        self.width = value
                    if key == "height":
                        self.height = value
                    if key == "x":
                        self.x = value
                    if key == "y":
                        self.y = value

    def to_dictionary(self):
        """__dict__ representation of rectangle"""
        return {"id": self.id, "width": self.__width,
                "height": self.__height, "x": self.__x, "y": self.__y}
