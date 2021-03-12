# continue mirip seperti break, hanya saja jika
# dalam break perulangan langsung berhenti, dan
# continue hanya melewati sekali aja

# struktur continue
# for i in range(1,x):
    # if kondisi:
        # continue
            # kode program

for i in range(1, 11):
    if i == 7:
        continue
    print(i, 'x', i, '=', i*i)

angka = [1,2,3,4,5]
for x in angka:
    if x  >= 3:
        continue
    print(x)


for x in range(2, 30, 3):
    print(x)

