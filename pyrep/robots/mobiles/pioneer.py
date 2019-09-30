from pyrep.robots.mobiles.nonholonomic_base import NonHolonomicBase


class Pioneer_p3dx(NonHolonomicBase):
    def __init__(self, count: int = 0):
        super().__init__(count, 2, 'Pioneer_p3dx')
