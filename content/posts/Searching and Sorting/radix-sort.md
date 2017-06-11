Title: Radix Sort - Sıralama Algoritmaları
Date: 2014-12-03 01:53
Author: Burak
Category: Algoritma
Tags: algorithm, sorting
Slug: radix-sort

Türkçe'de taban sıralaması , basamaklı sıralama , kök sıralaması veya
hane sıralaması olarak geçen bu algoritmada sıralanacak olan veriler
hanelerine göre sıralanır.En değersiz olan haneden en değerli haneye
doğru sıralama işlemi yapılır.

Sıralanacak verilerin tamsayı olduğu durumlarda kullanılan bu algoritma
işlenirken ilk olarak sıralanacak olan veri kümesindeki elemanların en
büyük elemanının kaç basamaklı olduğu tespit edildikten sonra sayıların
en değersiz olan basamağından itibaren incelenmeye başlanır ve yeni bir
diziye yerleştirilir.Bu işlem dizinin en büyük elemanının basamak sayısı
kadar tekrar edilir.

Bu algoritmanın çalışma zamanı O(nk) ve yer karmaşıklığı O(n+k)
olacaktır.Gayet iyi bir çalışma zamanına sahip olmasının nedeni bu
algoritmanın karşılaştırmalı bir sıralama algoritması olmamasıdır.En
büyük dezavantajı ise her basamak işlemi için yeni bir bellek alanı
gerektirmesidir.

<span style="color: #ff9900;">**Direkt Basamaklı SIralama ( Straight
Radix Sort)**</span> algoritmasına bir örnek verelim.

Sayılarımız : 32 , 224 , 16 , 15 , 31 , 169 , 123 , 252 olsun ve
çözümümüz için aşağıdaki gibi bir tablo ile daha rahat işlemlerimiz
anlaşılır.

İlk olarak sayılar aşağıdaki gibi tabloya yerleştirildi.  
[jtable]  
Hane3,Hane2,Hane1  
0,3,2  
2,2,4  
0,1,6  
0,1,5  
0,3,1  
1,6,9  
1,2,3  
2,5,2[/jtable]  
Hane1'e göre sıralama gerçekleştirildi.  
[jtable]  
Hane3,Hane2,Hane1  
0,3,1  
0,3,2  
2,5,2  
1,2,3  
2,2,4  
0,1,5  
0,1,6  
1,6,9  
[/jtable]  
Hane1 sıralaması bittikten sonra Hane2 sıralaması gerçekleştirildi.  
[jtable]  
Hane3,Hane2,Hane1  
0,1,5  
0,1,6  
1,2,3  
2,2,4  
0,3,1  
0,3,2  
2,5,2  
1,6,9  
[/jtable]  
ve son olarak maksimum sayımızın hane sayısına ulaşıldı ve Hane3'e göre
sıralama gerçekleştirildi.  
[jtable]  
Hane3,Hane2,Hane1  
0,1,5  
0,1,6  
0,3,1  
0,3,2  
1,2,3  
1,6,9  
2,2,4  
2,5,2  
[/jtable]

Her şey güzel peki sayının kaç basamaklı olduğunu nereden anlayacağız
diyorsanız.

> basamak sayısı = int(log(taban,max) + 1)

Örneğin üstteki örneğimizde en büyük eleman 252 sayısı ve bu sayılar 10
tabanındadır.Dolayısı ile  
log(10,252) + 1 = 3,401 olur ve bunu int çevirirsek = 3 çıkar.Şimdi bu
algoritmamızın örnek kodlarına gelelim.  

[gist:id=7160796469da0dc175b0]

<span style="color: #ff9900;">**Basamaklı Yer Değiştirme
Sıralaması(Radix Exchange Sort)**</span>

Şimdi direkt yerleştirmeli sıralamanın düzenlemiş hali olan Basamaklı
Yer Değiştirme Sıralaması'nı inceleyelim.Kısaca farkları şudur.Direkt
basamaklı sıralama algoritmasında sağdan-sola doğru yol alınırken bu
yaklaşımda soldan-sağa doğru yol alınır ve en önemli avantajı bu
algoritmada her basamak için özel bir bellek alanına ihtiyaç
duyulmayacaktır.Bu algoritma içerisinde[Quick Sort(Hızlı
Sıralama)](http://blog.koseburak.net/quick-sort/) algoritması
kullanılmıştır.

Sayılar ikili(binary) olarak tutulduğundan taban değişimi için ek bir
işlem yapılmasına gerek yoktur.Algoritmanın kodunu verirken biraz
modifiye ettiğimden söz etmeliyim.Ufak değişiklikler ile negatif sayılar
içinde işleyebilmesi için düzenledim.

[gist:id=4f95b6ad2890d02759e7]

BURAK KÖSE
