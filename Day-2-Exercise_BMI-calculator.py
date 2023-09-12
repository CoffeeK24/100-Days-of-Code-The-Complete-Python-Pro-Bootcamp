# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_n=float(height)
weight_n=float(weight)
bmi=weight_n/height_n**2
print(int(bmi))