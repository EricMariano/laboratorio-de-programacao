# 17.Faça um Programa para uma loja de tintas. O programa 
# deverá pedir o tamanho em metros² da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros²
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 
# ou em galões de 3,6 litros, que custam R$ 25,00.

#uma lata cobre 108m² -> um galao cobre 21.6m² três galões pintam 64.8 m²
metersForPaint = float(input('Enter the size of the area to be painted: '))


def isGalao():
    galao = metersForPaint / 21.6 
    priceGalao = 25.0

    if metersForPaint % 21.6 != 0:  
        galao = int(galao) + 1
        price = galao * priceGalao
        print(f"The number of paint's cans required is {galao} and the price is ${price}")
    else: 
        galao = int(galao)
        price = galao * priceGalao
        print(f"The number of paint's cans required is {galao} and the price is ${price}")

def isLata():
    lata = metersForPaint / 108
    priceLata = 80.00
    if metersForPaint % 108 != 0:
        lata = int(lata) + 1
        price = lata * priceLata
        print(f"The number of paint's cans required is {lata} and the price is ${price}")

    else:
        lata = int(lata)
        price = lata * priceLata
        print(f"The number of paint's cans required is {lata} and the price is ${price}")


if metersForPaint <= 64.8:
    isGalao()
else:
    isLata()
