height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
height_n = float(height)
weight_n = float(weight)
bmi = weight_n / height_n**2
print(int(bmi))
