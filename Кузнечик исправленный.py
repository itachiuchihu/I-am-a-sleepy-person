A=input().split()
for i in range (len(A)):
    A[i]=int(A[i])
t=int(input())
i=1
while i<=t:
    k=-1
    j=A[-1]
    c=0
    while abs(k)<=j:
        c=A[k]
        A[k]=A[k-1]
        A[k-1]=c
        k=k-1
    i+=1
print(A)

