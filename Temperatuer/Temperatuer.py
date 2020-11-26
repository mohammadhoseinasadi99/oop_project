class Celsios:
    def __get__(self, instance, owner):
        return instance.value
    def __set__(self, instance, value):
        instance.value = value
class Fahrenheit:
    def __get__(self, instance, owner):
        return  (instance.value * 1.8) + 32
    def __set__(self, instance, value):
        instance.value = (instance.celsios - 32) * (5 / 9)

class Temperatuer:
    def __init__(self, celsios):
        self.celsios = celsios
    celsios = Celsios()
    fahrenheit = Fahrenheit()

temp = Temperatuer(30)
print(temp.celsios, temp.fahrenheit)