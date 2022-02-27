class Calorie:
    """Represent optimal calroie amount a person needs to take today 
    BMR = 10*weight +6.25Height -5*age - 10*temperature"""

    def __init__(self, weight, height, age, temperature):
        self.temperature = temperature
        self.weight = weight
        self.age = age
        self.height = height

    def calculate(self):
        result = 10 * self.weight + 6.5 * self.height - 5 - self.temperature * 10
        return result

if __name__ == "__main__":
    temperature = Temperature(country="",city="").get()
    calorie = Calorie(weight=70,height=175,age=32,temperature=temperature)
    print(calorie.calculate())