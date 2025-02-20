# Kullanıcıdan iki sayı alırız.
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

# İşlemleri yapıp ve ekrana yazdırırız.
# 'f-string' ile değişkenlerin değerlerini içinde ifade etmek çok daha kolay olur.
print(f"Toplama: {sayi1} + {sayi2} = {sayi1 + sayi2}")
print(f"Çıkarma: {sayi1} - {sayi2} = {sayi1 - sayi2}")
print(f"Çarpma: {sayi1} * {sayi2} = {sayi1 * sayi2}")
print(f"Bölme: {sayi1} / {sayi2} = {sayi1 / sayi2}")
print(f"Mod Alma: {sayi1} % {sayi2} = {sayi1 % sayi2}")
print(f"Üs Alma: {sayi1} ** {sayi2} = {sayi1 ** sayi2}")