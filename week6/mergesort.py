#!/usr/bin/env python3 
import random, time
import threading, copy
from collections import deque

def mergesort(L, data):

    if not L: return L
    
    q = deque([[e] for e in L])

    while len(q) > 1:
        q.append(merge(q.popleft(), q.popleft()))
    
    ans = q.popleft()
    data.append(ans)
    return(ans)
       
def merge(L1,L2):
    if not L1 or not L2: return (L1 if not L2 else L1)

    ans = []
    c1,c2 = 0,0
    while c1 < len(L1) and c2 < len(L2):
        if L1[c1] < L2[c2]:
            ans.append(L1[c1])
            c1 += 1
        else:
            ans.append(L2[c2])
            c2 += 1
    ans += (L2[c2:] if c2 < len(L2) else L1[c1:])
    return ans


if __name__ == "__main__":
    L = [random.randint(1,1000000) for _ in range(1000000)] 
    L1 = copy.deepcopy(L)
    ans = []
    start = time.time()
    mergesort(L1, ans)
    end = time.time()
    print(end - start)
    
    
    #print(L)
    
    l1 = L[:len(L)//3]
    l2 = L[len(L)//3:2*len(L)//3]
    l3 = L[2*len(L)//3:]
    t1 = threading.Thread(None, mergesort, "Thread 1",[l1, ans])
    t2 = threading.Thread(None,mergesort, "Thread 2",[l2,ans])
    t3 = threading.Thread(None,mergesort, "Thread 3",[l3,ans])

    start = time.time()
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()

    fin = merge(ans.pop(),ans.pop())
    fin = merge(fin, ans.pop())
    end = time.time()
    print(end - start)
    #print(fin, len(fin))