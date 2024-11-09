import os
import time

def random(a:int=48271, c:int=0, m:int=2**31-1, n:int=None, seed=None, numRange:list[int]=None) -> int:#C++11's minstd_rand
    if seed is None: #iterasi pertama
        x0 = int(os.getpid() + time.time())
    else:
        x0 = seed
    if n is None:
        n = random(n=1, numRange=[2,10])
    for _ in range(n):
        x0 = (a * x0 + c) % m
    if numRange is None: #saat tidak dimasukkan daerah hasil yang diinginkan
        return x0
    else:
        hasil = int((x0 / (m - 1)) * (numRange[1] - numRange[0]) + numRange[0])
        if hasil == numRange[1]:
            hasil - 1
        return hasil
