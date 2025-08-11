# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = input("Digite algo: ")

print("O tipo primitivo do valor dado é ", type(algo))
print("É numérico?", algo.isnumeric())
print("É alfabético?", algo.isalpha())
print("É alfanumérico?", algo.isalnum())
print("Tem só letras maiusculas?", algo.isupper())
print("Tem só letras minisuculas?", algo.islower())
print("Está titularizado?", algo.istitle())
print("É um número decimal?", algo.isdecimal())
print("Só tem espaços?", algo.isspace())
print("Está dentro do padrão ASCII de 7 bits?", algo.isascii())