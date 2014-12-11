# -*- coding: utf-8 -*-
weight = float(raw_input("Input your weight:"))
height = float(raw_input("Input your height(cm):"))
count = float(weight/((height*height)/10000))

bmi=round(count,1)

while bmi >=25.0:
    print("Your BMI is "+ str(bmi) + ", you are too fat!")
    break

while 18.5 <= bmi <= 24.9:
    print("Your BMI is "+ str(bmi) + ", you are great!")
    break

while bmi <= 18.4:
    print("Your BMI is "+ str(bmi) + ", you are too skinny!")
    break
