#!/usr/bin/python3
"""saquare comments"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class"""
    def __init__(self, size, x=0, y=0, id=None):
        """init"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return a string"""
        return (f"[{self.__class__.__name__}] ({self.id}) \
{self.x}/{self.y} - {self.size}")

    @property
    def size(self):
        """getter"""
        return self.width

    @size.setter
    def size(self, value):
        """getter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """function"""
        i = 0
        if args is not None and len(args) != 0:
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
                i += 1
        else:
            if kwargs is not None and len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    if key == "size":
                        self.width = value
                    if key == "x":
                        self.x = value
                    if key == "y":
                        self.y = value

    def to_dictionary(self):
        """dictionary"""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
