import turtle

def bmi(weight, height):
    height /= 100
    result = weight / (height * height)
    return result

while True:
    weight = float(turtle.textinput("BMI", "몸무게"))
    height = float(turtle.textinput("BMI", "키"))
    
    if weight == 0:
        break
    
    bmi_value = bmi(weight,height)
    print(bmi_value)
    
turtle.bye()