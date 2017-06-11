Title: Bubble Sort - Sıralama Algoritmaları
Date: 2014-11-23 14:19
Author: Burak
Category: Algoritma
Tags: algorithm, sorting
Slug: bubble-sort

Algoritma yazılarıma sıralama algoritmaları ile başlamak istedim.İlk
olarak bubble sort ile başlamayı düşünürken bundan bir süre önce
izlediğim bir video aklıma geldi.

Bu videoda Barack Obama'nın başkan seçilmeden önce Google'da yaptığı bir
konuşma geçiyor. Google CEO'su Eric Schmidt ile yaptığı sohbette
Obama'ya bir milyon adet 32-bit integer sayıyı sıralamak için en efektif
yolun hangisi olduğu soruluyor.Obama biraz bocalayıp düşündükten sonra
Schmidt sorduğu soru için tam özür dileyerek yanıtlamayabilirsiniz
diyecekken Obama'dan kabarcık sıralamasının doğru olduğunu düşünmüyorum
cevabı gelince Schmidt şaşırarak Obama'nın bilgisayar bilimleriyle
ilgili bir geçmişinin olmadığını söylerek cevabı ona kimin söylediğini
soruyor.Tam bunun üzerine Obama

> "Bizim oradada casuslarımız var"

diyerekten ince esipirisini yapıyor.Şimdi gelelim algoritmamıza.

Kabarcık sıralaması olarak geçen bu algoritma ilk olarak yer değiştirme
algoritması olarak adlandırılmıştır.Şimdilerde kabarcık sıralaması
olarak adlandırılmasının nedeni ise dizi içerisindeki elemanların
algoritmanın her anında dizi sonuna doğru ilerlemesidir(sıralama türüne
bağlı olarak).

Algoritmanın analizi :

> En iyi durum : O(n)
>
> > -Dizi zaten sıralanmış  
> > -Yer değiştirme sayısı: 0  
> > -Karşılaştırma sayısı: n-1

> En kötü durum : O(n\^2)
>
> > -Dizi tersten sıralı  
> > -Yer değiştirme sayısı: O(n\^2)  
> > -Karşılaştırma sayısı: O(n\^2 /2)

> Ortalama durum : 0(n\^2)
>
> > -Bütün olasılıklar kontrol edilir

Dolayısı ile bu algoritmanın en kötü durumdaki çalışma zamanı
O(n\^2)'dir,algoritmanın en kötü durumda yapacağı karşılaştırma sayısı
O(n\^2 / 2)'dir ve yer karmaşıklığı O(n)'dir.

Örneğin küçükten büyüğe doğru sıralanacak bir işlem için algoritma şu
adımlarda gerçekleşir.Dizinin başından başlanılarak dizi elemanları
sırayle gezilir , gezilen dizi elemanları kendinden sonra gelecek eleman
ile sıralama türüne bağlı olarak(küçüten büyüğe gibi) kontrol edilir ve
yer değiştirilir.Bu işlem dizi sonuna kadar devam eder.

Bir örnek verelim

> 7 , 9 , 4 , 11 , 8 , 3 , 5

Bu algoritmanın adımları şu şekilde olacaktır.

> 1\. adım: 7 , 4 , 9 , 8 , 3 , 5 , 11
>
> 2\. adım: 4 , 7 , 8 , 5 , 7 , 9 , 11
>
> 3\. adım: 4 , 7 , 3 , 5 , 8 , 9 , 11
>
> 4\. adım: 4 , 3 , 5 , 7 , 8 , 9 , 11
>
> 5\. adım: 3 , 4 , 5 , 7 , 8 , 9 , 11
>
> 6\. adım: 3 , 4 , 5 , 7 , 8 , 9 , 11

gibi bir sonuç elde edilir.Yani kısaca şöyle bir işlem yapılıyor , iki
sayı alıyor bu iki sayıyı küçükten büyüğe sıralanacak şekilde yer
değitiriliyor ve bu işlem dizi bitene kadar tekrarlanıyor.Alttaki
animasyon anlamaya yardımcı olacaktır.


![Bubble-sort-example-300px](//upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif)
*(Alıntı : wikipedia)*

Kabarcık sıralaması çok da verimli olmayan bir sıralama algoritmasıdır
fakat bazı basit müdahaleler ile biraz daha efektif hale
getirilebilir.Bu konuda yazılarımı sıralama algoritmalarını temel olarak
inceledikten sonra yayınlayacağım bir yazıdan ulaşabilirsiniz.

[gist:id=e26eaa1f57a84afa5273]

Obama ve Eric Schdimit konuşması için :  

<iframe src="//www.youtube.com/embed/k4RRi_ntQc8" width="420" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>  
Bubble sort için eğlenceli bir anlatım:  

<iframe src="//www.youtube.com/embed/lyZQPjUT5B4" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>

BURAK KÖSE
