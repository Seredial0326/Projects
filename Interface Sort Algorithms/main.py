from tkinter import *
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sys
from matplotlib.animation import FuncAnimation
import tkinter as tk
from matplotlib.figure import Figure
import time
from tkinter import messagebox


from Bubble_Sort import OrdenaBurbuja
from Selection_Sort import OrdenaSeleccion
from Merge_Sort import MergeSort
from Counting_Sort import OrdenaConteo
from Heap_Sort import OrdenaHeap
from Quick_Sort import QuickSort
from Shell_Sort import OrdenaShell
from Insertion_Sort import OrdenaInsercion
from Comb_Sort import OrdenaComb
from Merge_Sort import MergeSort2
from Heap_Sort import OrdenaHeap2
from Quick_Sort import QuickSort2
from Radix_Sort import Radix

GUI1 = Tk()
GUI1.title("GUI1")
GUI1.geometry("1500x750")
GUI1.resizable(True, False)

lista = []
global Grafica
Frames1 = []
Frames2 = []

def destroy1():
    #if ani:
    #    ani.event_source.stop()
    if(len(Frames1)>0):
        for frame1 in Frames1:
            frame1.destroy()

def destroy2():
    if(len(Frames2)>0):
        for frame2 in Frames2:
            frame2.destroy()
        
def Ventana1():
    Ventanas.destroy()
    destroy2()

    def TipoOrdenamiento(Seleccion):
        global ordenas
        if Seleccion == "Bubble sort":
            ordenas = OrdenaBurbuja()
            ordenas.insert_sample(lista)
        if Seleccion == "Selection sort":
            ordenas = OrdenaSeleccion()
            ordenas.insert_sample(lista)
        if Seleccion == "Merge sort":
            ordenas = MergeSort()
            ordenas.insert_sample(lista)
            ordenas.merge_sort()
        if Seleccion == "Counting sort":
            ordenas = OrdenaConteo()
            ordenas.insert_sample(lista)
        if Seleccion == "Heap sort":
            ordenas = OrdenaHeap()
            ordenas.insert_sample(lista)
            ordenas.heap_sort()
        if Seleccion == "Quick sort":
            ordenas = QuickSort()
            ordenas.insert_sample(lista)
            ordenas.to_quick_sort()
        if Seleccion == "Shell sort":
            ordenas = OrdenaShell()
            ordenas.insert_sample(lista)
            ordenas.shell_sort()
        if Seleccion == "Radix sort":
            ordenas = OrdenaSeleccion()
            ordenas.insert_sample(lista)
        if Seleccion == "Insertion sort":
            ordenas = OrdenaInsercion()
            ordenas.insert_sample(lista)
        if Seleccion == "Comb sort":
            ordenas = OrdenaComb()
            ordenas.insert_sample(lista)
            ordenas.comb_sort()
        return ordenas
            
    def Ordenamiento1():
        Frames1[0].destroy()

        Grafica = Frame(GUI1, bg = "gray")
        Grafica.place(x = 10, y = 70, width = 1000, height = 500)

        Aviso = Label(GUI1, text = "EL ordenamiento puede tardar un poco dependiendo del caso")
        Aviso.place(x = 1400, y = 690,width=10,height=10)

        vel = int(Velocidad.get())
        vel = vel*10

        Seleccion = OrdenamientoOpc1.get()

        global ani
        # Crear figura y barras
        fig, ax = plt.subplots()
        grafica = ax.bar(range(len(lista)), lista)

        if Seleccion == "Merge sort" or Seleccion == "Heap sort" or Seleccion == "Comb sort" or Seleccion == "Quick sort" or Seleccion == "Shell sort":
            ani = FuncAnimation(fig, TipoOrdenamiento(Seleccion).ordena, fargs=(grafica,), frames=len(TipoOrdenamiento(Seleccion).listas), repeat=False, interval=vel)    
        else:
            ani = FuncAnimation(fig, TipoOrdenamiento(Seleccion).ordena, fargs=(grafica,), frames=len(lista) + 1, repeat=False, interval=vel)

        # Integrar la figura de Matplotlib en la ventana de Tkinter
        canvas = FigureCanvasTkAgg(fig, master=Grafica)
        canvas.draw()
        canvas.get_tk_widget().configure(borderwidth=2,relief="solid")
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        BotonesOrd = Frame(GUI1, bg = "lightgreen")
        BotonesOrd.place(x = 10, y = 590, width = 1000, height = 60)
        
        Pausar = Button(BotonesOrd, text = "Pausar Ordenamiento", command = stop_animation, cursor="hand2")
        Pausar.place(relx = 0.02, rely = 0.4, relwidth = 0.3, relheight = 0.5)
        
        Detener = Button(BotonesOrd, text = "Detener Ordenamiento", command = close_window, cursor="hand2")
        Detener.place(relx = 0.34, rely = 0.4, relwidth = 0.3, relheight = 0.5)
        
        Reanudar = Button(BotonesOrd, text = "Reanudar Ordenamiento", command = resume_animation, cursor="hand2")
        Reanudar.place(relx = 0.66, rely = 0.4, relwidth = 0.3, relheight = 0.5)

    def close_window():
        GUI1.destroy()
        sys.exit()

    def stop_animation():
        if ani:
            ani.event_source.stop()

    def resume_animation():
        if ani:
            ani.event_source.start()

    def GenerarLista():
        Frames1[0].destroy()

        Grafica = Frame(GUI1, bg = "gray")
        Grafica.place(x = 10, y = 70, width = 1000, height = 500) # cuadro donde esta el frame

        global lista
        rango = int(RLista.get())
        lista = random.sample(range(0,rango),rango)

        fig = Figure(figsize=(90, 40), dpi=100)
            
        ax = fig.add_subplot(111)
        ax.bar(range(len(lista)), lista)

        canvas = FigureCanvasTkAgg(fig, master=Grafica)
        canvas.draw()
        canvas.get_tk_widget().configure(borderwidth=2,relief="solid")
        canvas.get_tk_widget().pack()
        
        Ordenamiento = Frame(GUI1, bg = "lightgreen")
        Ordenamiento.place(x = 1025, y = 230, width = 300, height = 180)
        
        RListLabel = Label(Ordenamiento, text = "Velocidad", bg = "lightgreen", foreground="darkblue")
        RListLabel.pack()
        
        IniciarProceso = Button(Ordenamiento, text = "Iniciar", command = Ordenamiento1, cursor="hand2")
        IniciarProceso.place(relx = 0.25, rely = 0.7, relwidth = 0.5, relheight = 0.2)

        global Velocidad
        
        Velocidad = Scale(Ordenamiento, from_ = 0, to = 10, orient = HORIZONTAL, length = 270)
        Velocidad.pack(pady = 10)
        
        global OrdenamientoOpc1

        OrdenamientoOpc1 = StringVar()
        OrdenamientoOpc1.set("Elige")
        
        listaOrd = ["Bubble sort", "Selection sort", "Insertion sort", "Shell sort", "Quick sort", "Merge sort", "Counting sort", "Heap sort", "Radix sort", "Comb sort"]
        
        OpcOrd = OptionMenu(Ordenamiento, OrdenamientoOpc1, *listaOrd)
        OpcOrd.place(relx = 0.25, rely = 0.45, relwidth = 0.5, relheight = 0.2)

        Frames1.append(Ordenamiento)

    Grafica = Frame(GUI1, bg = "gray", borderwidth=2, relief="solid")
    Grafica.place(x = 10, y = 70, width = 1000, height = 500) # cuadro gris

    TlGrafica = Label(Grafica, text = "GRAFICA AQUI", bg = "gray",foreground="orange")
    TlGrafica.pack()

    Botones = Frame(GUI1, bg = "lightblue")
    Botones.place(x = 1025, y = 70, width = 300, height = 150)

    RListLabel = Label(Botones, text = "Lista", bg = "lightblue", foreground="darkgreen")
    RListLabel.pack()

    RLista = Scale(Botones, from_ = 10, to = 1000, orient = HORIZONTAL, length = 270)
    RLista.pack(pady = 10)

    GenLista = Button(Botones, text = "Generar Lista", command = GenerarLista, cursor="hand2")
    GenLista.place(relx = 0.25, rely = 0.60, relwidth = 0.5, relheight = 0.25)

    Frames1.append(Grafica)
    Frames1.append(Botones)

    Titulo = Label(GUI1, text= "Algortimos de Ordenamiento",background="darkred",foreground="white",font=("Castellar",18), height=1)
    Titulo.pack(fill=tk.X)

    Bienvenida = Label(GUI1, text = "¡H o l a!   B i e n v e n i d @")
    Bienvenida.place(x = 620, y = 45, height = 12)

    GUI1.protocol("WM_DELETE_WINDOW", close_window)

def Ventana2():
    destroy1()
    listaseleccion = []
    frames = []
    Graficav1vlis = []

    def destroy3():
        if(len(frames)>0):
            for frame3 in frames:
                frame3.destroy()

    def close_window():
        GUI1.destroy()
        sys.exit()

    def message():
        messagebox.showinfo("Tiempo de ejecucion", texto)

    def Bubblev1v():
        Graficav1vlis[0].destroy()

        Graficav1v = Frame (GUI1, bg = "gray")
        Graficav1v.place(relx = .05, rely = 0.20, relwidth = 0.6, relheight = 0.6)

        tituloBur = Label(GUI1, text = "B u b b l e   s o r t", bg= "lightgreen", borderwidth=1,relief="solid")
        tituloBur.place(x = 1020, y = 151, width = 200, height = 30)    

        info = Label(GUI1, text = "-> Big O: O(n^2)\n(tiempo de ejecución crece cuadráticamente con tamaño de la entrada)\n\n\n-> Ordenamiento más básico \n pero menos eficiente\n\n\n -> Elementos mas pequeños suben a primeras posiciones del arreglo\n asi como las burbujas mas livianas van hasta arriba en un vaso de refresco \n\n-> Recorre lista a ordenar varias veces secuencialmente")
        info.place(x = 920, y = 215, width = 400, height = 240)    

        ordena = OrdenaBurbuja()

        grafica(ordena, Graficav1v, 15, 10)
        canvas.get_tk_widget().configure(borderwidth=2,relief="solid")
        tiempo = Button(GUI1, text = "Tiempos ejecucion", command = message,bg="orange", cursor="hand2")
        tiempo.place(x = 1024, y = 525, width = 200, height = 30)

    def Selectionv1v():
        Graficav1vlis[0].destroy()

        Graficav1v = Frame (GUI1, bg = "gray")
        Graficav1v.place(relx = .05, rely = 0.20, relwidth = 0.6, relheight = 0.6)

        tituloSel = Label(GUI1, text = "S e l e c t i o n   s o r t", bg= "lightgreen", borderwidth=1,relief="solid")
        tituloSel.place(x = 1020, y = 151, width = 200, height = 30)    

        info = Label(GUI1, text = "-> Big O: O(n^2)\n(igual que en Bubble sort pero en menos tiempo)\n\n\n-> La base del sort es buscar el elemento minimo de la lista\n e intercambiarlo por la posicion actual de la lista\n\n\n -> Utiliza dos ciclos for (anidados):\n 1. Para encontrar elemento minimo\n 2. Para intercambiar el minimo con otro elemento de la lista")
        info.place(x = 920, y = 225, width = 400, height = 200)

        ordena = OrdenaSeleccion()

        grafica(ordena, Graficav1v, 15, 10)
        canvas.get_tk_widget().configure(borderwidth=2,relief="solid")
        tiempo = Button(GUI1, text = "Tiempos ejecucion", command = message,bg="orange", cursor="hand2")
        tiempo.place(x = 1024, y = 525, width = 200, height = 30)

    def Insertionv1v():
        Graficav1vlis[0].destroy()

        Graficav1v = Frame (GUI1, bg = "gray")
        Graficav1v.place(relx = .05, rely = 0.20, relwidth = 0.6, relheight = 0.6)

        tituloIns = Label(GUI1, text = "I n s e r t i o n   s o r t", bg= "lightgreen")
        tituloIns.place(x = 1020, y = 151, width = 200, height = 30)    

        info = Label(GUI1, text = "-> Big O en el mejor de los casos: O(n)\n-> Big O en el peor de los casos: O(n^2)\n\n\n-> Presenta una manera más natural de ordenar elementos\n parecido a acomodar un mazo de cartas numeradas\n\n\n -> Considera los elementos (posiciones de la lista) anteriores ya ordenadas\n por lo que no recorre la lista varias veces innecesarias,\n más eficiente que Bubble y Selection")
        info.place(x = 920, y = 225, width = 400, height = 200)

        ordena = OrdenaInsercion()

        grafica(ordena, Graficav1v, 15, 10)
        canvas.get_tk_widget().configure(borderwidth=2,relief="solid")
        tiempo = Button(GUI1, text = "Tiempos ejecucion", command = message,bg="orange", cursor="hand2")
        tiempo.place(x = 1024, y = 525, width = 200, height = 30)

    def Countingv1v():
        Graficav1vlis[0].destroy()

        Graficav1v = Frame (GUI1, bg = "gray")
        Graficav1v.place(relx = .05, rely = 0.20, relwidth = 0.6, relheight = 0.6)

        tituloCou = Label(GUI1, text = "C o u n t i n g   s o r t", bg= "lightgreen")
        tituloCou.place(x = 1020, y = 151, width = 200, height = 30)    

        info = Label(GUI1, text = "-> Big O: O(n+k)\n donde k es el elemento más grande de la lista\n\n\n-> No utiliza comparaciones\n ordena con frecuencia de cada elemento de la lista \ny creando nuevas listas\n\n\n -> Como hace uso de indices de las listas que crea: \n Solo puede usarse con enteros positivos y rango de valores tiene que: \n Ser pequeño y no tan variado (1,2,3,1000)")
        info.place(x = 920, y = 225, width = 400, height = 200)

        ordena = OrdenaConteo()

        grafica(ordena, Graficav1v, 15, 10)
        canvas.get_tk_widget().configure(borderwidth=2,relief="solid")
        tiempo = Button(GUI1, text = "Tiempos ejecucion", command = message,bg="orange", cursor="hand2")
        tiempo.place(x = 1024, y = 525, width = 200, height = 40)

    def Quickv1v():
        Graficav1vlis[0].destroy()

        Graficav1v = Frame (GUI1, bg = "gray")
        Graficav1v.place(relx = .05, rely = 0.20, relwidth = 0.6, relheight = 0.6)

        infoQui = Label(GUI1, text = "Q u i c k   s o r t", bg= "lightgreen")
        infoQui.place(x = 1020, y = 151, width = 200, height = 35)    

        info = Label(GUI1, text = "-> Divide y vencerás\n\n\n-> Divide la lista en subconjuntos más pequeños usando un pivote\n para después ordenarlos usando recursividad\n\n\n -> Big O en el mejor de los casos: O(n log n) \n Ya que divide la lista equilibradamente\n y realiza las comparaciones e intercambio un número logarítmico de veces\n\n\n -> Big O en el peor de los casos: O(n^2)\n Porque la lista se divide desequilibradamente")
        info.place(x = 920, y = 225, width = 400, height = 215)

        ordena = QuickSort2()

        grafica(ordena, Graficav1v, 15, 10)
        canvas.get_tk_widget().configure(borderwidth=2,relief="solid")
        tiempo = Button(GUI1, text = "Tiempos ejecucion", command = message,bg="orange", cursor="hand2")
        tiempo.place(x = 1024, y = 525, width = 200, height = 40)

    def Heapv1v():
        Graficav1vlis[0].destroy()

        Graficav1v = Frame (GUI1, bg = "gray")
        Graficav1v.place(relx = .05, rely = 0.20, relwidth = 0.6, relheight = 0.6)

        infoHe = Label(GUI1, text = "H e a p   s o r t", bg= "lightgreen")
        infoHe.place(x = 1020, y = 151, width = 200, height = 30)    

        info = Label(GUI1, text = "-> Hace comparaciones usando una estructura similar a un árbol binario,\n dicho árbol se construye con los elementos de la lista \npara después extraer sus máximos o mínimos\n\n\n -> Big O: O(n log n)\nYa que para la construcción del árbol ocupa O(n)\n y para los máximos o mínimos y el ordenamiento ocupa O(log n)")
        info.place(x = 920, y = 225, width = 400, height = 200)

        ordena = OrdenaHeap2()

        grafica(ordena, Graficav1v, 15, 10)
        canvas.get_tk_widget().configure(borderwidth=2,relief="solid")
        tiempo = Button(GUI1, text = "Tiempos ejecucion", command = message,bg="orange", cursor="hand2")
        tiempo.place(x = 1024, y = 525, width = 200, height = 40)

    def Shellv1v():
        Graficav1vlis[0].destroy()

        Graficav1v = Frame (GUI1, bg = "gray")
        Graficav1v.place(relx = .05, rely = 0.20, relwidth = 0.6, relheight = 0.6)

        infoSh = Label(GUI1, text = "S h e l l   s o r t", bg= "lightgreen")
        infoSh.place(x = 1020, y = 151, width = 200, height = 30)    

        info = Label(GUI1, text = "-> Big O: \nDepende de la secuencia de intervalos para diviir la lista en sublistas\n Se ha planteado que puede llegar a ser O(n^2) o  O(n log2 n)\n\n\n-> Es una mejora a Insertion sort, útil para ordenar archivos muy grandes\n\n\nPuede usar distintas secuencias de intervalos\n como la de Knut o Hibbard")
        info.place(x = 920, y = 225, width = 400, height = 200)

        ordena = OrdenaShell()

        grafica(ordena, Graficav1v, 15, 10)
        canvas.get_tk_widget().configure(borderwidth=2,relief="solid")
        tiempo = Button(GUI1, text = "Tiempos ejecucion", command = message,bg="orange", cursor="hand2")
        tiempo.place(x = 1024, y = 525, width = 200, height = 40)

    def Mergev1v():
        Graficav1vlis[0].destroy()

        Graficav1v = Frame (GUI1, bg = "gray")
        Graficav1v.place(relx = .05, rely = 0.20, relwidth = 0.6, relheight = 0.6)

        infoMe = Label(GUI1, text = "M e r g e   s o r t", bg= "lightgreen")
        infoMe.place(x = 1020, y = 151, width = 200, height = 30)    

        info = Label(GUI1, text = "-> Big O: O(n log n) en todos los casos\n\n\n -> Aplica el concepto de divide y vencerás\n\n\n-> 1. Divide lista en sub-listas más pequeñas\n 2. Ordena cada sub-lista recursivamente\n 3. Combina sub-listas ordenadas para obtener la lista ordenada")
        info.place(x = 920, y = 225, width = 400, height = 200)

        ordena = MergeSort2()

        grafica(ordena, Graficav1v, 15, 10)
        canvas.get_tk_widget().configure(borderwidth=2,relief="solid")
        tiempo = Button(GUI1, text = "Tiempos ejecucion", command = message,bg="orange", cursor="hand2")
        tiempo.place(x = 1024, y = 525, width = 200, height = 40)

    def Combv1v():
        Graficav1vlis[0].destroy()

        Graficav1v = Frame (GUI1, bg = "gray")
        Graficav1v.place(relx = .05, rely = 0.20, relwidth = 0.6, relheight = 0.6)

        infoCo = Label(GUI1, text = "C o m b   s o r t", bg= "lightgreen")
        infoCo.place(x = 1020, y = 151, width = 200, height = 30)    

        info = Label(GUI1, text = "-> Big O en mayoría de casos: O(n^2)\n\n\n -> Hace comparaciones similares a Bubble sort\n pero usa una técnica de saltos que\n permite mover los elementos distantes de mejor manera\n\n\n-> Básicamente es una mejora a Bubble sort")
        info.place(x = 920, y = 225, width = 400, height = 200)

        ordena = OrdenaComb()

        grafica(ordena, Graficav1v, 15, 10)
        canvas.get_tk_widget().configure(borderwidth=2,relief="solid")
        tiempo = Button(GUI1, text = "Tiempos ejecucion", command = message,bg="orange", cursor="hand2")
        tiempo.place(x = 1024, y = 525, width = 200, height = 40)

    def Radixv1v():
        Graficav1vlis[0].destroy()

        Graficav1v = Frame (GUI1, bg = "gray")
        Graficav1v.place(relx = .05, rely = 0.20, relwidth = 0.6, relheight = 0.6)

        infoRa = Label(GUI1, text = "R a d i x   s o r t", bg= "lightgreen")
        infoRa.place(x = 1020, y = 151, width = 200, height = 30)    

        info = Label(GUI1, text = "-> Big O: O(k * n)\n k representa número de dígitos necesarios para números\n en la base utilizada para el sort\n\n\n -> No utiliza comparaciones\nOrdena usando los dígitos individuales de cada elemento de la lista\nDesde el dígito menos significativo al más significativo\n\n\n En el mejor de los casos su Big O es de O(n)")
        info.place(x = 920, y = 225, width = 400, height = 215)

        ordena = Radix()

        grafica(ordena, Graficav1v, 15, 10)
        canvas.get_tk_widget().configure(borderwidth=2,relief="solid")
        tiempo = Button(GUI1, text = "Tiempos ejecucion", command = message,bg="orange", cursor="hand2")
        tiempo.place(x = 1024, y = 525, width = 200, height = 40)

    def v1v():
        Bur.destroy()
        Sel.destroy()
        Ins.destroy()
        Coun.destroy()
        Mer.destroy()
        He.destroy()
        Qui.destroy()
        Sh.destroy()
        Rad.destroy()
        Co.destroy()
        Elementos.destroy()
        destroy3()
        V1VFr.destroy()
        #V1VFr.place(relx = 0.02, rely = 0.05, relwidth = 0.20, relheight = 0.27)

        escoger = Label(GUI1, text= "Escoga el ordenamiento que quiera ver: ",font=("Calibri Light",12))
        escoger.place(x = 555, y = 40)
        Graficav1v = Frame (GUI1, bg = "gray")
        Graficav1vBtn = Frame(GUI1, bg = "lightblue")
        Graficav1v.place(relx = .05, rely = 0.20, relwidth = 0.6, relheight = 0.6)
        Graficav1vBtn.place(relx = .10, rely = 0.1, relwidth = 0.8, relheight = 0.05)

        Graficav1vlis.append(Graficav1v)

        Bubble = Button(Graficav1vBtn, text = "Bubble Sort", command = Bubblev1v)
        Bubble.place(relx = .01, rely = 0.15, relwidth = 0.08, relheight = 0.7)
        Sele = Button(Graficav1vBtn, text = "Selection Sort", command = Selectionv1v)
        Sele.place(relx = .11, rely = 0.15, relwidth = 0.08, relheight = 0.7)
        Inser = Button(Graficav1vBtn, text = "Insertion Sort", command = Insertionv1v)
        Inser.place(relx = .21, rely = 0.15, relwidth = 0.08, relheight = 0.7)
        Heap = Button(Graficav1vBtn, text = "Heap Sort", command = Heapv1v)
        Heap.place(relx = .31, rely = 0.15, relwidth = 0.08, relheight = 0.7)
        Quick = Button(Graficav1vBtn, text = "Quick Sort", command = Quickv1v)
        Quick.place(relx = .41, rely = 0.15, relwidth = 0.08, relheight = 0.7)
        Comb = Button(Graficav1vBtn, text = "Comb Sort", command = Combv1v)
        Comb.place(relx = .51, rely = 0.15, relwidth = 0.08, relheight = 0.7)
        Merge = Button(Graficav1vBtn, text = "Merge Sort", command = Mergev1v)
        Merge.place(relx = .61, rely = 0.15, relwidth = 0.08, relheight = 0.7)
        Shell = Button(Graficav1vBtn, text = "Shell Sort", command = Shellv1v)
        Shell.place(relx = .71, rely = 0.15, relwidth = 0.08, relheight = 0.7)
        Counting = Button(Graficav1vBtn, text = "Counting Sort", command = Countingv1v)
        Counting.place(relx = .81, rely = 0.15, relwidth = 0.08, relheight = 0.7)
        Radix = Button(Graficav1vBtn, text = "Radix Sort", command = Radixv1v)
        Radix.place(relx = .91, rely = 0.15, relwidth = 0.08, relheight = 0.7)

    def Bubblev1vAl():
        Graficav1vlis[0].destroy()

        Graficav1v = Frame (GUI1, bg = "gray")
        Graficav1v.place(relx = .05, rely = 0.20, relwidth = 0.6, relheight = 0.6)

        infoBur = Label(GUI1, text = "B u b b l e   s o r t", bg= "lightgreen")
        infoBur.place(x = 1030, y = 151, width = 200, height = 30)    

        info = Label(GUI1, text = "-> Como la lista está en orden inverso, la Big O cambia\nBig O: n * (n-1) [comparaciones e intercambios]\n\n\n-> La Big O aumenta debido a que:\nSe requiere un intercambio en cada comparación,\n y empieza en un valor muy alto termina realizando muchos steps en total")
        info.place(x = 920, y = 215, width = 400, height = 240)

        ordena = OrdenaBurbuja()

        graficaAl(ordena, Graficav1v, 15, 10)    
        tiempo = Button(GUI1, text = "Tiempos ejecucion", command = message,bg="orange", cursor="hand2")
        tiempo.place(x = 1024, y = 525, width = 200, height = 30)

    def Selectionv1vAl():
        Graficav1vlis[0].destroy()

        Graficav1v = Frame (GUI1, bg = "gray")
        Graficav1v.place(relx = .05, rely = 0.20, relwidth = 0.6, relheight = 0.6)

        infoSel = Label(GUI1, text = "S e l e c t i o n   s o r t", bg= "lightgreen")
        infoSel.place(x = 1030, y = 151, width = 200, height = 30)    

        info = Label(GUI1, text = "-> Big O: O(n^2)\nLa Big O en el peor de los casos es la misma\n\n\n-> Para Selection sort no importa el estado inicial de la lista\nSigue utilizando los ciclos anidados de misma forma\n\n\nSeguirá buscando el mínimo en cada iteración e intercambiara\n posición con los otros elementos de la lista")
        info.place(x = 920, y = 225, width = 400, height = 200)

        ordena = OrdenaSeleccion()

        graficaAl(ordena, Graficav1v, 15, 10)    
        tiempo = Button(GUI1, text = "Tiempos ejecucion", command = message,bg="orange", cursor="hand2")
        tiempo.place(x = 1024, y = 525, width = 200, height = 30)

    def Insertionv1vAl():
        Graficav1vlis[0].destroy()

        Graficav1v = Frame (GUI1, bg = "gray")
        Graficav1v.place(relx = .05, rely = 0.20, relwidth = 0.6, relheight = 0.6)

        infoIns = Label(GUI1, text = "I n s e r t i o n   s o r t", bg= "lightgreen")
        infoIns.place(x = 1030, y = 151, width = 200, height = 30)    

        info = Label(GUI1, text = "-> Big O promedio: O(n^2)\nDebido a que para mover cada elemento a su posición correcto necesita\n un número de operaciones cuadrático\n\n\nBig O en el mejor de los casos: O(n)\n\n\nEn general depende del estado inicial de la lista\npero en este caso es de O(n^2)")
        info.place(x = 920, y = 225, width = 400, height = 200)

        ordena = OrdenaInsercion()

        graficaAl(ordena, Graficav1v, 15, 10)
        tiempo = Button(GUI1, text = "Tiempos ejecucion", command = message,bg="orange", cursor="hand2")
        tiempo.place(x = 1024, y = 525, width = 200, height = 30)

    def Countingv1vAl():
        Graficav1vlis[0].destroy()

        Graficav1v = Frame (GUI1, bg = "gray")
        Graficav1v.place(relx = .05, rely = 0.20, relwidth = 0.6, relheight = 0.6)

        infoCou = Label(GUI1, text = "C o u n t i n g   s o r t", bg= "lightgreen")
        infoCou.place(x = 1030, y = 151, width = 200, height = 30)    

        info = Label(GUI1, text = "-> Big O: O(n+k)\n\n\n -> Debido a que el ordenamiento toma en cuenta la frecuencia de cada elemento\nno afecta el orden inverso de la lista\n\n\n-> Sin embargo, debido al rango el proceso puede tardar un poco")
        info.place(x = 920, y = 225, width = 400, height = 200)

        ordena = OrdenaConteo()

        graficaAl(ordena, Graficav1v, 15, 10)
        tiempo = Button(GUI1, text = "Tiempos ejecucion", command = message,bg="orange", cursor="hand2")
        tiempo.place(x = 1024, y = 525, width = 200, height = 30)

    def Quickv1vAl():
        Graficav1vlis[0].destroy()

        Graficav1v = Frame (GUI1, bg = "gray")
        Graficav1v.place(relx = .05, rely = 0.20, relwidth = 0.6, relheight = 0.6)

        infoQui = Label(GUI1, text = "Q u i c k   s o r t", bg= "lightgreen")
        infoQui.place(x = 1030, y = 151, width = 200, height = 30)    

        info = Label(GUI1, text = "-> Divide y vencerás\n\n\n-> Divide la lista en subconjuntos más pequeños usando un pivote\n para después ordenarlos usando recursividad\n\n\n -> Big O en el peor de los casos: O(n^2)\n Porque la lista se divide desequilibradamente, por el pivote")
        info.place(x = 920, y = 225, width = 400, height = 215)

        ordena = QuickSort2()

        graficaAl(ordena, Graficav1v, 15, 10)
        tiempo = Button(GUI1, text = "Tiempos ejecucion", command = message,bg="orange", cursor="hand2")
        tiempo.place(x = 1024, y = 525, width = 200, height = 30)

    def Heapv1vAl():
        Graficav1vlis[0].destroy()

        Graficav1v = Frame (GUI1, bg = "gray")
        Graficav1v.place(relx = .05, rely = 0.20, relwidth = 0.6, relheight = 0.6)

        infoHe = Label(GUI1, text = "H e a p   s o r t", bg= "lightgreen")
        infoHe.place(x = 1030, y = 151, width = 200, height = 30)    

        info = Label(GUI1, text = "-> Hace comparaciones usando una estructura similar a un árbol binario,\n dicho árbol se construye con los elementos de la lista \npara después extraer sus máximos o mínimos\n\n\n -> Big O: O(n log n)\nYa que para la construcción del árbol ocupa O(n)\n y para los máximos o mínimos y el ordenamiento ocupa O(log n)")
        info.place(x = 920, y = 225, width = 400, height = 200)

        ordena = OrdenaHeap2()

        graficaAl(ordena, Graficav1v, 15, 10)
        tiempo = Button(GUI1, text = "Tiempos ejecucion", command = message,bg="orange", cursor="hand2")
        tiempo.place(x = 1024, y = 525, width = 200, height = 30)

    def Shellv1vAl():
        Graficav1vlis[0].destroy()

        Graficav1v = Frame (GUI1, bg = "gray")
        Graficav1v.place(relx = .05, rely = 0.20, relwidth = 0.6, relheight = 0.6)

        infoSh = Label(GUI1, text = "S h e l l   s o r t", bg= "lightgreen")
        infoSh.place(x = 1030, y = 151, width = 200, height = 30)
        
        info = Label(GUI1, text = "-> Big O: \nDepende de secuencia de intervalos para dividir la lista en sublistas\n En este caso llegar a ser de O(n^2)\n\n\n-> Es una mejora a Insertion sort, útil para ordenar archivos muy grandes\n\n\n")
        info.place(x = 920, y = 225, width = 400, height = 200)

        ordena = OrdenaShell()

        graficaAl(ordena, Graficav1v, 15, 10)
        tiempo = Button(GUI1, text = "Tiempos ejecucion", command = message,bg="orange", cursor="hand2")
        tiempo.place(x = 1024, y = 525, width = 200, height = 30)

    def Mergev1vAl():
        Graficav1vlis[0].destroy()

        Graficav1v = Frame (GUI1, bg = "gray")
        Graficav1v.place(relx = .05, rely = 0.20, relwidth = 0.6, relheight = 0.6)

        infoMe = Label(GUI1, text = "M e r g e   s o r t", bg= "lightgreen")
        infoMe.place(x = 1030, y = 151, width = 200, height = 30)

        info = Label(GUI1, text = "-> Big O: O(n log n)\nYa que para la construcción del árbol ocupa O(n)\n y para los máximos o mínimos y el ordenamiento ocupa O(log n)\n\n\n-> En este caso de la lista invertida sigue siedo la misma Big O\n esto debido a la naturaleza del sort")
        info.place(x = 920, y = 225, width = 400, height = 200)

        ordena = MergeSort2()

        graficaAl(ordena, Graficav1v, 15, 10)
        tiempo = Button(GUI1, text = "Tiempos ejecucion", command = message,bg="orange", cursor="hand2")
        tiempo.place(x = 1024, y = 525, width = 200, height = 30)

    def Combv1vAl():
        Graficav1vlis[0].destroy()

        Graficav1v = Frame (GUI1, bg = "gray")
        Graficav1v.place(relx = .05, rely = 0.20, relwidth = 0.6, relheight = 0.6)

        infoCo = Label(GUI1, text = "C o m b   s o r t", bg= "lightgreen")
        infoCo.place(x = 1030, y = 151, width = 200, height = 30)    

        info = Label(GUI1, text = "-> Big O en este caso: O(n^2)\n\n\n -> Hace comparaciones similares a Bubble sort\n pero usa una técnica de saltos que permite mover los elementos distantes de mejor manera\n\n\n-> Básicamente es una mejora a Bubble sort")
        info.place(x = 920, y = 225, width = 400, height = 200)

        ordena = OrdenaComb()

        graficaAl(ordena, Graficav1v, 15, 10)
        tiempo = Button(GUI1, text = "Tiempos ejecucion", command = message,bg="orange", cursor="hand2")
        tiempo.place(x = 1024, y = 525, width = 200, height = 30)

    def Radixv1vAl():
        Graficav1vlis[0].destroy()

        Graficav1v = Frame (GUI1, bg = "gray")
        Graficav1v.place(relx = .05, rely = 0.20, relwidth = 0.6, relheight = 0.6)

        infoRa = Label(GUI1, text = "R a d i x   s o r t", bg= "lightgreen")
        infoRa.place(x = 1030, y = 151, width = 200, height = 30) 

        info = Label(GUI1, text = "-> Big O: O(k * n)\n k representa número de dígitos necesarios para números\n en la base utilizada para el sort\n\n\n -> No utiliza comparaciones\nOrdena usando los dígitos individuales de cada elemento de la lista\nDesde el dígito menos significativo al más significativo\n\n\n En el mejor de los casos su Big O es de O(n)")
        info.place(x = 920, y = 225, width = 400, height = 215)

        ordena = Radix()

        graficaAl(ordena, Graficav1v, 15, 10)
        tiempo = Button(GUI1, text = "Tiempos ejecucion", command = message,bg="orange", cursor="hand2")
        tiempo.place(x = 1024, y = 525, width = 200, height = 30)

    def v1vAl():
        Bur.destroy()
        Sel.destroy()
        Ins.destroy()
        Coun.destroy()
        Mer.destroy()
        He.destroy()
        Qui.destroy()
        Sh.destroy()
        Rad.destroy()
        Co.destroy()
        Elementos.destroy()
        destroy3()
        V1VFr.destroy()
        #V1VFr.place(relx = 0.02, rely = 0.05, relwidth = 0.20, relheight = 0.27)

        escoger = Label(GUI1, text= "Escoga el ordenamiento que quiera ver: ",font=("Calibri Light",12))
        escoger.place(x = 555, y = 40)
        Graficav1v = Frame (GUI1, bg = "gray")
        Graficav1vBtn = Frame(GUI1, bg = "lightblue")
        Graficav1v.place(relx = .05, rely = 0.20, relwidth = 0.6, relheight = 0.6)
        Graficav1vBtn.place(relx = .10, rely = 0.1, relwidth = 0.8, relheight = 0.05)

        Graficav1vlis.append(Graficav1v)

        Bubble = Button(Graficav1vBtn, text = "Bubble Sort", command = Bubblev1vAl, cursor="hand2")
        Bubble.place(relx = .01, rely = 0.15, relwidth = 0.08, relheight = 0.7)
        Sele = Button(Graficav1vBtn, text = "Selection Sort", command = Selectionv1vAl, cursor="hand2")
        Sele.place(relx = .11, rely = 0.15, relwidth = 0.08, relheight = 0.7)
        Inser = Button(Graficav1vBtn, text = "Insertion Sort", command = Insertionv1vAl, cursor="hand2")
        Inser.place(relx = .21, rely = 0.15, relwidth = 0.08, relheight = 0.7)
        Heap = Button(Graficav1vBtn, text = "Heap Sort", command = Heapv1vAl, cursor="hand2")
        Heap.place(relx = .31, rely = 0.15, relwidth = 0.08, relheight = 0.7)
        Quick = Button(Graficav1vBtn, text = "Quick Sort", command = Quickv1vAl, cursor="hand2")
        Quick.place(relx = .41, rely = 0.15, relwidth = 0.08, relheight = 0.7)
        Comb = Button(Graficav1vBtn, text = "Comb Sort", command = Combv1vAl, cursor="hand2")
        Comb.place(relx = .51, rely = 0.15, relwidth = 0.08, relheight = 0.7)
        Merge = Button(Graficav1vBtn, text = "Merge Sort", command = Mergev1vAl, cursor="hand2")
        Merge.place(relx = .61, rely = 0.15, relwidth = 0.08, relheight = 0.7)
        Shell = Button(Graficav1vBtn, text = "Shell Sort", command = Shellv1vAl, cursor="hand2")
        Shell.place(relx = .71, rely = 0.15, relwidth = 0.08, relheight = 0.7)
        Counting = Button(Graficav1vBtn, text = "Counting Sort", command = Countingv1vAl, cursor="hand2")
        Counting.place(relx = .81, rely = 0.15, relwidth = 0.08, relheight = 0.7)
        Radix = Button(Graficav1vBtn, text = "Radix Sort", command = Radixv1vAl, cursor="hand2")
        Radix.place(relx = .91, rely = 0.15, relwidth = 0.08, relheight = 0.7)

    def comparar(ordena,ax,nombre):
        t,items,steps = [], [], []

        for i in range(5):
            items.append((i+1)*400)
            ordena.insert_sample(random.sample(range(0, (i+1)*400), (i+1)*400))
            t.append(time.time())
            ordena.ordenagraf()
            steps.append(ordena.steps)
            t[-1] = time.time()-t[-1]
        
        ax[0].plot(items,t, label = nombre)
        ax[1].plot(items,steps, label = nombre)    

    def CompararBigO():
        BigOSel.destroy()
        Botones.destroy()

        fig, ax = plt.subplots(1, 2, figsize=(12, 5))
        plt.subplots_adjust(wspace=0.5, hspace=0.6)

        for i in range(len(listaOrd2)):
            if listaOrd2[i] == "Bubble sort":
                ordenas = OrdenaBurbuja()
                ordenas.insert_sample(lista)
            if listaOrd2[i] == "Selection sort":
                ordenas = OrdenaSeleccion()
                ordenas.insert_sample(lista)
            if listaOrd2[i] == "Merge sort":
                ordenas = MergeSort2()
                ordenas.insert_sample(lista)
            if listaOrd2[i] == "Counting sort":
                ordenas = OrdenaConteo()
                ordenas.insert_sample(lista)
            if listaOrd2[i] == "Heap sort":
                ordenas = OrdenaHeap2()
                ordenas.insert_sample(lista)
            if listaOrd2[i] == "Quick sort":
                ordenas = QuickSort2()
                ordenas.insert_sample(lista)
            if listaOrd2[i] == "Shell sort":
                ordenas = OrdenaShell()
                ordenas.insert_sample(lista)
            if listaOrd2[i] == "Radix sort":
                ordenas = Radix()
                ordenas.insert_sample(lista)
            if listaOrd2[i] == "Insertion sort":
                ordenas = OrdenaInsercion()
                ordenas.insert_sample(lista)
            if ordenas:
                ordenas.insert_sample(lista)
                comparar(ordenas, ax, listaOrd2[i])

        ax[0].set_title("Tiempo")
        ax[0].set_xlabel("Items")
        ax[0].set_ylabel("Tiempo")

        ax[1].set_title("Big-O")
        ax[1].set_xlabel("Items")
        ax[1].set_ylabel("Pasos")

        ax[0].legend()
        ax[1].legend()

        ad = Label(GUI1, text = "La cantidad de steps y tiempo puede ser muy grandes entre un algoritmo y otro", fg="darkblue", font=("Calibri",12))
        ad.place(x = 200, y = 600, width = 700, height = 20)    

        canvas = FigureCanvasTkAgg(fig, master=GUI1)
        canvas.draw()
        canvas.get_tk_widget().configure(borderwidth=2,relief="solid")
        canvas.get_tk_widget().place(x = 75, y = 65)  

    def CompararBigOInversa():
        BigOSel.destroy()
        Botones.destroy()

        fig, ax = plt.subplots(1, 2, figsize=(12, 5))
        plt.subplots_adjust(wspace=0.5, hspace=0.6)

        for i in range(len(listaOrd2)):
            if listaOrd2[i] == "Bubble sort":
                ordenas = OrdenaBurbuja()
                ordenas.insert_sample(listaAl)
            if listaOrd2[i] == "Selection sort":
                ordenas = OrdenaSeleccion()
                ordenas.insert_sample(listaAl)
            if listaOrd2[i] == "Merge sort":
                ordenas = MergeSort2()
                ordenas.insert_sample(listaAl)
            if listaOrd2[i] == "Counting sort":
                ordenas = OrdenaConteo()
                ordenas.insert_sample(listaAl)
            if listaOrd2[i] == "Heap sort":
                ordenas = OrdenaHeap2()
                ordenas.insert_sample(listaAl)
            if listaOrd2[i] == "Quick sort":
                ordenas = QuickSort2()
                ordenas.insert_sample(listaAl)
            if listaOrd2[i] == "Shell sort":
                ordenas = OrdenaShell()
                ordenas.insert_sample(listaAl)
            if listaOrd2[i] == "Radix sort":
                ordenas = Radix()
                ordenas.insert_sample(listaAl)
            if listaOrd2[i] == "Insertion sort":
                ordenas = OrdenaInsercion()
                ordenas.insert_sample(listaAl)
            if ordenas:
                ordenas.insert_sample(listaAl)
                comparar(ordenas, ax, listaOrd2[i])

        ax[0].set_title("Tiempo")
        ax[0].set_xlabel("Items")
        ax[0].set_ylabel("Tiempo")

        ax[1].set_title("Big-O")
        ax[1].set_xlabel("Items")
        ax[1].set_ylabel("Pasos")

        ax[0].legend()
        ax[1].legend()

        ad = Label(GUI1, text = "La cantidad de steps y tiempo puede ser mayor en algunos casos", fg="darkblue", font=("Calibri",12))
        ad.place(x = 350, y = 600, width = 700, height = 20)    

        canvas = FigureCanvasTkAgg(fig, master=GUI1)
        canvas.draw()
        canvas.get_tk_widget().configure(borderwidth=2,relief="solid")
        canvas.get_tk_widget().place(x = 75, y = 65)

    def grafica(ordena, frame, larg, anch):
        global canvas, texto
        t, items,steps = [], [], []
        texto = ""

        for i in range(10):
            items.append((i+1)*200)
            ordena.insert_sample(lista[:(i+1)*200])
            t.append(time.time())
            ordena.ordenagraf()
            steps.append(ordena.steps)
            t[-1] = time.time() - t[-1]
            texto += "Tiempo con " + str((i+1)*200) + " elementos es de: " + str(t[-1])+" segundos\n"
            
        ancho_pulgadas = anch
        alto_pulgadas = larg

        # Conversión de pulgadas a píxeles (dpi: dots per inch)
        dpi = 100  # Puedes ajustar este valor según la resolución deseada
        ancho_px = ancho_pulgadas * dpi
        alto_px = alto_pulgadas * dpi

        # Crear una figura de Matplotlib con el tamaño especificado
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(ancho_pulgadas, alto_pulgadas), dpi=dpi)

        # Graficar los tiempos
        ax1.plot(items, t)
        ax1.set_title("Time")

        # Graficar los pasos
        ax2.plot(items, steps)
        ax2.set_title("Steps")

        # Ajustar el espaciado entre los subplots
        plt.subplots_adjust(wspace=0.5, hspace=0.5)

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def graficaAl(ordena, frame, larg, anch):
        global texto, canvasAl
        t, items,steps = [], [], []
        texto = ""

        for i in range(10):
            items.append((i+1)*200)
            ordena.insert_sample(listaAl[:(i+1)*200])
            t.append(time.time())
            ordena.ordenagraf()
            steps.append(ordena.steps)
            t[-1] = time.time() - t[-1]
            texto += "Tiempo con " + str((i+1)*200) + " elementos es de: " + str(t[-1])+" segundos\n"
            
        ancho_pulgadas = anch
        alto_pulgadas = larg

        # Conversión de pulgadas a píxeles (dpi: dots per inch)
        dpi = 100  # Puedes ajustar este valor según la resolución deseada
        ancho_px = ancho_pulgadas * dpi
        alto_px = alto_pulgadas * dpi

        # Crear una figura de Matplotlib con el tamaño especificado
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(ancho_pulgadas, alto_pulgadas), dpi=dpi)

        # Graficar los tiempos
        ax1.plot(items, t)
        ax1.set_title("Time")

        # Graficar los pasos
        ax2.plot(items, steps)
        ax2.set_title("Steps")

        # Ajustar el espaciado entre los subplots
        plt.subplots_adjust(wspace=0.5, hspace=0.5)

        canvasAl = FigureCanvasTkAgg(fig, master=frame)
        canvasAl.draw()
        canvasAl.get_tk_widget().pack()

    def MostrarBigO():
        global Bur, Sel, Ins,Coun, Mer, He, Qui, Sh, Rad, Co, Elementos
        BigOSel.destroy()
        Botones.destroy()
        n = len(listaOrd2)
        Indicaciones.destroy()

        BubbleFr = Frame (GUI1, bg = "gray")
        SelectionFr = Frame (GUI1, bg = "gray")
        InsertionFr = Frame (GUI1, bg = "gray")
        CountingFr = Frame (GUI1, bg = "gray")
        MergeFr = Frame (GUI1, bg = "gray")
        HeapFr = Frame (GUI1, bg = "gray")
        QuickFr = Frame (GUI1, bg = "gray")
        ShellFr = Frame (GUI1, bg = "gray")
        RadixFr = Frame (GUI1, bg = "gray")
        CombFr = Frame (GUI1, bg = "gray")

        frames.append(BubbleFr)
        frames.append(SelectionFr)
        frames.append(InsertionFr)
        frames.append(CountingFr)
        frames.append(MergeFr)
        frames.append(HeapFr)
        frames.append(QuickFr)
        frames.append(ShellFr)
        frames.append(RadixFr)
        frames.append(CombFr)

        Bur = Label(GUI1,text="1.", bg="darkblue", fg="white")
        Sel = Label(GUI1,text="2.", bg="darkblue", fg="white")
        Ins = Label(GUI1,text="3.", bg="darkblue", fg="white")
        Coun = Label(GUI1,text="4.", bg="darkblue", fg="white")
        Mer = Label(GUI1,text="5.", bg="darkblue", fg="white")
        He = Label(GUI1,text="6.", bg="darkblue", fg="white")
        Qui = Label(GUI1,text="7.", bg="darkblue", fg="white")
        Sh = Label(GUI1,text="8.", bg="darkblue", fg="white")
        Rad = Label(GUI1,text="9.", bg="darkblue", fg="white")
        Co = Label(GUI1,text="10.", bg="darkblue", fg="white")

        Bur.place(relx = 0.01, rely = 0.07, relwidth = 0.01, relheight = 0.02)
        Sel.place(relx = 0.26, rely = 0.07, relwidth = 0.01, relheight = 0.02)
        Ins.place(relx = 0.51, rely = 0.07, relwidth = 0.01, relheight = 0.02)
        Coun.place(relx = 0.76, rely = 0.07, relwidth = 0.01, relheight = 0.02)
        Mer.place(relx = 0.01, rely = 0.36, relwidth = 0.01, relheight = 0.02)
        He.place(relx = 0.26, rely = 0.36, relwidth = 0.01, relheight = 0.02)
        Qui.place(relx = 0.51, rely = 0.36, relwidth = 0.01, relheight = 0.02)
        Sh.place(relx = 0.76, rely = 0.36, relwidth = 0.01, relheight = 0.02)
        Rad.place(relx = 0.26, rely = 0.65, relwidth = 0.01, relheight = 0.02)
        Co.place(relx = 0.505, rely = 0.65, relwidth = 0.015, relheight = 0.02)
        

        BubbleFr.place(relx = 0.02, rely = 0.07, relwidth = 0.22, relheight = 0.27)
        SelectionFr.place(relx = 0.27, rely = 0.07, relwidth = 0.22, relheight = 0.27)
        InsertionFr.place(relx = 0.52, rely = 0.07, relwidth = 0.22, relheight = 0.27)
        CountingFr.place(relx = 0.77, rely = 0.07, relwidth = 0.22, relheight = 0.27)
        MergeFr.place(relx = 0.02, rely = 0.36, relwidth = 0.22, relheight = 0.27)
        HeapFr.place(relx = 0.27, rely = 0.36, relwidth = 0.22, relheight = 0.27)
        QuickFr.place(relx = 0.52, rely = 0.36, relwidth = 0.22, relheight = 0.27)
        ShellFr.place(relx = 0.77, rely = 0.36, relwidth = 0.22, relheight = 0.27)
        RadixFr.place(relx = 0.27, rely = 0.65, relwidth = 0.22, relheight = 0.27)
        CombFr.place(relx = 0.52, rely = 0.65, relwidth = 0.22, relheight = 0.27)

        for i in range(len(listaOrd2)):
            if listaOrd2[i] == "Bubble sort":
                ordenas = OrdenaBurbuja()
                ordenas.insert_sample(lista)
            if listaOrd2[i] == "Selection sort":
                ordenas = OrdenaSeleccion()
                ordenas.insert_sample(lista)
            if listaOrd2[i] == "Merge sort":
                ordenas = MergeSort2()
                ordenas.insert_sample(lista)
            if listaOrd2[i] == "Counting sort":
                ordenas = OrdenaConteo()
                ordenas.insert_sample(lista)
            if listaOrd2[i] == "Heap sort":
                ordenas = OrdenaHeap2()
                ordenas.insert_sample(lista)
            if listaOrd2[i] == "Quick sort":
                ordenas = QuickSort2()
                ordenas.insert_sample(lista)
            if listaOrd2[i] == "Shell sort":
                ordenas = OrdenaShell()
                ordenas.insert_sample(lista)
            if listaOrd2[i] == "Radix sort":
                ordenas = Radix()
                ordenas.insert_sample(lista)
            if listaOrd2[i] == "Insertion sort":
                ordenas = OrdenaInsercion()
                ordenas.insert_sample(lista)
            if listaOrd2[i] == "Comb sort":
                ordenas = OrdenaComb()
                ordenas.insert_sample(lista)
            grafica(ordenas, frames[i], 3, 5)
        
        Elementos = Label(GUI1, text = "1. Bubble sort \n 2. Selection sort \n 3. Insertion sort \n 4. Counting sort \n 5. Merge sort \n 6. Heap sort \n 7. Quick sort \n 8. Shell sort \n 9. Radix sort \n 10. Comb sort", font=("Calibri Light",11))
        Elementos.place(x = 1100, y = 490, width = 200, height = 200)

        global V1VFr

        V1VFr = Frame(GUI1, bg = "lightblue")
        V1VFr.configure(borderwidth=2,relief="solid")
        V1VFr.place(relx = 0.02, rely = 0.70, relwidth = 0.22, relheight = 0.15)
        Sig = Label(V1VFr, text = "Ver mejor la grafica \n e informacion de cada sort", fg="black", bg="lightblue",font=("Calibri Light",10))
        V1V = Button(V1VFr, text = "Click aqui", command = v1v, cursor="hand2")
        Sig.place(relx = 0.05, rely = 0.15, relwidth = 0.90, relheight = 0.30)
        V1V.place(relx = 0.3, rely = 0.55, relwidth = 0.40, relheight = 0.40)

    def MostrarBigOInversa():
        global Bur, Sel, Ins,Coun, Mer, He, Qui, Sh, Rad, Co, Elementos
        Indicaciones.destroy()
        BigOSel.destroy()
        Botones.destroy()
        n = len(listaOrd2)

        BubbleFr = Frame (GUI1, bg = "gray")
        SelectionFr = Frame (GUI1, bg = "gray")
        InsertionFr = Frame (GUI1, bg = "gray")
        CountingFr = Frame (GUI1, bg = "gray")
        MergeFr = Frame (GUI1, bg = "gray")
        HeapFr = Frame (GUI1, bg = "gray")
        QuickFr = Frame (GUI1, bg = "gray")
        ShellFr = Frame (GUI1, bg = "gray")
        RadixFr = Frame (GUI1, bg = "gray")
        CombFr = Frame (GUI1, bg = "gray")
        frames.append(BubbleFr)
        frames.append(SelectionFr)
        frames.append(InsertionFr)
        frames.append(CountingFr)
        frames.append(MergeFr)
        frames.append(HeapFr)
        frames.append(QuickFr)
        frames.append(ShellFr)
        frames.append(RadixFr)
        frames.append(CombFr)

        Bur = Label(GUI1,text="1.", bg="darkblue", fg="white")
        Sel = Label(GUI1,text="2.", bg="darkblue", fg="white")
        Ins = Label(GUI1,text="3.", bg="darkblue", fg="white")
        Coun = Label(GUI1,text="4.", bg="darkblue", fg="white")
        Mer = Label(GUI1,text="5.", bg="darkblue", fg="white")
        He = Label(GUI1,text="6.", bg="darkblue", fg="white")
        Qui = Label(GUI1,text="7.", bg="darkblue", fg="white")
        Sh = Label(GUI1,text="8.", bg="darkblue", fg="white")
        Rad = Label(GUI1,text="9.", bg="darkblue", fg="white")
        Co = Label(GUI1,text="10.", bg="darkblue", fg="white")

        Bur.place(relx = 0.01, rely = 0.07, relwidth = 0.01, relheight = 0.02)
        Sel.place(relx = 0.26, rely = 0.07, relwidth = 0.01, relheight = 0.02)
        Ins.place(relx = 0.51, rely = 0.07, relwidth = 0.01, relheight = 0.02)
        Coun.place(relx = 0.76, rely = 0.07, relwidth = 0.01, relheight = 0.02)
        Mer.place(relx = 0.01, rely = 0.36, relwidth = 0.01, relheight = 0.02)
        He.place(relx = 0.26, rely = 0.36, relwidth = 0.01, relheight = 0.02)
        Qui.place(relx = 0.51, rely = 0.36, relwidth = 0.01, relheight = 0.02)
        Sh.place(relx = 0.76, rely = 0.36, relwidth = 0.01, relheight = 0.02)
        Rad.place(relx = 0.26, rely = 0.65, relwidth = 0.01, relheight = 0.02)
        Co.place(relx = 0.505, rely = 0.65, relwidth = 0.015, relheight = 0.02)

        BubbleFr.place(relx = 0.02, rely = 0.07, relwidth = 0.22, relheight = 0.27)
        SelectionFr.place(relx = 0.27, rely = 0.07, relwidth = 0.22, relheight = 0.27)
        InsertionFr.place(relx = 0.52, rely = 0.07, relwidth = 0.22, relheight = 0.27)
        CountingFr.place(relx = 0.77, rely = 0.07, relwidth = 0.22, relheight = 0.27)
        MergeFr.place(relx = 0.02, rely = 0.36, relwidth = 0.22, relheight = 0.27)
        HeapFr.place(relx = 0.27, rely = 0.36, relwidth = 0.22, relheight = 0.27)
        QuickFr.place(relx = 0.52, rely = 0.36, relwidth = 0.22, relheight = 0.27)
        ShellFr.place(relx = 0.77, rely = 0.36, relwidth = 0.22, relheight = 0.27)
        RadixFr.place(relx = 0.27, rely = 0.65, relwidth = 0.22, relheight = 0.27)
        CombFr.place(relx = 0.52, rely = 0.65, relwidth = 0.22, relheight = 0.27)

        for i in range(len(listaOrd2)):
            if listaOrd2[i] == "Bubble sort":
                ordenas = OrdenaBurbuja()
                ordenas.insert_sample(listaAl)
            if listaOrd2[i] == "Selection sort":
                ordenas = OrdenaSeleccion()
                ordenas.insert_sample(listaAl)
            if listaOrd2[i] == "Merge sort":
                ordenas = MergeSort2()
                ordenas.insert_sample(listaAl)
            if listaOrd2[i] == "Counting sort":
                ordenas = OrdenaConteo()
                ordenas.insert_sample(listaAl)
            if listaOrd2[i] == "Heap sort":
                ordenas = OrdenaHeap2()
                ordenas.insert_sample(listaAl)
            if listaOrd2[i] == "Quick sort":
                ordenas = QuickSort2()
                ordenas.insert_sample(listaAl)
            if listaOrd2[i] == "Shell sort":
                ordenas = OrdenaShell()
                ordenas.insert_sample(listaAl)
            if listaOrd2[i] == "Radix sort":
                ordenas = Radix()
                ordenas.insert_sample(listaAl)
            if listaOrd2[i] == "Insertion sort":
                ordenas = OrdenaInsercion()
                ordenas.insert_sample(listaAl)
            if listaOrd2[i] == "Comb sort":
                ordenas = OrdenaComb()
                ordenas.insert_sample(listaAl)
            graficaAl(ordenas, frames[i], 3, 5)
        
        Elementos = Label(GUI1, text = "1. Bubble sort \n 2. Selection sort \n 3. Insertion sort \n 4. Counting sort \n 5. Merge sort \n 6. Heap sort \n 7. Quick sort \n 8. Shell sort \n 9. Radix sort \n 10. Comb sort", font=("Calibri Light",11))
        Elementos.place(x = 1100, y = 490, width = 200, height = 200)

        global V1VFr

        V1VFr = Frame(GUI1, bg = "lightblue")
        V1VFr.configure(borderwidth=2,relief="solid")
        V1VFr.place(relx = 0.02, rely = 0.70, relwidth = 0.22, relheight = 0.15)
        Sig = Label(V1VFr, text = "Ver mejor la grafica \n e informacion de cada sort", fg="black", bg="lightblue",font=("Calibri Light",10))
        V1V = Button(V1VFr, text = "Click aqui", command = v1vAl, cursor="hand2")
        Sig.place(relx = 0.05, rely = 0.15, relwidth = 0.90, relheight = 0.30)
        V1V.place(relx = 0.3, rely = 0.55, relwidth = 0.40, relheight = 0.40)

    def GenerarLista2():
        global lista, BigOSel, Indicaciones
        lista = random.sample(range(0,2000),2000)

        fig = Figure(figsize=(10, 4), dpi=130)

        RListLabel = Label(BigOSel, text = "Esta es la lista que vas a ordenar", bg = "gray", fg="white")
        RListLabel.pack()
            
        ax = fig.add_subplot(111)
        ax.bar(range(len(lista)), lista)
        ax.set_title("Lista Aleatoria")

        canvas = FigureCanvasTkAgg(fig, master=BigOSel)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
        global listaOrd2
        
        listaOrd2 = ["Bubble sort", "Selection sort", "Insertion sort", "Shell sort", "Quick sort", "Merge sort", "Counting sort", "Heap sort", "Radix sort", "Comb sort"]
        
        GenLista.destroy()

        ListaAl.place(relx = .3, rely = 0.25, relwidth = 0.2, relheight = 0.5)

        Indicaciones = Label(GUI1, text = "El proceso puede tardar un poco debido al tamaño de la lista")
        Indicaciones.place(x = 440, y = 110, width = 500, height = 20)    

        Mostrar = Button(Botones, text = "Mostrar Graficas", command = MostrarBigO, cursor="hand2")
        Mostrar.place(relx = .525, rely = 0.25, relwidth = 0.2, relheight = 0.5)

        Todo = Button(Botones, text = "Comparacion", command=CompararBigO, cursor="hand2")
        Todo.place(relx = 0.75, rely = 0.25, relwidth = 0.2, relheight = 0.5)

    def GenerarListaInversa():
        global listaAl, Indicaciones

        listaAl = []
        for i in range(2000,0,-1):
            listaAl.append(i)
        
        fig = Figure(figsize=(10, 4), dpi=130)

        RListLabel = Label(BigOSel, text = "Esta es la lista que vas a ordenar", bg = "gray", fg="white")
        RListLabel.pack()
            
        ax = fig.add_subplot(111)
        ax.bar(range(len(listaAl)), listaAl)
        ax.set_title("Lista Inversa")

        canvas = FigureCanvasTkAgg(fig, master=BigOSel)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
        global listaOrd2
        
        listaOrd2 = ["Bubble sort", "Selection sort", "Insertion sort", "Shell sort", "Quick sort", "Merge sort", "Counting sort", "Heap sort", "Radix sort", "Comb sort"]
        
        GenLista.destroy()

        ListaAl.place(relx = .3, rely = 0.25, relwidth = 0.2, relheight = 0.5)

        Indicaciones = Label(GUI1, text = "El proceso puede tardar un poco debido al tamaño de la lista")
        Indicaciones.place(x = 440, y = 110, width = 500, height = 20)    

        Mostrar = Button(Botones, text = "Mostrar Graficas", command = MostrarBigOInversa, cursor="hand2")
        Mostrar.place(relx = .525, rely = 0.25, relwidth = 0.2, relheight = 0.5)

        Todo = Button(Botones, text = "Comparacion", command=CompararBigOInversa, cursor="hand2")
        Todo.place(relx = 0.75, rely = 0.25, relwidth = 0.2, relheight = 0.5)

    Titulo = Label(GUI1, text= "Big-O  y  tiempos",background="darkred",foreground="white",font=("Castellar",18), height=1)
    Titulo.pack(fill=tk.X)

    Botones = Frame(GUI1, bg = "lightblue")
    Botones.place(x = 220, y = 50, width = 900, height = 50)

    global BigOSel

    BigOSel = Frame(GUI1, bg = "gray")
    BigOSel.configure(borderwidth=2,relief="solid")
    BigOSel.place(x = 77, y = 150, width = 1200, height = 500)

    RListLabel = Label(Botones, text = "Opciones  grafica: ", bg = "lightblue")
    RListLabel.place(relx = 0.025, rely = 0.35, relwidth = 0.3, relheight = 0.3)

    GenLista = Button(Botones, text = "Lista aleatoria", command = GenerarLista2, cursor="hand2")
    GenLista.place(relx = 0.3, rely = 0.25, relwidth = 0.2, relheight = 0.5)

    ListaAl = Button(Botones, text = "Lista inversa", command = GenerarListaInversa, cursor="hand2")
    ListaAl.place(relx = 0.6, rely = 0.25, relwidth = 0.2, relheight = 0.5)

    GUI1.protocol("WM_DELETE_WINDOW", close_window)

def BotonesVentanas():
        global Ventanas
        Ventanas = Frame(GUI1, bg = "lightblue") # Big O
        Ventanas.place(x = 420, y = 200, width = 500, height = 250)

        Pestaña = Label(Ventanas, text = "Ventana", bg = "lightblue",foreground="darkgreen")
        Pestaña.pack()
        
        Orde = Button(Ventanas, text = "Grafica Ordenamiento", command = Ventana1, cursor="hand2")
        Orde.place(relx = 0.25, rely = 0.23, relwidth = 0.5, relheight = 0.25)
        
        BigO = Button(Ventanas, text = "BIG O", command = Ventana2, cursor="hand2")
        BigO.place(relx = 0.25, rely = 0.58, relwidth = 0.5, relheight = 0.25)

        Frames1.append(Ventanas)

BotonesVentanas()

GUI1.mainloop()
