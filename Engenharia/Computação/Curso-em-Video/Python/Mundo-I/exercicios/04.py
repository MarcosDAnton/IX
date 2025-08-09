# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = input(int(bool(float(str("Digite algo:")))))

print("Você digitou: ",algo, " e é do tipo ", type(algo))
