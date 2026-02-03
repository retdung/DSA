import numpy as np, time
from numba import jit

@jit(nopython=True)
def heapify(arr, n, i):
    largest, l, r = i, 2*i + 1, 2*i + 2
    if l < n and arr[l] > arr[largest]: largest = l
    if r < n and arr[r] > arr[largest]: largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

@jit(nopython=True)
def heap_sort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1): heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def main():
    print(f"{'Heapsort':<10} | {'Time (ms)':<10}")
    times = []
    heap_sort(np.array([3., 1., 2.]))

    for i in range(1, 11):
        filename = f"data{i:02d}.txt"
        with open(filename) as f:
            data = np.array(f.read().split(), dtype=np.float64)

        t0 = time.time()
        heap_sort(data)
        dt = (time.time() - t0) * 1000
        
        times.append(dt)
        print(f"{filename:<10} | {dt:.2f}")

    print(f"AVERAGE    | {np.mean(times):.2f} ms")
  
main()
