Title: İlk gelen işi kapar (First Come First Serve)
Date: 2014-11-24 01:05
Author: Burak
Category: Algoritma
Tags: algorithm, operating systems, scheduling
Slug: first-come-first-serve

Kısaca FCFS algoritması.İsim benzerliği ve aslında çalışma mantığı
bakımında kuyruk(queue) veri yapısına çok benzer(FIFO).Bilgisayar
alanında özellikle işletim sistemlerinde bir çok alanda kullanılan bir
algoritmadır.Bu algoritmik yaklaşımda bir sıraya ilk girenin işi ilk
halledilmektedir.

<!--more-->

Bu şu şekilde açıklanabilir.Mahallenizde bir berber bulunmaktadır fakat
ne yazık ki berber doludur ve herkes sırasını beklemektedir.Sizde bir
sıra alırsınız ve aldığınız sırayı beklemek zorundasınızdır.Sizi önemli
kılan hiç bir (para,pul,şöhret,tanıdık...) sıranızı beklemekten
alıkoyamaz ve size sıra gelebilmesi için berberin sizden önce gelen tüm
müşteriler ile ilgilenmiş olması gerekmektedir .İşte bu algoritmada buna
benzer şekilde çalışır.

Şimdi bu algoritmayı CPU Scheduling yani işlemci zamanlama tarafından
örnekleyerek açıklayalım.Bu yaklaşımda işlemciye gelen işlerin
işlenmesi, işlemlerin geliş sırasına göre belirlenmektedir.

| Process | Çalışma Zamanı |
|:-------:|:--------------:|
|    A    |       23       |
|    B    |        6       |
|    C    |        2       |

ve sonuç olarak aşağıdaki gibi bir tablo göreceğiz.

| Başlangıç Zamanı | Process | Çalışma Zamanı | Kalan Zaman |
|:----------------:|:-------:|:--------------:|:-----------:|
|         0        |    A    |       23       |      0      |
|        23        |    B    |        6       |      0      |
|        29        |    C    |        2       |      0      |

Bu algoritma sonunda işlemlerin bekleme süreleri

| Process | Bekleme Süresi |
|:-------:|:--------------:|
|    A    |        0       |
|    B    |       23       |
|    C    |       29       |

Dolayısı ile ortalama bekleme süresi = (0+23+29) / 3 = 17.3

First come first serve (FCFS) algoritması nonpreemptive(kesintisiz) bir
zamanlama algoritmasıdır.Yani sıraya giren işlemlerden biri bitirilmeden
diğer işleme geçilmemektedir.

Not : Eğer yukarıdaki processleri geliş sürelerine göre değilde çalışma
zamanlarına göre sıralayarak işleme alsaydık ortalama bekleme süresinin
daha az olduğunu görürdük.(bknz :SJF algoritması)

BURAK KÖSE
