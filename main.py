# Perulangan / Pengulangan / Loop

print('Teguh')
print('Teguh')
print('Teguh')
print('Teguh')
print('Teguh')
print('Teguh')
print('Teguh')
print('Teguh')
print('Teguh')
print('Teguh')

# increment itu penambahan 1 angka ke variabel
i = 1
i += 1
print('Hasil increment = ',i)

# decrement itu pengurangan 1 angka ke variabel
i -= 1
print('hasil decrement = ', i)

# while loop
# start/inisiasi variabel
# while kondisi(true/false):
# kode program
# increment

# increment
# dari yang terkecil ke yang terbesar
i = 1
while i<=100:
    print('teguh ke',i )
    i += 1
print('=======================')
# decrement
# dari yang terbesar ke yang terkecil
i = 50
while i>= 10:
    print('teguh ke',i )
    i -= 1

# membuat deret kelipatan tiga
j = 3
while j< 50:
    print(j)
    j += 3

# for loop
# listangka = [1,2,3,4]
# for i in listangka:
# kode program

angka = [1,2,3,4,5]
for x in angka:
    print(x)

buah = ["Jambu", "Anggur", "Mangga", "Alpukat", "Jahe"]
for j in buah:
    print(j)

nama = {'Joni', 'Dori', 'Joni', 'Alvin'}
for k in nama:
    print(k)

for i in range(5,10):
  print(i)

firstname = 'andi'
for a in firstname:
    print(a)

ulang = 10
for i in range(ulang):
    print ("Perulangan ke-"+str(i))