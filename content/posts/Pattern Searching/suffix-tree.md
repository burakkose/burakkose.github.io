Title: Suffix Tree - String Algoritmaları
Date: 2014-12-04 00:08
Author: Burak
Category: Algoritma
Tags: algorithm, string, searching, bioinformatic
Slug: suffix-tree

Biyoinformatik'de adı sıkça geçen algoritmalardan olan suffix tree veri
yapısı bir dizgi model(pattern) eşleştirme algoritmasıdır.Örneğin
elinizde uzun bir dizgi olsun ve siz bu dizgi içinde alt dizgiler aramak
ve hatta bu dizgilerden kaç adet bulunduğunu öğrenmek istiyorsunuz.İşte
bu veri yapısı bu işlemleri kolaylaştırmak ile birlikte gayet hızlı
işlem yapmamıza olanak sağlıyor.

Bu tip bir yöntem kullanmadan ilkel olarak çözüm olarak şunu
yapabilirdik.Ana dizgi içerisinde lineer olarak sırayla karşılaştırma
yapa yapa devam ederek sonuca ulaşabilirdik.Bu bir yöntemdir fakat dizgi
boyutları arttıkça bu işlem çok maliyetli olmaktadır.

Suffix tree incelemesi yapmadan önce suffix nedir bundan
bahsedelim.Suffix Türkçe'de son ek olarak geçer ve bir dizginin son
ekleri şu şekilde bulunur.Örnek:

> String = burak

sonekler

> burak,urak,rak,ak,k

olacaktır.Görüldüğü gibi n uzunluğunda bir dizgi n adet suffix
sahibidir.

Suffix tree oluşturmak için önce ihtiyacımız olan suffixleri bulmamız
gerekmektedir.Yukarıdaki örnekteki gibi suffixler elde edildikten sonra
bunlar uzunluklarına göre sıralanmalıdır.Örneğin

> String = xabxac

için sonekler

> xabxac,abxac,bxac,xac,ac,c

olarak elde edilikten sonra sırası ile 1,2,3,4,5,6 numaraları
verilir.Ağaç şu şekilde oluşturulur.Bir başlangıç noktası vardır ve
buradan dallanmalar yapılmaktadır.Önce 1 numara dallanır daha sonra
gelen 2 numaraya ait dizgi ile ortak başlangıç noktaları varsa bu
noktadan itibaren dallanma yapılır eğer yoksa yeni bir dallanma
yapılır.Şimdi adım adım ağacımızı oluşturalım.

**<span style="color: #ff9900;">\#1.Adım</span>**  
İlk dallanmamızı 1 numaralı suffix ile yapıyoruz.  

![1](/images/suffix_tree/1.png)  
<span style="color: #ff9900;">**\#2.Adım**</span>  
2 numaralı suffix olan "abxac"' için inceleme yapıldığında şuana kadar
başlangıç noktasından itibaren "a" ile başlayan bir dallanma
olmadığından yeni bir dallanma yapılır.  

![2](/images/suffix_tree/2.png)  
<span style="color: #ff9900;"> **\#3.Adım**</span>  
3 numaralı suffix "bxac"' için inceleme yapıldığında "b" ile başlayan
bir dallanma olmadığından tekrar başlangıç noktamızdan yeni bir dallanma
yapılır.  

![3](/images/suffix_tree/3.png)  
<span style="color: #ff9900;"> **\#4.Adım**</span>  
4 numaralı suffix "xac"' için inceleme yapıldığında bu noktada işin
şekli değişmektedir.Ağaca baktığımızda başlangıç noktasından itibaren
bir "x" ile başlangıç vardır.Hatta bir adım daha arama yaptığımızda
sadece "x" ile değil devam edildiğinde "xa" ile bir başlangıç olan
dallanma vardır(1 numaralı suffix).Dolayısı ile kesişme noktasından bir
dallanma yapılır.  

![4](/images/suffix_tree/4.png)  
<span style="color: #ff9900;"> **\#5.Adım**</span>  
5 numaralı suffix "ac" için inceleme yapabilmek için tekrar root
noktasından taramaya başlıyoruz ve ilk olarak "a" başlangıcı
arıyoruz.Görüldüğü gibi en iyi kesişim 2 numaralı suffixtedir.Dolayısı
ile bir kesişim noktası yapıp yeni bir dallanma yaratıyoruz.  

![5](/images/suffix_tree/5.png)  
<span style="color: #ff9900;"> **\#6.Adım**</span>  
Ve son olarak sırada 6 numaralı suffix olan "c" için incelemede.Tek
başına bir dallanma yapması gerektiği görülüyor.  

![6](/images/suffix_tree/6.png)

Ağaç oluşturulmuştur.Şimdi bir arama yapalım,örneğin "xa"  , bu dizgi
içinde geçiyor mu ve geçiyorsa kaç kere geçiyor sorusuna cevap arayalım.

Ağaca bakmaya root noktasından başlayalım ve "xa" arayalım.Hemen root
noktasının altında "xa" başlangıcı ile karşılaşıldı.Dolayısı ile "xa"
eşlemesi sağlandı ama kaç tane "xa" olduğunu nereden anlayacağız?Kaç
tane "xa" olduğunu bulunan noktanın altında kaç tane dallanma varsa o
kadar "xa" vardır diyeceğiz.Baktığımızda iki adet dallanma olduğu
görülmektedir.  

![new6](/images/suffix_tree/new6.png)

**Peki "bxa" var mıdır ?**  
Ağaçta aramaya tekrar root noktasından başlanır ve sırayla "bxa"
aranır.  

![new6.1png](/images/suffix_tree/new6.1png.png)  
evet "bxa" vardır ve 1 kere bulunur.

**Peki "xb" var mı?**  
Hayır "xb" yoktur.Sebebi ise root noktasından aramaya başlandığında
"xb" eşlemesi ile başlayan bir dallanma bulunamamıştır.

<span style="color: #ff9900;">**Her dizgi bir suffix tree sahibi
midir?**</span>

Her dizgi bir suffix tree sahibi değildir.Eğer bir dizginin suffixleri
prefixlerine eşitse bir suffix ağacı yoktur.Mesela "cdbcd" için inceleme
yapalım.

> Suffixlerin : cdbcd,dbcd,bcd,**cd**,d olduğunu biliyoruz.

ve

> Prefixleri : c,**cd**,cdb,cdbc,cdbcd şeklindedir.

Dizginin kendisi dikkate alınmadan incelendiğinde "cd" değerlerinin
ortak olduğu görülmektedir.Dolayısı ile "cdbcd" için bir suffix tree
çizilemez.Peki bu sorunu nasıl çözebiliriz ? Çok basit sadece "cdbcd"
stringinin sonuda bir "\$" ekleyerek.Eğer "cdbcd\$" için inceleme
yaparsanız bir sorun olmadığını göreceksiniz.

BURAK KÖSE
