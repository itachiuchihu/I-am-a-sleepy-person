A=input().split()
for i in range (len(A)):
    A[i]=int(A[i])
print(A[0])
i=0
S=0
M=0
while i<len(A):
    if A[i]==2:
        if (i!=len(A)-1)and(A[i+1]==2):
            S=S+A[i]
        elif i==len(A)-1:
            S=S+A[i]
        else:
            M+=1
    else:
        S=S+A[i]
    i+=1
result=int(S/(len(A)-M))
print('Mark=',result)

