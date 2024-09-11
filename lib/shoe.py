#!/usr/bin/env python3

import sys

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = 'New'  # Initial condition is 'New'

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer", file=sys.stdout)
        else:
            self._size = value

    def cobble(self):
        self.condition = 'New'  # Set condition to 'New' after repair
        print("Your shoe is as good as new!")
