N=int(input())
i=0
B=[]
while i<N:
    A=input().split()
    for k in range (2):
        A[k]=int(A[k])
    B=B+A
    i+=1
T=int(input())
i=0
S=0
while i<=(len(B)-2):
    C=[]
    C=C+[B[i]]+[B[i+1]]
    if (T>=C[0])and(T<=C[1]):
        S+=1
    i=i+2
print('Answer=',S)




