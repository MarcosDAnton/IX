caractere = input("Digite um Texto: ")
inteiro = int(input("Digite um Número Inteiro: "))
real = float(input("Digite um Número Real: "))

# Para booleano, é comum verificar se a entrada não está vazia ou um valor específico
# Uma forma simples é considerar True para qualquer entrada e False para entrada vazia
# Ou, mais comumente, verificar "True" ou "False"
booleano_input = input("Digite 'True' ou 'False' (ou deixe vazio para False): ")
booleano = booleano_input.lower() == 'true'

print(f"\nVariável 'caractere': {caractere} (Tipo: {type(caractere)})")
print(f"Variável 'inteiro': {inteiro} (Tipo: {type(inteiro)})")
print(f"Variável 'real': {real} (Tipo: {type(real)})")
print(f"Variável 'booleano': {booleano} (Tipo: {type(booleano)})")