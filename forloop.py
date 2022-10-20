l=("12",5,5.63,3+5j) #
l=[34,55,102,33,104,10001]

for i in l:
    print(i, type(i))


for i in range(10):  #(0,1,2,3,4,5,6,7)
    print(i)
print("i #####################")






for i in range(5,15):#5,6,7,8,9,10,11,12,13,14
    print(i)


print("##########################")

for i in range(5,20,2): #5,7,9,11,13,15,17,19
    print(i)

###################################
def factfn(a):
  """
    if f=0 number is negative
  """
  f=1 
  if a<0:
    f=0
  elif a==0:
    f=1
    
  else:
    for i in range(1,a+1):
       f=f*i
  return f
   
    
while 1:
    
    b=int(input("Enter element to be added"))
    r=factfn(b)

    if(r):
        print("The factorial of",b,"is",r)
    else:
        print("Negative number")