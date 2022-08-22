l=[]
while 1:
    l.append(int(input("Enter element to be added")))
    op=input("Do you want to continue (y/n):")
    if(op=="n"):
        break

for i in l:
    print(i)