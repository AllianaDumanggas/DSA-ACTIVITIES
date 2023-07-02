class Animal:
    def __init__(self,name):
        self.name = name
        self.birth= "An Animal has been born"

    def eat(self):
       return print("Munch munch")
    def make_noise(self):
       return print("Grrr says ", self.name)
    def get_name(self):
        return print("This Animal name is: ", self.name)
    def set_name(self):
        self.name
    def give_birth(self):
        return print(self.birth)

class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
        self.name =name
        self.birth= "A Cat has been born"
    def make_noise(self):
        return print("Meow says", self.name)
    def get_name(self):
        return print("This Cat name is: ",self.name)
    def set_name(self):
        self.name
    def give_birth(self):
        return print(self.birth)


class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
        self.name=name
        self.birth= "A dog has been born"
    def make_noise(self):
        return print("Bark says ", self.name)
    def get_name(self):
        return print("This Dog name is: ",self.name)
    def set_name(self):
        self.name
    def give_birth(self):
        return print(self.birth)







