# defention
# call
#no arg, no return
def testfn1(): #function def
    print("Hello Its function")

testfn1()

################# with arg #################################

def testfn2(a,b):
    print("Its arg function\n Values are\na=",a)
    print("b=",b)

testfn2(15,63)
testfn2(b=15,a=63)

########### Default arg #####################################

print("Hello","Welcome")# sep =space end \n

def testfn2(a,b=63):
    print("\nIts def function\n Values are\na=",a)
    print("b=",b)

testfn2(15,63)
testfn2(b=15,a=63)
testfn2()
testfn2(13)

###############  #################

