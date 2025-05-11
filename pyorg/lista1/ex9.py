# 9.Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. (C * 9/5) + 32 = F
# And Fahrenheit to Celsius, asking for the user what converter his want. C = 5 * ((F-32) / 9).

# this question has been changed to a better practice.
def celsiusToFahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheitToCelsius(fahrenheit):
    return 5 * ((fahrenheit - 32) / 9)

def main():
    print("Bem-vindo ao conversor de temperaturas!")
    print("Escolha uma opção:")
    print("1 - Converter Celsius para Fahrenheit")
    print("2 - Converter Fahrenheit para Celsius")
    
    option = input("Digite sua escolha (1 ou 2): ")
    
    if option == "1":
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        fahrenheit = celsiusToFahrenheit(celsius)
        print(f"{celsius:.2f}°C é equivalente a {fahrenheit:.2f}°F.")
    elif option == "2":
        fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
        celsius = fahrenheitToCelsius(fahrenheit)
        print(f"{fahrenheit:.2f}°F é equivalente a {celsius:.2f}°C.")
    else:
        print("Opção inválida. Por favor, reinicie o programa e tente novamente.")

main()
