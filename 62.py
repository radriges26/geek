# Реализовать класс Road (дорога)

class Road:
    def __init__(self):
        self._width = 20
        self._length = 5000

    def mass_asphalt(self, mas1m, depth):
        print(f"{int((self._length * self._width * mas1m * depth) / 1000)} т.")


asf = Road()
asf.mass_asphalt(25, 5)
