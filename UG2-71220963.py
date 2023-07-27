def volumetabung(diameter,tinggi):
    phi = 3.14
    r = diameter / 2
    volume = phi * r**2*tinggi
    return volume
def volumekubus(sisi):
    kubus = sisi**3
    return kubus
def volumebalok(p, l, t):
    balok = p*l*t
    return balok
print("========= KALKULATOR CERDAS =========")
print("1. Tabung")
print("2. Kubus")
print("3. Balok")
pilihan = int(input("Pilihlah bangung yang ingin anda hitung (inputan angka saja): "))
if pilihan == 1:
    diameter = int(input("Masukkan diameter (cm) : "))
    tinggi = int(input("Masukkan tinggi (cm) : "))
    print("Volume tabung adalah ",volumetabung(diameter,tinggi),"cm")
elif pilihan == 2:
    sisi = int(input("Masukkan sisi (cm): "))
    print("Volume kubus adalah ", volumekubus(sisi),"cm")
elif pilihan == 3:
    p = int(input("Masukkan panjang (cm): "))
    l = int(input("Masukkan lebar (cm): "))
    t = int(input("Masukkan tinggi (cm): "))
    print("Volume balok adalah ", volumebalok(p,l,t),"cm")
else: 
    print("Inputan yang anda masukka salah !!")  