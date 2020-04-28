class Mammal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        print("Hello I'm Mammal")

    def walk(self):
        print(f"Walk {self.name} {self.color}")


class Cat(Mammal):
    def __init__(self, name, color, is_male):
        Mammal.__init__(self, name, color)
        self.isBarge = is_male

    def walk(self):
        print("Walk of Cat")


cat = Cat(name='Cat', color='Red', is_male=True)
print(cat.walk())

mamal = Mammal('Dog', 'blue')
print(mamal.name)
print(mamal.walk())
