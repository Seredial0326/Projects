class OrdenaShell:
    def __init__(self):
        self.lista = []
        self.steps = 0
        self.listas = []
    
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

    def shell_sort(self):
        
        h = len(self.lista)//2

        while h>0:

            # el metodo de shell utiliza el ordenamiento por insercion
            for i in range(h,len(self.lista)):
                tempo = self.lista[i]
                j = i

                while j>=h and self.lista[j-h]>tempo:
                    self.lista[j] = self.lista[j-h]
                    j -= h
                    self.listas1()

                self.lista[j] = tempo
                self.listas1()
            
            h //= 2

    def ordena(self,i,grafica):
        for barra,valor in zip(grafica,self.listas[i]):
            barra.set_height(valor)
        return grafica
    
    def ordenagraf(self):
        self.steps = 0

        h = len(self.lista)//2

        while h>0:

            for i in range(h,len(self.lista)):
                tempo = self.lista[i]
                j = i

                while j>=h and self.lista[j-h]>tempo:
                    self.lista[j] = self.lista[j-h]
                    j -= h

                self.lista[j] = tempo
                self.steps += 1
            
            h //= 2