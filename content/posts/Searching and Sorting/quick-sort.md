Title: Quick Sort - Sıralama Algoritmaları
Date: 2014-11-27 12:00
Author: Burak
Category: Algoritma
Tags: algorithm, sorting
Slug: quick-sort

Quick sort, Türkçe hızlı arama olan bu algoritma günümüzde en çok
tercih edilen sıralama algoritmasıdır.1960 yılında C. A. R. Hoare
tarafından ortaya atılmıştır.Bu algoritma yaklaşım bakımından "parçala
ve çözümle" ilkesine göre çalışmaktadır.

Bu yaklaşım şu şekilde açıklanabilir.Eldeki problem çok daha ufak
problemciklere ayrılır ve bütün bu problemcikler tek tek çözülerek
birleştirilir ve sonuç elde edilir.Örneğin çarpılacak iki matrisin daha
küçük matrislere ayrılarak işlem yapılıp sonucun birleştirilerek elde
edilmesi.

Şimdi gelelim algoritmanın çalışma şekline.İlk olarak sıralanacak veri
kümesini parçalayacak bir pivot seçilir.Geriye kalan elemanlar pivotun
sağına ve soluna yerleştirilir.Bu yerleştirme seçilen pivotun solunda
kalan elemanlar pivottan küçükler , sağında kalanlar ise pivottan büyük
elemanlar olacaktır , eşit olanların ise ne tarafa yerleştiklerinin bir
önemi yoktur.Bu işlem ardından yukarıdaki işlemler tüm parçalanmış
diziler içinde tekrarlanır ve sonuç olarak sıralanmış dizi elde edilir.

Bu algoritmanın ortalama çalışma zamanının karmaşıklığı O(nlogn)
'dir.Sebebi veri kümesi her seferinde ikiye bölünerek devam eder(logn)
ve n adet eleman için sıralama yapılır.Algoritma en kötü durumda O(n\^2)
ile çalışır.En kötü durum oluşması için seçilen pivot , veri kümesinin
en küçük ya da en büyük büyük elemanı olması ile oluşur.

Aşağıdaki animasyon

<center>
	![Quick Sort](https://upload.wikimedia.org/wikipedia/commons/9/9c/Quicksort-example.gif)  
	*(Alıntı : wikipedia)*
	ve video sonrası anlamak daha kolay olacaktır.
	<iframe src="//www.youtube.com/embed/ywWBy6J5gz8" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>
</center>

[gist:id=b53e632cedeb46078f7d]

#### <span style="color: #ff9900;">**\#Geliştirilmiş Hızlı Sıralama(Enhanced Quick Sort)**</span> {style="text-align: justify;"}

Quick sort algoritmasında en kötü durum sonucunun ürettiği performans
düşüklüğünü göz önüne alınarak algoritmada değişikliğe
gidilmiştir.Bununla birlikte veri kümesinin 10'dan az elemana sahip
olduğu zamanlarda hızlı sıralama algoritmasının yerine [direkt
yerleştirme sıralama](http://blog.koseburak.net/insertion-sort/)sının
uygulanması daha efektif olacaktır.

En kötü durumun oluşmasının nedeni pivot seçimidir.Pivot seçimi normal
şartlar altında dizinin orta noktası seçilerek gerçekleşiyordu.Bunun
yerine bu yaklaşımda pivot elemanı dizinin ortasındaki,başındaki ve
sonundaki elemanlar karşılaştırılarak seçilmesi şeklinde
düzenlenmiştir(bknz : median of three).Bu değişiklik hızlı sıralama
algoritmasının karmaşıklığını değiştirmeyecek fakat gerçekleştirilen
karşılaştırma sayısında azalma olacaktır.

[gist:id=6db3ad4e3893dc530408]

#### <span style="color: #ff9900;">**\#Yinelemeli Olmayan Hızlı Sıralama(Non-Recursive Quick Sort)  
**</span> {style="text-align: justify;"}

Özyinelemeli(recursion) yaklaşımdan zorunda kalmadığım müddetçe uzak
kalmaya çalışıyorum.Bazı zamanlar oldukça yorucu olabiliyor.Bu
algoritmayıda olumsuz yönde etkileyen bir etken özyinelemeli yaklaşım.

Stack kullanarak bu soruna bir alternatif yaklaşım üretebiliriz.Hızlı
sıralama algoritmasında fark edildiği gibi aslında çok önemli iki
parametre alıyor.Bunlar alt veri kümenin başlangıç ve bitiş
indisleri.Bunları ayrı bir veri yapısında tutarak şöyle bir çözüm
üretebiliriz.

[gist:id=7faa4e70c7c672ee2694]

Yapılan değişiklikler algoritmanın karmaşıklığını etkilemediği için
çalışma zamanı karmaşıklığı değişmemektedir.

BURAK KÖSE
