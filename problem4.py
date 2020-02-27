l=[1, 1, 2, 3, 4, 64, 35, 93, 35, 87, 4, 3]
out=[]
for i in  l:
        if i  not in out:
            out.append(i)
print(out)