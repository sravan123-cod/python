n =int(input("enter thenumber of rows"))
for i in range(1,n):
    for j in range(i):
        print("*",end ="")
    print()

n =int(input("enter the number of rows"))
for e in range(n,1,-1):
    for g in range (e,1,-1):
        print("*",end ="")
    print()

def no_notes(a):
    Q=[500,200,100,50,20,10]
    x=0
    for i in range(6):
        q=Q[i]
        x=a//q
        print("Notes of {}={}".format(q,x))
        a=a%q
amount=(int(input("enter total amount ")))
no_notes(amount)

