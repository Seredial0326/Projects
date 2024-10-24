import matplotlib.pyplot as plot

class OrdenaSeleccion:

    def __init__(self):
        self.lista = []
        self.steps = 0

    def insert_sample(self,lista):
        for i in lista:
            self.lista.append(i)

    def ordena(self,i,grafica):

        if i<len(self.lista):

            for barra,valor in zip(grafica,self.lista):
                barra.set_height(valor)

            minimo = i

            for j in range(i+1,len(self.lista)):
                if self.lista[j] < self.lista[minimo]:
                    minimo = j
            
            tempo = self.lista[minimo]
            self.lista[minimo] = self.lista[i]
            self.lista[i] = tempo

        return grafica
    
    def ordenagraf(self):
        self.steps = 0

        for i in range(len(self.lista)-1):
            minimo = i

            for j in range(i+1,len(self.lista)):
                self.steps += 1
                if self.lista[j] < self.lista[minimo]:
                    minimo = j
            
            tempo = self.lista[minimo]
            self.lista[minimo] = self.lista[i]
            self.lista[i] = tempo