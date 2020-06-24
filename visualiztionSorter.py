import sys
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter
from tkinter import Frame,Label,Entry,Button
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def swap(Array,i,j):
      if i!=j:
        Array[i],Array[j] = Array[j],Array[i]

def cocktailSort(Array):
    if len(Array)==1:
        return
    
    swapped = True
    for i in range(len(Array)-1):
        if not swapped:
            break
        swapped=False
        for j in range(len(Array) - 1 - i):
            if Array[j] > Array[j + 1]:
                swap(Array, j, j + 1)
                swapped = True
            yield Array
        if not swapped:
            break
        swapped=False
        for j in range(len(Array)-1-i,i,-1):
            if Array[j]<Array[j-1]:
                swap(Array,j,j-1)
                swapped=True
            yield Array

        

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

iteration = [0]

def update_fig(Array, rects, iteration, text):
    for rect, val in zip(rects, Array):
        rect.set_height(val)
    iteration[0] += 1
    text.set_text("# of operations: {}".format(iteration[0]))
         

def vp_start_gui(N,sort_type):
    global root
    root = tkinter.Tk()
    root.geometry("1000x700")
    root.title("Sorting Visualizer")
    app=tkinter.Frame(root)
    app.pack(fill='both',expand=1)
    iteration = [0]




    #creating the label
    app.labelElements = Label(app,text="Number of elements",width=20)
    app.labelElements.grid(row=0,column=1)

    #creating the box
    app.textElements = Entry(app,width=12)
    app.textElements.grid(row=1,column=1)
    app.textElements.insert(index=0,string=N)

    app.labelSort = Label(app,text="Sort Type",width=20)
    app.labelSort.grid(row=2,column=1)
    #creating the box
    app.textSort = Entry(app,width=12)
    app.textSort.grid(row=3,column=1)
    app.textSort.insert(index=0,string=sort_type)
    #plot button
    method=app.textSort.get()
    
    def getNum():
        refresh(int(app.textElements.get()),app.textSort.get())

    app.buttonPlot = Button(app,text="Plot",width=12, command=getNum)
    app.buttonPlot.grid(row=4,column=1)
    app.buttonPlot = Button(app,text="Exit",width=12, command=exitSort)
    app.buttonPlot.grid(row=5,column=1)


    Array = [x+1 for x in range(N)]
    random.shuffle(Array)

    if method == "b":
        title = "Bubble sort"
        generator = bubbleSort(Array)
    elif method == "i":
        title = "Insertion sort"
        generator = insertionSort(Array)
    elif method == "m":
        title = "Merge sort"
        generator = mergeSort(Array, 0, N - 1)
    elif method == "q":
        title = "Quicksort"
        generator = quickSort(Array, 0, N - 1)
    elif method == 'c':
        title = "Cocktail Shaker"
        generator = cocktailSort(Array)
    else:
        title = "Selection sort"
        generator = selectionSort(Array)



    app.fig, app.ax = plt.subplots()
    app.ax.set_title(title)
    bar_rect=app.ax.bar(range(len(Array)),Array,align="edge")
    app.ax.set_xlim(0, N)
    app.ax.set_ylim(0, int(1.07 * N))
    text = app.ax.text(0.02, 0.95, "", transform=app.ax.transAxes)

    def update_fig(Array, rects, iteration):
        for rect, val in zip(rects, Array):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))

    app.canvas = FigureCanvasTkAgg(app.fig, master=app)
    app.canvas.get_tk_widget().grid(column=0,row=6)
    app.ani = animation.FuncAnimation(app.fig,update_fig,fargs=(bar_rect, iteration),frames=generator,interval=1,repeat=False,cache_frame_data=False)
    root.mainloop()    


if __name__ == '__main__':
    def refresh(num,sort):
        root.destroy()
        vp_start_gui(num,sort)

    def exitSort():
        root.destroy()


    vp_start_gui(10,'b')