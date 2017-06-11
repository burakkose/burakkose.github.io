Title: Etkinlik paylaşım problemi - Greedy Yaklaşımı
Date: 2015-10-11 10:00
Author: Burak
Category: Algoritma
Tags: algorithm, greedy
Slug: etkinlik-secim-problemi

Etkinlik paylaşım problemi klasik bir açgözlü(greedy) yaklaşımı ile çözülen bir problemdir.Greedy kısaca parça parça çözüme ulaşılan ve her bir aşamada o anki en optimum seçeneği seçemedir.

Eğer bir problemi Greedy yaklaşımı ile çözebiliyorsak muhtemelen o problemin çözümü diğer çözüm yöntemlerine göre en optimum çözüm olacaktır fakat her durumda uygulanamaz.

Şimdi probleme gelelim, size n adet aktivite ve her aktivitenin başlangıç ve bitiş süreleri veriliyor.Sizden tek bir kişinin yapabileceği en fazla sayıda aktivite gerçekleştirmesi isteniyor.

Örneğin;

```
etkinlikler  =  0   1  2  3  4  5
             - - - - - - - - - - - -
başlangıç[]  =  {1, 3, 0, 5, 8, 5};
bitiş[]      =  {2, 4, 6, 7, 9, 9};
Cevap = {0,1,3,4}
```

İlk bitecek aktiviteleri aradan çıkarırsak sonuca ulaşabiliriz.Bunun için yapılması gerekenler;

1. Aktiviteleri bitiş zamanlarına göre sıralamalıyız
2. Sıralanmış aktivitelerden ilkini almalıyız.
3. Geriye kalan aktivitelerin başlangıç zamanı ile seçilen aktivitenin bitiş zamanı karşılaştırılmalı

Çözüme ait kod aşağıdaki gibi olur.

```
def print_max_activities(activities):
    choise,activities = activities[0],activities[1:]
    print(choise)
    for i in activities:
        if i[0] >= choise[1]:
            choise = i
            print(choise)

if __name__ == '__main__':
    #[(start,finish)]
    activities = [(1,2),(3,4),(0,6),(5,7),(8,9),(5,9)]
    activities.sort(key=lambda x : x[1]) #Bitişe göre sıralama
    print_max_activities(activities)
```
