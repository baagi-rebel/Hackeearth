t=int(input())
for k in range(t):
    n,x,y=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    sum1=0
    for i in range(len(a)):
        if a[i]>b[i] and x>0:
            sum1+=a[i]
            x=x-1
        elif b[i]>a[i] and y>0:
            sum1+=b[i]
            y=y-1    
        elif a[i]==b[i]:
            if x>y:
                sum1+=a[i]
                x=x-1
            elif y>x:
                sum1+=b[i]
                y=y-1
            else:    
                sum1+=a[i]
                x=x-1
                        
        elif y==0 and x!=0:
            sum1+=sum(a[i:n])
            break
        elif x==0 and y!=0:
            sum1+=sum(b[i:n])
            break


    print(sum1)                 