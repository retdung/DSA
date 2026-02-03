import numpy as np, time
from numba import jit

@jit(nopython=True)
def partition(arr, low, high):
    mid = (low + high) // 2
    arr[mid], arr[high] = arr[high], arr[mid] 
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

@jit(nopython=True)
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def main():
    print(f"{'Quicksort':<10} | {'Time (ms)':<10}")
    times = []
    quick_sort(np.array([3., 1., 2.]), 0, 2) 

    for i in range(1, 11):
        filename = f"data{i:02d}.txt"
        with open(filename) as f:
            data = np.array(f.read().split(), dtype=np.float64)

        t0 = time.time()
        quick_sort(data, 0, len(data)-1)
        dt = (time.time() - t0) * 1000
        
        times.append(dt)
        print(f"{filename:<10} | {dt:.2f}")

    print(f"AVERAGE    | {np.mean(times):.2f} ms")

main()
