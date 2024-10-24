import matplotlib.pyplot as plot

class OrdenaInsercion:

    def __init__(self):
        self.lista = []
        self.steps = 0

    def insert_sample(self,lista):
        for i in lista:
            self.lista.append(i)

    def ordena(self,i,grafica):

        if i<len(self.lista):

            tempo = self.lista[i]
            j = i

            while j>0 and self.lista[j-1] > tempo:
                self.lista[j]=self.lista[j-1]
                j-=1

            self.lista[j]=tempo

            for barra, valor in zip(grafica,self.lista):
                barra.set_height(valor)

        return grafica
    
    def ordenagraf(self):
        self.steps = 0

        for i in range(1,len(self.lista)):
            tempo = self.lista[i]
            j = i

            steps = 0
            while j>0 and self.lista[j-1] > tempo:
                self.lista[j]=self.lista[j-1]
                j-=1

                steps += 1

            if steps!=0:
                self.steps += steps
            else:
                self.steps += 1

            self.lista[j]=tempo