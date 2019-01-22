import time
start_time = time.time()
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        if j==1 or j==i:
            print(1,end=' ')
        else:
            print(i-1,end=' ')    
    print(' ')
print( (time.time() - start_time))

