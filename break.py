# break adalah untuk menghentikan perulangan

i = 1
while i<50 :
    print(i)
    break

i = 1
while i <= 10:
    print(i,'x', i, '=', i*i)
    if i == 5:
        break
    i += 1

for i in range(1, 11):
    print(i, 'x' , i, "= ", i*i)
    if i == 5:
        break

