# Kullanıcıdan bir sayı alırız. Bunu int() 'e dönüştürüz.
n = int(input("Bir sayı girin: "))

# Toplamı saklamak için değişken atarız. Başlangıç değeri "0"dır.
toplam = 0

# 1'den n'e kadar olan sayıları toplarız.
for i in range(1, n + 1):  
    toplam += i  # toplam = toplam + i

# Sonucu ekrana yazdırırız.Burada "n" değeri ne ise otomatik olarak çıktı alma satırına geçer.
print(f"1'den {n}'e kadar olan sayıların toplamı: {toplam}")
