ke = open('file.txt', 'r+')
toaddr1 = [i.strip() for i in ke.readlines()]
# toaddr = ke.readlines()
print(toaddr1)
temp2 = ke.readlines()
a = []
for li in temp2:
    a.append(li.strip())

print(a[1])
ke.close()