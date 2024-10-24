import random
import time
import matplotlib.pyplot as plot

class Radix:
    
    def __init__(self):
        self.lista = []
        self.listas = []
        self.steps = 0
        
    def insert_sample(self, lista):
        self.lista = []
        for i in lista:
            self.lista.append(i)
        
    def mostrar(self):
        for i in self.lista:
            print(i, end = ", ")
            
        print()

    def listas1(self):
        lista = []
        for i in self.lista:
            lista.append(i)
        self.listas.append(lista)


    def counting_b10(self, exp):
        lista_conteo = [0]*10
        for i in self.lista:
            indice = i // exp
            lista_conteo[indice%10]+=1
            self.steps +=1
        
        for i in range(1, len(lista_conteo)):
            lista_conteo[i] += lista_conteo[i-1]
            self.steps +=1
            
            
        lista_salida = [0]*(len(self.lista))
    
        for i in range(len(self.lista)-1, -1, -1):
            indice = self.lista[i]//exp
            
            lista_salida[lista_conteo[indice%10] -1] = self.lista[i]
            
            lista_conteo[indice%10] -= 1
            self.steps +=1
            
        for i in range(len(lista_salida)):
            self.lista[i] = lista_salida[i]
            self.steps +=1
            
            self.listas1()
            
            
    def ordenagraf(self):
        self.steps = 0
        maximo = max(self.lista)
        exp = 1
        while maximo//exp > 0:
            self.counting_b10(exp)
            exp *= 10

    def ordena(self,i,grafica):
        self.listas[i]
        for barra,valor in zip(grafica,self.listas[i]):
            barra.set_height(valor)
        return grafica
        #self.graficar(self.insert_lista2(self.lista), self.lista)