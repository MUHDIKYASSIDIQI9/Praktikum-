def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

def fibonacci(n):
        if n == 1 or n == 2:
                return 1
        else:
                return fibonacci(n - 1) + fibonacci(n - 2)

print("Pilih menu:")
print("1. Faktorial")
print("2. Fibonacci")

pilihan = int(input("Masukkan pilihan (1/2): "))

if pilihan == 1:
    a = int(input("Masukkan angka untuk faktorial: "))
    cari_faktorial = faktorial(a)
    print("Nilai dari", a, "! adalah", cari_faktorial)

elif pilihan == 2:
    u = int(input("Masukkan batas deret Fibonacci: "))
    print("Deret Fibonacci: ", end='')
    print ("Hasilnya adalah : ", fibonacci (u))

else:
    print("Peringatan: Pilihan tidak valid! Harap masukkan 1 atau 2.")
