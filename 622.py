# Реализовать класс Road (дорога)

class Road:
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def mass_asphalt(self, mas1m, depth):
        print(f"{int((self._length * self._width * mas1m * depth) / 1000)} т.")


asf = Road(50, 2000)
asf.mass_asphalt(25, 5)
