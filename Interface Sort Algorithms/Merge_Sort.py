import matplotlib.pyplot as plot
import random 

class MergeSort:
    def __init__(self):
        self.lista = []
        self.listas = []

    def insert_sample(self,lista):
        for i in lista:
            self.lista.append(i)
        self.listas1()
    
    def mostrar(self):
        for i in self.lista:
            print(i, end=", ")
        print()

    def merge(self,lista,izq,der):
        i = j = k = 0

        while i < len(izq) and j < len(der):
            if izq[i] < der[j]:
                lista[k] = izq[i]
                i += 1 
            else:
                lista[k] = der[j]
                j += 1
            k += 1
            
            self.listas1()
        
        while i<len(izq):
            lista[k] = izq[i]
            self.listas1()
            i += 1
            k += 1
        
        while j<len(der):
            lista[k] = der[j]
            self.listas1()
            j += 1
            k += 1

    def rec_merge_sort(self,lista):
        if len(lista)>1:    
            mid = len(lista) // 2
            izq = lista[:mid]
            der = lista[mid:]

            self.rec_merge_sort(izq)
            self.rec_merge_sort(der)
            
            self.merge(lista,izq,der)
            self.listas1()
    
    def merge_sort(self):
        self.steps = 0
        self.rec_merge_sort(self.lista)
    
    def listas1(self):
        lista = []
        igual = True
        if(len(self.listas) > 0):
            for i in range(len(self.lista)):
                if(self.lista[i] == self.listas[len(self.listas)-1][i]):
                    igual = True
                else:
                    igual = False
                    break
            if(igual == False):
                for i in self.lista:
                    lista.append(i)
                self.listas.append(lista)
        else:
            for i in self.lista:
                lista.append(i)
            self.listas.append(lista)
    
    def ordena(self,i,grafica):
        for barra,valor in zip(grafica,self.listas[i]):
            barra.set_height(valor)
        return grafica

class MergeSort2:
    def __init__(self):
        self.lista = []
        self.lista2 = []
        self.steps = 0
        
    def insert_sample(self,lista):
        self.lista = []
        for i in lista:
            self.lista.append(i)
        
    def mostrar(self):
        for i in self.lista:
            print(i, end = ", ")
            
        print()

    def merge(self,lista, izq, der):
        i = j = k = 0
        
        while i<len(izq) and j<len(der):
            if izq[i] < der[j]:
                lista[k] = izq[i]
                i += 1
            else:
                lista[k] = der[j]
                j += 1
                
            self.steps += 1
            
            k += 1
            
        while i<len(izq):
            lista[k] = izq[i]
            i += 1
            k += 1
            self.steps += 1
            
            
        while j<len(der):
            lista[k] == der[j]
            j += 1
            k += 1
            self.steps += 1


    def rec_merge_sort(self, lista):
        if len(lista) > 1:
            mid = len(lista)//2
            izq = lista[:mid]
            der = lista[mid:]
            
            self.rec_merge_sort(izq)
            self.rec_merge_sort(der)
            
            self.merge(lista, izq, der)
            
        
    def ordenagraf(self):
        self.steps = 0
        self.rec_merge_sort(self.lista)