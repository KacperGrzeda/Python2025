lista = [5, 80.3, 'gruszka' , 9, 'banan', '5,1', 0]
print(lista[2])
lista.append (0.4)
for x in lista:
    if type(x) is float:        
        print(x)