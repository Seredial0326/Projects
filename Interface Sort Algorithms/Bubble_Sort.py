import matplotlib.pyplot as plot
import random

class OrdenaBurbuja:
    def __init__(self): 
        self.lista = [] 
        self.steps = 0  
    
    def insert_sample(self,lista):
        for i in lista:
            self.lista.append(i)
    
    def mostrar(self):
        for i in self.lista:
            print(i, end=", ")
        
        print()      

    def ordena(self,i,grafica):
         
        if i<len(self.lista):
            for barra,valor in zip(grafica,self.lista):
                barra.set_height(valor)

            for j in range(len(self.lista)-1-i):
                
                if self.lista[j]>self.lista[j+1]:
                    tempo = self.lista[j]
                    self.lista[j] = self.lista[j+1]
                    self.lista[j+1] = tempo
            
            return grafica
    
    def ordenagraf(self):
        self.steps = 0

        for i in range(len(self.lista)-1):
            for j in range(len(self.lista)-1-i):
                if self.lista[j]>self.lista[j+1]:
                    self.steps += 1
                    tempo = self.lista[j]
                    self.lista[j] = self.lista[j+1]
                    self.lista[j+1] = tempo
        

        