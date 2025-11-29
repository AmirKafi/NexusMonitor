class Component:
    def __init__(self,name:str):
        self.name = name
        self.usage = 0
        self.temp = 0

    def update_temp(self,temp:int):
        self.temp = temp

    
    def update_usage(self,usage:int):
        self.usage = usage
    