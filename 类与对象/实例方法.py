class Car:
    def __init__(self, brand, name, price):
        self.brand = brand
        self.name = name
        self.price = price
    def running (self):
        print(f"{self.brand} {self.name} {self.price}")
    def cost(self,discount,rate):
        return discount * rate * self.price
c1=Car("bba","bb",1000)
print(c1.cost(5,2))
c1.running()
print(c1.__dict__)