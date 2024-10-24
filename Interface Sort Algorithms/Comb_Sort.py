class OrdenaComb:
    def __init__(self):
        self.lista = []
        self.listas = []
        self.steps = 0
    
    def insert_sample(self,lista):
        for i in lista:
            self.lista.append(i)
        self.listas1()
    
    def comb_sort(self):
        saltos = len(self.lista)
        reducir = 1.3
        ordenado = False
        
        while not ordenado:            

            saltos = int(saltos / reducir)
            if saltos < 1:
                saltos = 1
                ordenado = True
            a = 0
            while a + saltos < len(self.lista):
                if self.lista[a] > self.lista[a + saltos]:
                    self.lista[a], self.lista[a + saltos] = self.lista[a + saltos], self.lista[a]
                    ordenado = False
                self.listas1()
                a += 1
                self.steps += 1

    def ordenagraf(self):
        saltos = len(self.lista)
        reducir = 1.3
        ordenado = False
        
        while not ordenado:            

            saltos = int(saltos / reducir)
            if saltos < 1:
                saltos = 1
                ordenado = True
            
            a = 0
            while a + saltos < len(self.lista):
                if self.lista[a] > self.lista[a + saltos]:
                    self.lista[a], self.lista[a + saltos] = self.lista[a + saltos], self.lista[a]
                    ordenado = False
                a += 1
                self.steps += 1

    def listas1(self):
        lista = []
        for i in self.lista:
            lista.append(i)
        self.listas.append(lista)
    
    def ordena(self,i,grafica):
        for barra,valor in zip(grafica,self.listas[i]):
            barra.set_height(valor)
        return grafica
