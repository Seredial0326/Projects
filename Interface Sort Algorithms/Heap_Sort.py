import random

class OrdenaHeap:
    def __init__(self):
        self.lista = []
        self.listas = []
        self.n = 0
    
    def insert_sample(self,lista):
        for i in lista:
            self.lista.append(i)
        self.n = len(self.lista)
        self.listas1()

    def mostrar(self):
        for i in self.lista:
            print(i, end=", ")
        
        print()      

    def heapify(self,i):
        h_izq = 2*i+1
        h_der = 2*i+2

        if h_izq < self.n and self.lista[i] < self.lista[h_izq]:
            mayor = h_izq
        else:
            mayor = i

        if h_der < self.n and self.lista[mayor] < self.lista[h_der]:
            mayor = h_der
        
        if mayor!=i: 
            self.lista[i], self.lista[mayor] = self.lista[mayor], self.lista[i]
            self.listas1()
            self.heapify(mayor)

    def heap_sort(self):
        for i in range(self.n//2 -1,-1,-1):
            self.heapify(i)   


        for i in range(self.n-1,0,-1):
            self.lista[0],self.lista[i] = self.lista[i],self.lista[0]
            self.n = i
            self.heapify(0)
            self.listas1()            

    def listas1(self):
        lista = []
        for i in self.lista:
            lista.append(i)
        self.listas.append(lista)
    
    def ordena(self,i,grafica):
        self.listas[i]
        for barra,valor in zip(grafica,self.listas[i]):
            barra.set_height(valor)
        return grafica

class OrdenaHeap2:
    def __init__(self):
        self.lista = []
        self.listas = []
        self.steps = 0
    
    def insert_sample(self,lista):
        self.lista = []
        for i in lista:
            self.lista.append(i)

    def heapify(self, n, i):
        h_izq = 2 * i + 1
        h_der = 2 * i + 2
        
        if h_izq < n and self.lista[i] < self.lista[h_izq]:
            mayor = h_izq
        else:
            mayor = i
            
        if h_der < n and self.lista[mayor] < self.lista[h_der]:
            mayor = h_der
        
        if mayor != i:
            self.lista[i], self.lista[mayor] = self.lista[mayor], self.lista[i]
            self.steps += 1
            self.heapify(n, mayor)
        else:
            return


    def ordenagraf(self):
        self.steps = 0
        n = len(self.lista)
        for i in range(n//2 - 1, -1, -1):
            self.heapify(n, i)
            
        for i in range(n-1, 0, -1):
            self.lista[0], self.lista[i] = self.lista[i], self.lista[0]
            self.heapify(i, 0)

