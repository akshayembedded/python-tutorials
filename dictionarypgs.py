a={"Raju":"7845123265"} # key : value
details={"Mob":"7845123265","Tel":"0497251436","Age":42}
r={"raju":details}


print(a)
print(details)
print(r)

################### functions ########################
print(details["Mob"])
print(details.items())
print(details.keys())
print(details.values())

print(r.keys())
print(r.values())

c=dict.fromkeys(details,0)            #c=dict.fromkeys(["Ramu","Rahim","rajesh"],0)
print(c)
c["Mob"]="987654321"
c["Tel"]="0497123456"
print(c.get("Mob"))
print(c["Mob"])