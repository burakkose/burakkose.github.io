Title: Rastgele Sayı Üretmek
Date: 2014-12-05 05:57
Author: Burak
Category: Algoritma
Tags: algorithm, random, number theory
Slug: rastgele-sayi

Rastgele yani tesadüfen , tesadüfi olarak , ayırmadan , seçmeden
anlamındadır.Çoğumuz yazdığımız kodu test ederken , oyun programlarken
ve çişitli hesaplamarda kullanırız rastgele sayıları.Günlük hayatta
rastgele kavramı insalar için keyfi olarak kullanılır.Aklınızdan bir
sayı tutup söylersiniz bu bir rastgele işlemidir.Peki gerçekten
böylemidir,bilgisayarlar için de durum bu mudur?

Hep verilen bir örnek vardır , zar.Zar atma olayı rastgele midir ? Bize
göre evet fakat matematikte durum böyle değildir.Zarın hangi sayı
gelmesi bir çok etkene bağlıdır.Bunlar sürtünme,ağırlık,yerçekimi,hız vs
gibi.Dolayısı ile gelecek sayının ne olduğu kestirilemediği için
rastgele denilir.

Biraz daha zorlayalım , mesela aklınzdan bir sayı tutup söyleme
gerçekten de rastgele midir ? Değildir. Çok hızlı karar verdiğimiz için
nasıl seçtiğimizi pek anlayamayız.Aslında bizim söyleyeceğimiz sayınında
etkenleri vardır.Örneğin favori sayımız , söylenecek sayının
sınırlandırılması gibi.

Uygulamamızda rastgele sayı elde etmek için çeşitli kütüphaneler ,
metodlar bulunur.Peki bunlar nasıl rastgele sayı üretiyorlar.Şimdi bir
kaç rastgele sayı üretme algoritmasına bakalım.

<span style="color: #ff6600;">**1\# Orta kare yöntemi ( 4r )**</span>

Bu algoritma [John von
Neumann](https://tr.wikipedia.org/wiki/John_von_Neumann) ve ekip
arkadaşları tarafından ortaya atılmıştır.Kabaca şu şekilde gerçekleşir.

> 1- 4r basamaklı bir sayı seçilir.'r' bir tamsayıdır.  
>  2- Sayının sağdan ve soldan 'r' adet basamağı silinir.  
>  3- Geriye kalan '2r' basamaklı sayının karesi bulunur fakat 'r'
> sayısının tamsayı olması gerektiğini unutmayın.Kare alma işleminden
> sonra elimizde tekrar 4r basamaklı bir sayı bulunur.  
>  4- Tekrar yeni bir sayı üretilmek istenirse 2. adıma geri dönülür.

Bir örnek verelim.Sayımız 81.599.441 olsun.Tamamen salladığım bir sayı.8
basamaklıdır dolayısı ile r = 2 olur.Soldan ve sağdan r = 2 adet sayı
silelim.Yeni sayı 5994 olacaktır.Peki devam edelim 5994\^2 = 35.928.036
olur ve takrar r adet sayı soldan ve sağdan silelim.Yeni sayı 9280
olur.Devam etmek istersek bu böyle devam edecektir.Sayılar soldan
parçalanarak 2 basamaklı rastgele sayılar elde edilir.Örneğin 2
basamaklı rastgele sayılar için kümemiz {81,35} olurken üç basamaklı
sayılar için {815,359} olur.

Görüldüğü gibi çok pratik olmayan bir yöntemdim ve bazı soruları
vardır.Örneğin başlangıçta alınan 2500 sayısı için 50\^2 = 2500 elde
edilir ve bir çıkmaza girilir**.**

**<span style="color: #ff6600;"> **2**\#</span>** <span
style="color: #ff6600;">**Lineer Benzerlik Algoritması**</span>

Daha önce C kullanmış olanlar bu algoritma onlara tanıdık gelecektir ve
ilk kez rastgele sayı oluşturan kişilerin genelde bunlar aynı sayılar
şeklinde devam ediyor , bu problem nedir dedikleri olmuştur(En azından
ben bu soruyu sormuştum).

[D.H Lehmer](https://en.wikipedia.org/wiki/Derrick_Henry_Lehmer)
tarafından geliştirilmiş rastgele sayı üretme algoritmasıdır.İlk olarak
s,c,b değişkenleri belirlenir.

> 's' başlangıç noktası  
>  'c' çarpım için  
>  'b' artış için  
>  'm' ise mod işlemi için belirlenen bir değerdir

Algoritma şu şekilde işler.İlk olarak başlangıç noktası(s) çarpım için
belirlenmiş olan(c) ile çarpılır ve 'b' ile toplanır ve sonuç mod
işlemine alınır(m),ilk rastgele sayı üretilir.Bu işlem üretilen rastgele
sayının tekrar 'c' ile çarpılıp 'b' ile toplanıp 'm' ile modunu alınması
şeklinde devam eder.Örnek;

> s = 10  
>  c = 2  
>  b = 1  
>  m = 5 (Dikkat maksimum sayı 4 olabilir anlamına gelir)

> 1.Adım:  
>  (s\*c + b ) % m yani (10 \* 2 + 1) % 5 = 1 olacaktır ve yeni s = 1  
>  2.Adım:  
>  (1 \* 2 + 1) % 5 = 3 olacaktır ve yeni s = 3  
>  3.Adım:  
>  (3 \* 2 + 1) % 5 = 2 olacaktır ve yeni s = 2

gibi işlemler devam edecektir.3 adımda 3 adet sayı ürettik bunlar
{1,3,2}'dir.Gerçek sayı üretme işlemlerinde bu değerler bu kadar küçük
seçilmezler.[D.E Knuth](https://tr.wikipedia.org/wiki/Donald_Knuth) ve
[H.W. Lewis](https://en.wikipedia.org/wiki/Harold_Lewis)tarafından
önerilen değerler ise;

> c = 1664525  
>  b = 1013904226  
>  m = 2 \^ 32

Detaylı bilgi için
[bakın.](http://portals.omg.org/hpec/files/specs/vsipl/random.xhtml)

Şimdi gelelim şu C'de yaşanılan probleme.Bilindiği gibi
[rand()](http://www.cplusplus.com/reference/cstdlib/rand/) fonksiyonu
geriye bir rastgele sayı döndürür fakat geri döndürdüğü sayılar belli
bir süre sonra tekrar ettiği görülür , hatırlarsınız orta karaler
yönteminde de benzer bir çıkmaza giriliyordu.Yani başlangıç için
belirlenen değer zamanla değiştirilmez.Bunun için
[srand()](http://www.cplusplus.com/reference/cstdlib/srand/) fonksiyonu
kullanılır.Bu ise başlangıç değerini değiştirir.

<span style="color: #ff6600;">**3\# 147 Algoritması  
**</span>  
İsimden anlaşılacağı gibi 147 sayısı kullanılarak sayı üretilir.

> 1.Adım : 0 \< n \< 1 aralığında bir '0,abcdefg' sayısı seçilir.Burada
> g = {1,3,7,9} olmak zorundadır.  
>  2.Adım : s = n \* 147 elde edilir.  
>  3.Adım : s sayısından tam sayı kısmı çıkartılır.  
>  4.Adım : 2. adıma geri dönülür.

Bir örnek verelim.Örneğin n = 0,1234567 olsun. s = 0,1234567 \* 147 =
18,1481349 olarak bulunur ve 3. adıma göre s = 18,1481349 - 18 =
0,1481349 olarak güncellendikten sonra işlemler tekrar edilir.

<span style="color: #ff6600;">**4\# Engel Algoritması  
**</span>  
Bazen yeni bir formul ile karşılaştığımda genelde ilk tepkim bu
insanlar bu hesaplamarı bulurken bu absurd sabitler nereden geliyor diye
kendime soruyorum.Mesela 147 algoritmasında görüldüğü gibi neden 147 ?
Bu algoritmada da bir basit kullanılıyor.Bu seferki sabitimiz 'π'(pi)
ama işin ilginç yanı bu sabiti kullanmak zorunda değiliz.Sadece 1'e
yakın bir sayı olmasın yeter.

Rastgele sayı üretiminde tahmin edilebilirliğin çok düşük olması
gerektiğinden bahsetmiştik.Bu algoritmada sayılarda ki değişiklikler
belirsizdir.

Algoritma için tanımlama

> 1.Adım : 0 \<= n \<= 1 koşulunu sağlayan bir sayı seçilir.  
>  2.Adım : u = (n + π ) \^ 8 elde edilir ve u'nun tam sayı kısmı atılır
> ve n = geriye kalan sayı olur.  
>  3.Adım : 2.Adıma geri dönülür.

Bir örnek verelim.

> n = 0 alalım.  
>  1.Sayı için : u = (0 + π)\^8 = 9450,116981 elde edilir ve n =
> 9450,116981 - 9450 = 0,116981 olur.  
>  2.Sayı için : u = (0,116981 + π)\^8 = 12662,5682884 elde edilir ve n
> = 0,5682884 olur.

BURAK KÖSE
