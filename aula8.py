frutas= ['abacaxi','banana','pitaya','morango','uva']
print(frutas[2])

numeros= [1,2,3,4,5,2,1,2,23,23,4,2]
lista= list(numeros)
print (lista)

meses= ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro"]
for i in meses:
    print(i)

notas= [10,8,8,7,10,3]
notas_tuplas= tuple(notas)
print(notas_tuplas[0])

ponto= (23,43,65)
x,y,z=ponto
print(f'Coordenada: {x}')
print(f'Coordenada: {y}')
print(f'Coordenada: {z}')