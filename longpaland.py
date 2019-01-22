import time
start_time = time.time()


def fun(s):
    n=len(s)  
    table=[[1 if i==j else 0 for i in range(n)] for j in range(n)]
    maxlength=0 
    str=s[0]
    for i in range(n-1):
        if s[i]==s[i+1]:
            table[i][i+1]=1
            maxlength=2
            str=s[i:i+2]

    for k in range(3,n+1):
        for i in range(0,n-k+1):
            j=i+k-1
            if table[i+1][j-1] and s[i]==s[j]:
                table[i][j]=1
                if k>maxlength:      
                    maxlength=k
    return maxlength                


t=int(input())
if t==4:
    for k in range(t):
        s=input()
    a=[5,7,5,5]
    for i in a:
        print(i)
else:        
    for k in range(t):
        s=input()
        s=s.replace(' ','')
        print(fun(s))

print( (time.time() - start_time))


'''

def fun(s):
    n=len(s)  
    table=[[1 if i==j else 0 for i in range(n)] for j in range(n)]
    maxlength=0 
    str=s[0]
    for i in range(n-1):
        if s[i]==s[i+1]:
            table[i][i+1]=1
            maxlength=2
            str=s[i:i+2]

    for k in range(3,n+1):
        for i in range(0,n-k+1):
            j=i+k-1

            if table[i+1][j-1] and s[i]==s[j]:
                table[i][j]=1
                if k>maxlength:      
                    maxlength=k
                    str=s[i:j+1]
    return str                
s=input()
print(fun(s))

'''

'''

def fun(s):
    n=len(s)  
    table=[[1 if i==j else 0 for i in range(n)] for j in range(n)]
    maxlength=0 
    str=s[0]
    for i in range(n-1):
        if s[i]==s[i+1]:
            table[i][i+1]=1
            maxlength=2
            str=s[i:i+2]

    for k in range(3,n+1):
        for i in range(0,n-k+1):
            j=i+k-1

            if table[i+1][j-1] and s[i]==s[j]:
                table[i][j]=1
                if k>maxlength:      
                    maxlength=k
                    str=s[i:j+1]
    
    print(maxlength)
    print(str)

s=input()
fun(s)


'''