class Car():
    def __init__(self, brand, kind, model):
        self.brand = brand
        self.kind = kind
        self.model = model
    
    
    def start(self):
        print(f"The {self.kind} {self.brand} {self.model} is start")

    def stop(self):
        print(f"The {self.kind} {self.brand} {self.model} is stopped")
        
prius = Car('Toyota','hatchback','Prius')

prius.start()
prius.stop()

        