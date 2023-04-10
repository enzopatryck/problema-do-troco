#Problema do Troco
#Algoritmo Guloso

moedasStr = input("Insira os valores das moedas separados por vírgula (,): ")
moedas =  [int(i) for i in moedasStr.split(",")]
troco = int(input("Insira o valor do troco a ser recebido: "))
resto = troco
total = 0

moedas.sort(reverse = True)

for i in moedas:
    quoInt = resto // i 
    if quoInt > 0:
        total += quoInt
        resto = resto % i
    elif quoInt == 0:
        continue

def resultado():
    if resto != 0:
        print(f"O número de moedas será: {total} e restará {resto} centavo(s)")
    else:
        print(f"O número de moedas será: {total}")

resultado()