name = input("Masukkan nama Anda : ").lower()

namekapital = f"Halo, {name.upper()}!"

tengah = namekapital.center(50,"-")
print(tengah)

print("Jumlah huruf vokal yang terdapat pada nama Anda")
print("'a' =", name.count('a'), "'i' =", name.count('i'), "'u' =", name.count('u'), "'e' =", name.count('e'), "'o' =", name.count('o'))