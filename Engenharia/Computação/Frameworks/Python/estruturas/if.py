try:
    varI = int(input("Digite um Valor Numérico Inteiro: "))
    varII = int(input("Digite um Valor Numérico Inteiro Comparativo: "))

    if varI >= varII:
        print("O valor digitado é maior ou igual ao segundo!")
   
except ValueError:
    print("Entrada inválida. Por favor, digite apenas números inteiros.")