Title: Selection Sort - Sıralama Algoritmaları
Date: 2014-11-25 12:00
Author: Burak
Category: Algoritma
Tags: algorithm, sorting
Slug: selection-sort

Veri kümesinin sıralı olarak tutulması için geliştirilmiş en basit
sıralama algoritmalarındandır.Türkçe'de seçmeli sıralama , seçerek
sıralama şeklinde kullanılır.Geliştirilen uygulamalarda seçmeli sıralama
kullanmak için düzgün bir analiz yapılması gerekir.Yer değiştirme
sayısındaki sabitlik dolayısı ile büyük sayıda verinin bulunduğu uzun
dosyalarda lineer zamanda sıralama yapılabilir.

Temel olarak işleyiş şu şekilde gerçekleşir.İlk olarak veri kümesinin
ilk elemanı seçilir ve geri kalan veriler ile karşılaştırılarak en küçük
eleman bulunur ve kümenin başına yazılır.Daha sonra bir sonraki
elemanlar içinde aynı işlem yapılarak dizi sıralanana kadar n. adımda
tamamlanır.Aşağıdaki animasyon ile daha iyi anlayabiliriz.

<center>
	![Selection Sort](https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif)  
    *(Alıntı : wikipedia)*
</center>

>  Karmaşıklık analizi : O(n \^ 2)  
>  Karşılaştırma sayısı : n\^2 / 2  
>  Yer değiştirme sayısı : n (sabit)

<center>
	<iframe width="560" height="315" src="//www.youtube.com/embed/Ns4TPTC8whw" frameborder="0" allowfullscreen></iframe>
</center>

[gist:id=f90e31967b4d07aa8601]

BURAK KÖSE
