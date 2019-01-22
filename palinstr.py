import time
start_time = time.time()

t1=int(input())
for k in range(t1):
    s=input()
    s1=''
    sum=0
    n=len(s)
    f=0
    for i in range(n):
        for j in range(n):

            if sum<len(s[i:(n-j)]):
                t=s[i:(n-j)]
                if t==t[::-1]:
                    sum=len(t)
                    s1=t
            elif len(s[i:n])<sum:
                f=f+1
                break
        if f!=0:
            break         
    print(s1)                


print( (time.time() - start_time))

