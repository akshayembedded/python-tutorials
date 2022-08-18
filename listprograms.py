############   LIST    #############
### 0  1  2  3  4   5   6
## -7 -6 -5 -4  -3 -2  -1  
a=[12,34,45,66,102,654,102]
print(a)

print(len(a))  # size of list

print(a[len(a)-1]) #lAST element using len function

######### index based
print(a[0]) #0th element
print(a[1]) #1st element

### positive & negative Index
print(a[-1]) #last element

######### Masking
print(a[:3])
print(a[2:5])
print(a[4:])
print(a[5:6])
print(a[-4:-6])  # a[-4:]  [66,102,654,102]   a[:-6] = [12]
print(a[-6:-4])  # a[:-4]  [12,34,45]   a[-6:] = [34,45,66,102,654,102]
a[6]=45
########### funct

a.append(1234)
a.insert(5,2) # 

print(a)

print(a.count(102))
print(a.index(102))
print(a.pop())
print(a)
print(a.pop(2))
print(a)
a.remove(102)
print(a)
a.reverse()
print(a)
#a.remove(1)
a.sort(reverse=1)
print(a)

a.clear()
print(a)


##############    Multiple data types     ###################
a=["Raju",56,"875412365",100000000.0,4+5j,True,]
print(a)
