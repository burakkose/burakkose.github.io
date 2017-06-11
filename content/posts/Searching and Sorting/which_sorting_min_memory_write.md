Title: Hangi sıralama algoritması belleğe en az sayıda yazma yapar?
Date: 2015-10-05 18:00
Author: Burak
Category: Algoritma
Tags: algorithm, sorting
Slug: which-sorting-min-memory

Hafızaya yazma işlemini azaltmak, büyük veri kümeeleri üzerinde uğraşmanın maliyetli olduğu EEPROMs ve ya flash gibi platformlar için kazançlıdır.

Sıralama algoritmaları arasında `Selection Sort` agoritmasının en az sayıda yazma işlemi yaptığını(`O(n)`) biliyoruz. Fakat `Cycle Sort` neredeyse her zaman `Selection Sort` algoritmasına göre daha az sayıda yazma işlemi yapar. Eğer değer doğru noktada ise, o değer için hiç yazma işlemi yapılmaz ve eğer değer doğru noktada değilse bir kez yazma işlemi yapılarak doğru noktaya getirilir.
