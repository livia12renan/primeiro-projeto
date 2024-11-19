#solicita ao usuário que insira um número
numero = int(input("por favor insira o número de sua matrícula:"))

#verifica se o número é par ou ímpar
if numero % 2 == 0:
    print(f"você está no time azul.")

else:
    print(f"você está no time amarelo.")