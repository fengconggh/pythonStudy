class Car:
    wheel = 4
    def __init__(self, color, brand, price):
        self.color = color
        self.brand = brand
        self.price = price
        self.wheel = 2

    def run(self):
        print(f"{self.brand}444444444")

    def __str__(self):
        return f"{self.color}-{self.brand}-{self.price}-{Car.wheel}-{self.wheel}"

    def __eq__(self, other):
        return self.brand == other.brand and self.color == other.color and self.price == other.price

    def __gt__(self, other: Car):
        return self.price > other.price


c1 = Car("red", "BMW", 3010)
c2 = Car("red", "BMW", 300)

print(c1) # red-BMW-3010
print(c2) # red-BMW-300
print(c1 == c2) # False
print(c1 > c2) # True
print(c1.wheel) # 2
print(Car.wheel) # 4
