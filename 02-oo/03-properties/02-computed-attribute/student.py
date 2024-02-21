class BMICalculator:
    def __init__(self, weight_in_kg, height_in_m):
        self.weight_in_kg = weight_in_kg
        self.height_in_kg = height_in_m
    
    @property
    def bmi(self):
        return self.weight_in_kg / self.height_in_kg ** 2
    
    @property
    def category(self):
        if self.bmi < 18.5:
            return "underweight"
        elif 18.5 < self.bmi <= 25:
            return "normal"
        else:
            return "overweight"


calc = BMICalculator(weight_in_kg=80, height_in_m=1.80)
print(calc.bmi)