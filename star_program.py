inp=input("enter list items:")
etc=inp.split()
for values in etc:
    for i in range(int(values)):
        print('*',end="")
    print("\n")
''' other way
inp=input("enter list items:")
etc=inp.split()
x=len(etc)
y=int(x)
for values in etc:
    y=int(values)
    print("\n")
    while(y>0):
        print("*",end="")
        y=y-1
'''

        



    

            

    
