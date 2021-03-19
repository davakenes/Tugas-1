a = (input("Masukkan Nilai Ujian Teori Anda : "))
x = float(a)
b = (input("Masukkan Nilai Ujian Praktek Anda : "))
y = float(b)

if x >= 70 and y >=70 :
    print("Selamat, Anda Lulus !")
elif x >=70 and y < 70 :
    print("Anda harus mengulang ujian praktek")
elif x < 70 and y >= 70 :
    print("Anda harus mengulang ujian teori")
else :
    print("Anda harus mengulang ujian teori dan praktek")