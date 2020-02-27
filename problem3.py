l=[1, 2, 3, 2, 0, 65, 21, 4, 2, 10]
a=2
out=[]
for i in range(0,len(l)):
    if l[i] == a:
        out.append(i)
print(out)
