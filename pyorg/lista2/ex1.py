#1 Faça um programa que pergunte o preço de três produtos e 
# informe qual produto mais barato.
print('Cheapest product')
product1 = float(input('Enter the price of the first product: '))
product2 = float(input('Enter the price of the second product: '))
product3 = float(input('Enter the price of the third product: '))

def check_cheapest_product():
    products_list = [product1, product2, product3]
    products_list.sort()
    print(f'The cheapest product costs: {products_list[0]}')

check_cheapest_product()