from temperature import Temperature

class Calories:

    def __init__(self,weight, height, age,temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature


    def calculate(self):
        result = 10.0 * float(self.weight) + 6.5 * float(self.height) + 5.0 - self.temperature
        return result



if __name__ == "__main__":
    temperature = Temperature(country= 'india', city= 'pune').get()
    calorie = Calories(72, 177, 22,temperature)
    print(calorie.calculate())




