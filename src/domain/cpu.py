from domain.component import Component

class CPU(Component):
    def __init__(self,name:str):
        super().__init__(name=name)
        self.cores_count = 0

    def update_cores_count(self,count:int):
        self.cores_count = count