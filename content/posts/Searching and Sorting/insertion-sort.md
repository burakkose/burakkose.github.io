Title:Insertion Sort - Sıralama Algoritmaları
Date: 2014-11-24 16:00
Author: Burak
Category: Algoritma
Tags: algorithm, sorting
Slug: insertion-sort

Uygulaması kolay olan bu algoritmayı büyük diziler yerine daha küçük
dizilerde kullanıldığında ve özellikle gelen veri kümesinin zaten
sıralanmış veya sıralanmış haline çok yakın olduğunda kullanılır.

Kararlı bir algoritma olmasıyla birlikle çalışma anında ek bir bellek
ihtiyacı duymayan bu algoritma Türkçe'da yerleştirmeli sıralama ,
eklemeli sıralama ve sokma sıralaması olarak adlandırılabilir.

Algoritma sıralanacak olam veri kümesinin ikinci elemanından itibaren
verileri sırayla kontrol eder ve bir önceki kayıt o anki kayıttan
büyükse(veya küçükse sıralama tipine bağlı olarak) bu iki elemanın
yerleri değiştirilir ve geriye doğru kontrollere devam edilir.Dizi
elemanı doğru yere yerleştirilene kadar bu işlemler tekrar edilir.

Günlük hayatta aslında iskambil kağıtlarını sıralarken bu algoritmayı
kullanırız.Şimdi bu algoritmayı analiz edelim.

> > En iyi durumda (best case) : O(n)
> >
> > > Dizi zaten sıralanmıştır  
> > > Karşılaştırma sayısı : n(n-1)/2
>
> > En kötü durumda(worst case) : O(n\^2)
> >
> > > Dizi tersten sıralı  
> > > Karşılaştırma sayısı : n(n-1)/2

ve bu algoritmayı aşağıdaki şekilde tanımlayabiliriz.

[gist:id=8ad4a6c60d2cc51fe8d4]

<iframe src="//www.youtube.com/embed/ROalU379l3U" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe>

#### <span style="color: #ff9900;">**\#Direkt Yerleştirmeli Sıralama (Straight Insertion Sort)**</span> {style="text-align: justify;"}

Yukarıda bu algoritmanın günlük hayatta iskambil kağıtlarını sıralamak
için kullanıldığını söylemiştik.Aslında bu çok da doğru değildir.Bir
araya ekleme işlemi vardır fakat bu ekleme işlemi hiç bir zaman tek tek
kontrol yaparak ve yer değiştirerek olmayacaktır.Bir örnek verelim.

> 2,4,1,5

ve algoritmayı ilk adım için işletelim ve 4'ü seçelim bir işlem
yapılamayacaktır çünkü bu aşamada sıralıdır.Bir sonraki adım olarak 1'i
seçelim ve geriye doğru kotrollere devam edelim.

> 1 \< 4 mü ?

evet o halde 1'i araya al.Yeni durum **"2,1,4,5"**

> 1 \< 2 mi?

evet o halde tekrar araya al.Yeni durum **"1,2,4,5"**

şeklinde algoritma işleyecektir.Oysa biz gerçekte 2 ve 4 sıralı olduğu
için direk olarak 1'i en başa ekleyeceğiz.Yani her seferinde yer
değiştirme yapmayacağız sadece kaydırma işlemi yapacağız ve direkt
olarak yerleştirme yapacağız.

Şimdi bu yaklaşım ile insertion sort'un yeniden düzenlenmiş bir
algoritması olan **Direkt Yerleştirmeli Sıralama ( Straight Insertion
Sort)** algoritmasının inceleyelim.

> En kötü durumda(worst case) : O(n\^2)
>
> > Dizi tersten sıralı  
> > Karşılaştırma sayısı : n\^2 / 2  
> > Yer değiştirme sayısı : n\^2 / 4

[gist:id=b9ee29a595a80d486622]  
Algoritmayı aşağıdaki animasyon ile daha iyi anlayabiliriz.


![Insertion Sort](https://upload.wikimedia.org/wikipedia/commons/9/9c/Insertion-sort-example.gif)  
*(Alıntı : wikipedia)*

#### **<span style="color: #ff9900;">\#İkili Yerleştirmeli Sıralama(Binary Insertion Sort)</span>**

Şimdi biraz daha derine inerek bu algoritmanın daha optimize bir hale
getirilmiş hali olan ve daha büyük veri kümelerinde diğer yerleştirmeli
sıralama algoritmalarına göre daha başarılı olan bir algoritma olan
İkili Yerleştirmeli Sıralama algoritmasını inceleyelim.

Bu algoritmada seçilen dizi verisinin kendinden önce gelen veriler
arasında nereye yerleştirileceğine karar verilirken geriye doğru ardaşık
olarak kontrol etmek yerine , elimizdeki veri kümesine bir bütün olarak
bakılarak ikili arama yapılması amaçlanmıştır.Hedef yer belirlendikten
sonra tekrar kaydırma işlemi yapılarak işlem tamamlanır.

Karmaşıklık için.

> En kötü durumda(worst case) : O(nlogn)
>
> > Dizi tersten sıralı  
> > Karşılaştırma sayısı : n(logn - nloge) (yaklaşık olarak)

[gist:id=6a568b504a36dedbc397]

BURAK KÖSE
