import matplotlib.pyplot as plot

class OrdenaConteo:
    def __init__(self):
        self.lista = []
        self.steps = 0
        self.lista_salida = [0]*len(self.lista)

    def insert_sample(self,lista):
        self.lista=[]
        for i in lista:
            self.lista.append(i)
        self.lista_salida = [0]*len(self.lista)

    def ordena(self,i,grafica):
        maximo = max(self.lista)
        
        lista_conteo = [0]*(maximo+1)

        for j in self.lista:
            lista_conteo[j] += 1

        for j in range (1,len(lista_conteo)):
            lista_conteo[j] += lista_conteo[j-1]

        if i<len(self.lista):

            self.lista_salida[lista_conteo[self.lista[i]]-1] = self.lista[i]
            lista_conteo[self.lista[i]] -= 1

            for barra, valor in zip(grafica,self.lista_salida):
                barra.set_height(valor)

            self.steps += 1
            return grafica
        
    def ordenagraf(self):
        self.steps = 0
        maximo = max(self.lista)
        
        lista_conteo = [0]*(maximo+1)

        for i in self.lista:
            lista_conteo[i] += 1
            self.steps += 1

        for i in range (1,len(lista_conteo)):
            lista_conteo[i] += lista_conteo[i-1]
            self.steps += 1

        for i in range(len(self.lista)):
            self.lista_salida[lista_conteo[self.lista[i]]-1] = self.lista[i]
            lista_conteo[self.lista[i]] -= 1
            self.steps += 1

        return self.lista_salida