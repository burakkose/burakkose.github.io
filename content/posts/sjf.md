Title: İlk iş kısa süreliler (Shortest Job First)
Date: 2014-11-26 12:00
Author: Burak
Category: Algoritma
Tags: algorithm, operating systems, scheduling
Slug: sjf

Bir önceki yazımda cpu zamanlama algoritmalarından olan fcfs
algoritmasından bahsetmiştim.Asıl ismi "shortest next CPU burst
algorithm" olarak geçen ve yine bir cpu zamanlama algoritması olan
Shortest Job First(SJF) yani en kısa iş ilk algoritmasını inceleyelim.

Bu algoritmada belli bir sırada bekleyen işlerden önce kısa olanların
işlenmesi amaçlanmıştır.Eğer iki işten aynı çalışma süresi içeren işler
varsa geliş sıralarına göre işlem görürler.Bu algoritmanın duruma göre
hem nonpreemptive(kesintisiz) hemde preemptive(kesintili) olarak
düzenlenebilir.

Temel olarak eldeki işlerin en kısasını yaparak zamandan kazanmaya
çalışan bir algoritma olsada en büyük dezavantajı bir çıkmaz
yaratmasıdır.Bu çıkmazı şöyle bir örnek ile açıklayabiliriz.

Bir berbere gidiyorsunuz ve berberde sıra var.Dolayısı ile sıra almanız
gerekiyor ve sıraya giriyorsunuz .Bu berberde işi kısa sürecek olan
kişilere hep öncelik tanınıyor.Dolayısı ile siz,işi sizden uzun
süreceklerin önüne geçiyorsunuz ve sıra size geliyor .İşiniz
hallediliyor tam siz berberden çıkarken yine işi kısa sürecek biri
geliyor ve sizin önünüze geçtiğiniz kişinin sırasını tekrar alıyor ve
bunun çalışma saatleri bitene kadar böyle devam ettiğini
düşünün.Dolayısı ile işi uzun ama çok önce gelmiş kişiler gün sonunda
işini halledememiş bir şekilde beklemeye devam ediyorlar.

Böyle bir kısır döngüye girme ihtimali bulunmaktadır.Şimdi
algoritmamızı nonpreemptive bir durum için şu örnek ile açıklamaya devam
edelim.

| Process | Çalışma Zamanı |
|:-------:|:--------------:|
|    A    |        8       |
|    B    |       10       |
|    C    |        9       |
|    D    |        5       |

ve sonuç olarak aşağıdaki gibi bir çalışma zamanı tablosu göreceğiz.

| Başlangıç Zamanı | Process | Çalışma Zamanı | Kalan Zaman |
|:----------------:|:-------:|:--------------:|:-----------:|
|         0        |    D    |        5       |      0      |
|         5        |    A    |        8       |      0      |
|        13        |    C    |        9       |      0      |
|        22        |    B    |       10       |      0      |


Bu işlemler sonunda işlemlerin bekleme süreleri

| Process | Çalışma Zamanı |
|:-------:|:--------------:|
|    A    |        5       |
|    B    |       22       |
|    C    |       13       |
|    D    |        0       |

Yukarıdaki örnekde giren işlem kesintisiz bir şekilde
gerçekleşmiştir.Şimdi bu örneğimizde ise algoritmamızı preemptive bir
durum için inceleyelim.

| Process | Geliş Zamanı | Çalışma Zamanı |
|:-------:|:------------:|:--------------:|
|    A    |       0      |       10       |
|    B    |       1      |        6       |
|    C    |       2      |       11       |
|    D    |       3      |        7       |

ve sonuç olarak aşağıdaki gibi bir çalışma zamanı tablosu göreceğiz.

| Başlangıç Zamanı | Process | Çalışma Zamanı | Kalan Zaman |
|:----------------:|:-------:|:--------------:|:-----------:|
|         0        |    A    |        1       |      9      |
|         1        |    B    |        6       |      0      |
|         7        |    D    |        7       |      0      |
|        14        |    A    |        9       |      0      |
|        23        |    C    |       11       |      0      |

BURAK KÖSE
