#!/usr/bin/python3
"""class"""


class MyInt(int):
    """class my int"""

    def __eq__(self, num):
        """equality"""
        return (super().__ne__(num))

    def __ne__(self, num):
        """inequality"""
        return (super().__eq__(num))
