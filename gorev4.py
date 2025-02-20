# Kullanıcıdan metin alırız.
metin = input("Bir metin girin: ")

# Ters çevirilmiş metni saklamak için boş bir string oluştururuz.
ters_metin = ""

# Metnin son karakterinden ilk karakterine doğru döngü oluştururuz.
# '-1' döngünün bitiş koşuludur ve burada döngünün 0. indekse kadar (0 dahil) devam etmesi gerektiğini belirtiriz.

for i in range(len(metin) - 1, -1, -1):  
    ters_metin += metin[i]  # Karakteri ekle

# Sonucu ekrana yazdırırız.
print("Ters çevrilmiş metin:", ters_metin)
