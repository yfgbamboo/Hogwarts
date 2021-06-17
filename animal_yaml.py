import yaml

class Animal:
    def __init__(self,name,color,age,gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def speak(self):
        print(f'{self.name} can speak')

    def run(self):
        print(f'{self.name} can run')


class Cat(Animal):


    def __init__(self,name,color,age,gender):
        self.hair = "short"
        super().__init__(name,color,age,gender)


    def catch_mouse(self):
        return "caught one mouse"

    def speak(self):
        print(f'{self.name} can Meow')

class Dog(Animal):
    def __init__(self,name,color,age,gender):
        self.hair = "long"
        super().__init__(name,color,age,gender)

    def watch_house(self):
        print(f'{self.name} can watch house')

    def speak(self):
        print(f'{self.name} can wang')

if __name__ == '__main__':
    with open('./datas/animal.yaml',encoding="utf8") as f:
        datas = yaml.safe_load(f)
            # print(datas)
    data = datas['default']

    animal = Animal(data['name'],data['color'],data['age'],data['gender'])
    print(f'{animal.name},with {animal.color} color,{animal.age} years old,{animal.gender}')
