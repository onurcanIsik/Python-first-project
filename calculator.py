


x = int(input("Bir X sayısı giriniz : "));
y = int(input("Bir Y sayısı giriniz : "));
print("İslemler = 1-Toplama, 2-Çıkarma, 3-Bölme, 4-Çarpma")
islem = int(input("Bir İslem Seçiniz : "))
sonuc = 0;


if (islem ==1 ) : sonuc = x + y;
elif (islem ==2) : sonuc = x-y;
elif (islem ==3) : sonuc = x/y;
else : sonuc = x*y;


print(sonuc)


