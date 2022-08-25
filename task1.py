a=list("abcdefghijklmnobqrstuvwxyz")
print(list(a))
val=0
name=input("enter name :")
for x in range(len(name)):
    if name[x] in a:
    #    print(name[x])
       val += a.index(name[x])
print(val)