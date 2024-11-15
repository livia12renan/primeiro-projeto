idadePet = int (input("ola caro cliente qual a idade do seu cachorro? responda com numeros reais: ")) 
nomePet = str (input("qual nome do seu pet? "))
portePet = int (input("qual é o porte do seu pet, porfavor digite 1 para grande, 2 para médio , 3 para pequeno: "))
qtdBanho = int (input("qual é a quantidade de banho do seu pet  no ano: "))

if portePet == 1: print(input(f"obrigado cliente a idade humana do {nomePet} é {idadePet*7} anos, e nos últimos 12 meses ele nos visitou {qtdBanho}  vezes, gerando R$ {55*qtdBanho}) de lucro"))

elif portePet == 2: print(input(f"obrigado cliente a idade humana do {nomePet} é {idadePet*7} anos e nos últimos 12 meses ele nos visitou {qtdBanho} vezes, gerando R$ {45*qtdBanho} de lucro"))

elif portePet == 3: print(input(f"obrigado cliente a idade humana do {nomePet} é {idadePet*7} anos e nos últimos 12 meses ele nos visitou {qtdBanho} vezes, gerando R$ {45*qtdBanho} de lucro"))

