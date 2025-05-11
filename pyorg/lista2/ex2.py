#2 Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = float(input('Enter a number: '))
n2 = float(input('Enter another number: '))
n3 = float(input('Enter a third number: '))

def descending_order():
    numbers_list = [n1, n2, n3]
    numbers_list.sort(reverse=True)
    print(numbers_list)

descending_order()