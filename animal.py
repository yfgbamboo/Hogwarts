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
    Miao = Cat("Miaomiao",'grey','2','girl')
    action = Miao.catch_mouse()
    print(f'{Miao.name},with {Miao.color} color,{Miao.age} years old,{Miao.gender},',action)


    puppy = Dog("Puppy",'white','3','boy')
    puppy.watch_house()
    print(f'name:{puppy.name},color:{puppy.color},age:{puppy.age},gender:{puppy.gender},hair:{puppy.hair}')