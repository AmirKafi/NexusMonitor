from domain.component import Component


class GPU(Component):
    def __init__(self, name):
        super().__init__(name)
        self.clock = 0.0

    def update_clock(self,clock:float):
        self.clock = clock

    @property
    def gpu_clock(self):
        return f"{self.clock} MHz"