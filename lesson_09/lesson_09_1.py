from ctypes.wintypes import PHKEY


class Rhombus:

    def __init__(self, **kwargs):
        self.side = kwargs.get('side')
        if (kwargs.get('tangle_a') + kwargs.get('tangle_b')) == 180:
            self.tangle_a = kwargs.get('tangle_a')
            self.tangle_b = kwargs.get('tangle_b')
        else:
            raise ValueError("sum a + b tangles must be equal to 180")

    def __setattr__(self, side, value):
        if value > 0:
            super().__setattr__(side, value)
        else:
            raise ValueError("side cannot be less than 0")



rhombus_1 = Rhombus(side=5, tangle_a=60, tangle_b=120)
rhombus_1.__setattr__('side', 6)
print(rhombus_1.__getattribute__('side'))



