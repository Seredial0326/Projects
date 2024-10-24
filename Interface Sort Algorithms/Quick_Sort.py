import matplotlib.pyplot as plot 

class QuickSort:

    def __init__(self):
        self.lista = []
        self.listas = []
        self.steps = 0
    
    def insert_sample(self,lista):
        for i in lista:
            self.lista.append(i)

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

    def partition(self, izq, der, pivote):
        i = izq - 1
        for j in range(izq, der):
            self.steps += 1
            if self.lista[j] < pivote:
                i += 1
                self.lista[i], self.lista[j] = self.lista[j], self.lista[i]

                self.listas1()
        
        i += 1
        self.lista[i], self.lista[der] = self.lista[der], self.lista[i]
        self.listas1()
        
        return i
    
    
    def quick_sort(self, izq, der):
        if izq >= der:
            return
        else:
            pivote = self.lista[der]
            particion = self.partition(izq, der, pivote)
            self.quick_sort(izq, particion - 1)
            self.quick_sort(particion + 1, der)
            
    def to_quick_sort(self):
        self.quick_sort(0, len(self.lista) - 1)

    def ordena(self,i,grafica):
        for barra,valor in zip(grafica,self.listas[i]):
            barra.set_height(valor)
        return grafica

class QuickSort2: 
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
        

    def partition(self, izq, der, pivote):
        i = izq - 1
        for j in range(izq, der):
            self.steps += 1
            if self.lista[j] < pivote:
                i += 1
                self.lista[i], self.lista[j] = self.lista[j], self.lista[i]
        
        i += 1
        self.lista[i], self.lista[der] = self.lista[der], self.lista[i]
        
        return i
    
    
    def quick_sort(self, izq, der):
        if izq >= der:
            return
        else:
            pivote = self.lista[der]
            particion = self.partition(izq, der, pivote)
            self.quick_sort(izq, particion - 1)
            self.quick_sort(particion + 1, der)
            
    def ordenagraf(self):
        self.steps = 0
        self.quick_sort(0, len(self.lista) - 1)