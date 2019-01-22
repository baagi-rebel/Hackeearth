s,s1=input().split()
list=[]
sum=0
def lcs(s,s1,i,j):
    if i>0 and j>0:
        if s[i]==s[j]:
            return 1
        else:
            sum=0
            sum+=max(lcs(s,s1,i,j-1),lcs(s,s1,i-1,j))
            return sum

print(lcs(s,s1,len(s)-1,len(s1)-1))

'''
def fun(s,n):
    if n>0:
        list.append(s[0:n])
        return fun(s,n-1)
    else:
        return list    
    print('hello')

print(fun(s,len(s)))
'''