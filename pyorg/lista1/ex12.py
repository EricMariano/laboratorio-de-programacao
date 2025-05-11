# 12 Tendo como dados de entrada a altura e o peso de uma pessoa, construa um algoritmo que calcule o seu peso ideal e o seu IMC usando a seguinte fórmula: 
# para homens 52 + (0.75 × (altura - 152.4) para mulheres 52 + (0.67 × (altura - 152.4) para IMC peso (kg) / [altura (m)]²

print('BMI Calculator!')
gender = input('Enter your gender M for male and F for female: ').casefold

if gender == 'm' or gender == 'male':
    heigth = float(input('Enter your heigth in cm: '))
    weigth = float(input('Enter your weigth in kg: '))
    fineWeigth = 52 + (0.75 * (heigth - 152.4))
    bmi = weigth / (heigth)**2
    print(f'Your ideal weigth is {fineWeigth:.1f}Kg and your BMI is {bmi}kg/m²')
    
else: 
    heigth = float(input('Enter your heigth in cm: '))
    weigth = float(input('Enter your wigth in kg: '))
    fineWeigth = 52 + (0.67 * (heigth - 152.4))
    bmi = weigth / (heigth)**2
    print(f'Your ideal weigth is {fineWeigth:.1f}Kg and your BMI is {bmi}kg/m²')
