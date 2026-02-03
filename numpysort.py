import numpy as np
import time

def main():
    print(f"{'Numpy':<10} | {'Time (ms)':<10}")
    times = []
    
    for i in range(1, 11):
        filename = f"data{i:02d}.txt"
        
        with open(filename) as f:
            data = np.array(f.read().split(), dtype=np.float64)

        t0 = time.time()
        np.sort(data)       
        dt = (time.time() - t0) * 1000
        times.append(dt)

        print(f"{filename:<10} | {dt:.2f}")
        
    print(f"AVERAGE    | {np.mean(times):.2f} ms")
main()
