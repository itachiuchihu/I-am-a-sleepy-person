N=int(input())
i=1
A=[]
C=[]
while i<=(N+1):
    B=[]
    if i==1:
        A=A+[1]
        print(A)
    elif i==2:
        A=A+[1]
        print(A)
    else:
        for k in range(len(A)):
            if k!=len(A)-1:
                B=B+[A[k]+A[k+1]]
        if i<=3:
            C=C+[A[0]]+B+[A[1]]
            print(C)
        else:
            C=[1]+B+[1]
            print(C)
        A=C
    i+=1




