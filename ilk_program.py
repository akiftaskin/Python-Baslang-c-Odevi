print("Merhaba, Dünya!")

#Değişken Tanımlama Kuralları
#Değişken İsimleri harf veya _ ile başlamalıdır.
#Değişken sayı ile başlamaz.
#Türkçe karakter kullanılmaz.Yaş değil yas
#Büyük harfe duyarlıdır. (Ad ile ad farklıdır)
#Boşluk içermez boşluk yerlerinde _ kullanılır (soyadın, soy adin, soy_adim)

isim = "Ahmet"
yas = 25
boy = 1.80
ogrenci_mi = True

print(isim,"adlı kullanıcın yaşı:",yas)

ad = input("Adınızı giriniz:")
print("Merhaba,", ad, "!")

dogum_yili = int(input("Doğum yılınızı yazınız:"))
yas = 2025 - dogum_yili
print("Yaşınız:", yas)