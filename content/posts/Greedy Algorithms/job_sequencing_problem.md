Title: İş planlama problemi - Greedy Yaklaşımı
Date: 2015-10-11 12:00
Author: Burak
Category: Algoritma
Tags: algorithm, greedy
Slug: is-planlama

İş planlanması ile ilgili olan bir problem. Girdi olarak son teslim tarihine ve kazanç bilgilerine sahip olan işler veriliyor. En büyük kazancı nasıl elde edebileceğimizi bulmamız gerekiyor.

Örnek olarak ;

```
Input:
  JobID    Son Tarih     Kazanç
    a        4            20   
    b        1            10
    c        1            40  
    d        1            30
Output:
        c, a   


Input:  
   JobID     Son Tarih     Kazanç
     a         2           100
     b         1           19
     c         2           27
     d         1           25
     e         3           15
Output:
        c, a, e
```

Greedy yaklaşımı ile şu şekilde çözebiliriz.

1. Tüm işleri azalan kazanç oranlarına göre sırala
2. İlk iş başlangıcın olsun
3. Geriye kalan n-1 iş için
    1. Eğer şuanki iş zaman aşımına uğramadan sonuç listesine sığabiliyorsa elindeki işi sonuç dizisine ekle, aksi halde şuanki işi es geç.

Çözüm aşağıdaki gibi olacaktır.

```

def print_job_scheduling(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)
    result, slot = [None] * len(jobs), [False] * len(jobs)
    for job in jobs:
        j = min(len(jobs), job[1]) - 1
        while j >= 0:
            if not slot[j]:
                result[j] = job[0]
                slot[j] = True
                break
            j -= 1

    print(result, sep='\n')

if __name__ == '__main__':
    # (id,zaman aşımı,kazanç)
    jobs = [('a', 2, 100), ('b', 1, 19),
            ('c', 2, 27), ('d', 1, 25), ('e', 3, 15)]
    print_job_scheduling(jobs)
    
```

Bu algoritmanın zaman karmaşıklığı `O(n^2)` olacaktır.Union-find veri yapısı kullanılarak `O(n)` gibi bir karmaşıklıkta çözülebilir.
