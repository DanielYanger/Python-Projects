from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import tkinter as tk
from tkinter import Frame,Label,Entry,Button
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def swap(Array,i,j):
      if i!=j:
        Array[i],Array[j] = Array[j],Array[i]

def bubbleSort(Array):
        if len(Array)==1:
            return
        
        swapped=True
        for i in range(len(Array)-1):
            if not swapped:
                break
            swapped=False
            for j in range(len(Array) - 1 - i):
                if Array[j] > Array[j + 1]:
                    swap(Array, j, j + 1)
                    swapped = True
                yield Array    

def insertionSort(Array):
        for i in range(1,len(Array)):
            j=i
            while j>0 and Array[j]<Array[j-1]:
                swap(Array,j,j-1)
                j-=1
                yield Array    

def mergeSort(Array, start, end):

        if end <= start:
            return

        mid = start + ((end - start + 1) // 2) - 1
        yield from mergeSort(Array, start, mid)
        yield from mergeSort(Array, mid + 1, end)
        yield from merge(Array, start, mid, end)
        yield Array    

def merge(Array, start, mid, end):
        
        merged = []
        leftIdx = start
        rightIdx = mid + 1

        while leftIdx <= mid and rightIdx <= end:
            if Array[leftIdx] < Array[rightIdx]:
                merged.append(Array[leftIdx])
                leftIdx += 1
            else:
                merged.append(Array[rightIdx])
                rightIdx += 1

        while leftIdx <= mid:
            merged.append(Array[leftIdx])
            leftIdx += 1

        while rightIdx <= end:
            merged.append(Array[rightIdx])
            rightIdx += 1

        for i, sorted_val in enumerate(merged):
            Array[start + i] = sorted_val
            yield Array    


def quickSort(Array, start, end):
        if(start>=end):
            return

        pivot=Array[end]
        pivotIdx = start

        for i in range(start,end):
            if Array[i]<pivot:
                swap(Array,i,pivotIdx)
                pivotIdx+=1
            yield Array
        swap(Array, i+1,pivotIdx)
        yield Array

        yield from quickSort(Array,start,pivotIdx-1)
        yield from quickSort(Array,pivotIdx+1,end)    

def selectionSort(Array):
        if len(Array)==1:
            return
        
        for i in range(len(Array)):
            minVal = Array[i]
            minIdx = i
            for j in range(i,len(Array)):
                if Array[j]<minVal:
                    minVal=Array[j]
                    minIdx=j
                yield Array
            swap(Array,i,minIdx)
            yield Array    

class Window(Frame):

    

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()


    def Clear(self):
        x=0

#    def Plot(self):
#        x=0


    def init_window(self):


        iteration = [0]

        def update_fig(Array, rects, iteration):
          for rect, val in zip(rects, Array):
              rect.set_height(val)
          iteration[0] += 1
          text.set_text("# of operations: {}".format(iteration[0]))
        self.master.title("Use Of FuncAnimation in tkinter based GUI")
        self.pack(fill='both', expand=1)     

#Create the controls, note use of grid

        self.labelSpeed = Label(self,text="Speed (km/Hr)",width=12)
        self.labelSpeed.grid(row=0,column=1)
        self.labelAmplitude = Label(self,text="Amplitude",width=12)
        self.labelAmplitude.grid(row=0,column=2)

        self.textSpeed = Entry(self,width=12)
        self.textSpeed.grid(row=1,column=1)
        self.textSpeed.insert(index=0,string='10')
        self.textAmplitude = Entry(self,width=12)
        self.textAmplitude.grid(row=1,column=2)


#        self.buttonPlot = Button(self,text="Plot",command=self.Plot,width=12)
        self.buttonPlot = Button(self,text="Plot",width=12)
        self.buttonPlot.grid(row=2,column=1)
        
        self.buttonClear = Button(self,text="Clear",command=self.Clear,width=12)
        self.buttonClear.grid(row=2,column=2)

#        self.buttonClear.bind(lambda e:self.Plot)
        self.buttonClear.bind(lambda e:self.Clear)


        N=(int(self.textSpeed.get()))
        tk.Label(self,text="SHM Simulation").grid(column=0, row=3)
        Array = [x+1 for x in range(N)]
        random.shuffle(Array)
        self.fig, self.ax = plt.subplots()
        self.ax.set_title("Bubble Sort")
        bar_rect=self.ax.bar(range(len(Array)),Array,align="edge")
        self.ax.set_xlim(0, N)
        self.ax.set_ylim(0, int(1.07 * N))
        text = self.ax.text(0.02, 0.95, "", transform=self.ax.transAxes)
          


        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().grid(column=0,row=4)
  
        self.ani = animation.FuncAnimation(self.fig,update_fig,fargs=(bar_rect, iteration),frames=bubbleSort(Array),interval=1,repeat=False)

    
   


root = tk.Tk()
root.geometry("1500x700")
app = Window(root)
tk.mainloop()
