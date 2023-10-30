# Exercício Python 25: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

numero= {}

for i in range(0,6):
    n= int(input("digite o numero"))
    if n %2 ==0:
        numero.append(n) 

        soma=sum(numero)
        print(soma)