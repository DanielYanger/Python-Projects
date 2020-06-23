import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


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


if __name__ == "__main__":
    N = int(input("Enter number of integers: "))
    method_msg = "Enter sorting method:\n(b)ubble\n(i)nsertion\n(m)erge \
        \n(q)uick\n(s)election\n"
    method = input(method_msg)

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
    else:
        title = "Selection sort"
        generator = selectionSort(Array)
    
    fig, ax = plt.subplots()
    ax.set_title(title)
    bar_rect=ax.bar(range(len(Array)),Array,align="edge")
    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.07 * N))
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    iteration = [0]
    def update_fig(Array, rects, iteration):
        for rect, val in zip(rects, Array):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))
    
    anim = animation.FuncAnimation(fig,update_fig,fargs=(bar_rect, iteration),frames=generator,interval=1,repeat=False)
    plt.show()
