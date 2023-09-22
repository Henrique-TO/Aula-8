#1
def regressiva():
    contagem= 10
    while contagem>0:
        print (contagem)
        contagem -= 1
    if contagem==0 :
        print ('Fogo!')
#regressiva()

#2
def positivos():
    numero= int(input('insira um numero positivo: '))
    lista= range(1,numero,2)
    soma= sum(lista)
    print(soma)
    print(lista)
#positivos()

#3 Tabuada
def tabuada():
    num=int(input('Tabuada do numero: '))

    for n in range (11):
        print(f'{num} * {n} = {num*n}')
#tabuada()
#4 
def um_a_cem():
    num= 99
    while num != 0:
        print(num)
        num -= 1

#um_a_cem()

#Testando o Random
#1
import random
# aleatorio= random.randint(5,10)
# print (aleatorio)

#2
# x= random.randint(1,10)
# y= random.randint(1,10)
# z= random.randint(1,10)
# print(x,y,z)

#3
bah= random.randrange(10,30)
print(bah)