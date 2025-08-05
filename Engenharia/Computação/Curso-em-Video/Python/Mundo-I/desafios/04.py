# Faça um programa que leia algo pelo teclado o seu tipo primitivo e todas as informações possíveis sobre ele.

string = str(input("Digite um Texto:")) 
floating = float(input("Digite um Valor Real:"))
boolean = bool(input("Digite um Valor Lógico:"))
integer = int(input("Digite um Valor Inteiro: ")) 

print("A 1º linha é do tipo:",type(string))
print("A 2º linha é do tipo:",type(floating))
print("A 3º linha é do tipo:",type(boolean))
print("A 4º linha é do tipo:",type(integer))