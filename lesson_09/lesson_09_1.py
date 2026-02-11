from ctypes.wintypes import PHKEY


class Rhombus:

    def __init__(self, **kwargs):
        if kwargs.get('side') > 0:
            self.side = kwargs.get('side')
        else:
            raise ValueError("side cannot be less than 0")
        if (kwargs.get('tangle_a') + kwargs.get('tangle_b')) == 180:
            self.tangle_a = kwargs.get('tangle_a')
            self.tangle_b = kwargs.get('tangle_b')
        else:
            raise ValueError("sum a + b tangles must be equal to 180")

rhombus_1 = Rhombus(side=5, tangle_a=60, tangle_b=120)


