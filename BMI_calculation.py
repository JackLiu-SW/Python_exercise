height = float(input('My height is:'))
weight = float(input('My weight is:'))
print('Your height is', height, 'cm, ', 'your weight is', weight, 'kg')
bmi_calculation = weight / (height / 100)**2
print('Your BMI is', bmi_calculation)
if bmi_calculation < 18.5:
    print('Underweight')
elif bmi_calculation >=18.5 and bmi_calculation < 25:
    print('Normal')
elif bmi_calculation >=25 and bmi_calculation < 30:
    print('Overwright')
elif bmi_calculation >=30 and bmi_calculation < 35:
    print('Obese Class I')
elif bmi_calculation >=35 and bmi_calculation < 40:
    print('Obese Class II')
else:
    print('Obese Class III')