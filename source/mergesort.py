import numpy as np, time
from numba import jit

@jit(nopython=True)
def merge(arr, l, m, r, temp):
    i, j, k = l, m + 1, l
    while i <= m and j <= r:
        if arr[i] <= arr[j]: temp[k] = arr[i]; i += 1
        else: temp[k] = arr[j]; j += 1
        k += 1
    while i <= m: temp[k] = arr[i]; i += 1; k += 1
    while j <= r: temp[k] = arr[j]; j += 1; k += 1
    for i in range(l, r+1): arr[i] = temp[i]

@jit(nopython=True)
def merge_sort(arr, l, r, temp):
    if l < r:
        m = (l + r) // 2
        merge_sort(arr, l, m, temp)
        merge_sort(arr, m + 1, r, temp)
        merge(arr, l, m, r, temp)

def main():
    print(f"{'Mergesort':<10} | {'Time (ms)':<10}")
    times = []
    d = np.array([3., 1., 2.]); merge_sort(d, 0, 2, np.zeros_like(d))

    for i in range(1, 11):
        filename = f"data{i:02d}.txt"
        with open(filename) as f:
            data = np.array(f.read().split(), dtype=np.float64)
            
        temp = np.empty_like(data)

        t0 = time.time()
        merge_sort(data, 0, len(data)-1, temp)
        dt = (time.time() - t0) * 1000
        
        times.append(dt)
        print(f"{filename:<10} | {dt:.2f}")

    print(f"AVERAGE    | {np.mean(times):.2f} ms")

main()
