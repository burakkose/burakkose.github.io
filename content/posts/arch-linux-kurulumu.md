Title: Arch Linux Nasıl Kurulur
Date: 2014-11-12 18:45
Author: Burak
Category: Linux
Tags: archlinux
Slug: arch-linux-kurulumu

*Bu yazı Arch Linux 2014 Ağustos kalıbı dikkate alınarak
hazırlanmıştır.*

**Neden Arch , Nedir Bu ?**

Arch Linux "sürekli güncel"(bkz: "rolling release") paket mantığı
üzerine kurulu, belirli bir düzeyde GNU/Linux bilgisi olan kullanıcıları
hedef alan(tamamen göreceli kimileri yeni başlayanlar için ideal olduğu
görüşünde) bağımsız bir dağıtımdır.Arch hızlı, hafif, esnek ve basittir.

Arch Linux temel sistemi olabildiğince ufaktır.Çeşitli
işlemlerin yapılması kullanıcıya bırakılmıştır.Kullanıcı istediği
doğrultuda zengin depo yardımıyla istediği şekilde kendine uygun şekle
getirebilir.Kısacası kendi evinizi istediğiniz şekilde
biçimlendiriyorsunuz.

**Kurulum**

Kurulum aşaması metin tabanlı gerçekleşmektedir.Dolayısı ile komutlar
ile kurulum yapılmaktadır.Arch Linux'un dökümantasyonu çok
gelişmiştir.Sadece kurulum aşamasında değil çoğu zaman karşılaştığınız
sorunların çok büyük bir bölümüne buradan çözüm bulabilirsiniz.

<https://wiki.archlinux.org/>  
<http://archtr.org/wiki/index.php/Ana_Sayfa>

Donanımım

>  CPU: 64 bit Intel  
>  Hard Drive: 500GB HDD  
>  RAM: 8GB  
>  Intel Graphic Card  
>  Nvidia GTX 660M  
>  BIOS

**Kuruluma Hazırlık Aşaması**

Arch Linux'un elde edilmesi için bu adres üzerinden kalıba
ulaşabilirsiniz.

<https://www.archlinux.org/download/>

CD veya USB üzerinden kurulumu gerçekleştirebilirsiniz.İndirdiğiniz
kalıbı bu ortamlara yazarak bir sonraki aşamaya geçelim ve kurulum
yapacağınız birimi boot ettiğimizde karşılaşacağımız ekran aşağıdaki
gibi olacaktır.

![Karşılaşılan Ekran](/images/arch_linux/arch-linux-install-001.jpg)]

### **Aşama\#1 [Arch Kurulumu](https://wiki.archlinux.org/index.php/Beginners%27_Guide#Establish_an_internet_connection)** {style="text-align: justify;"}

Kurulum aşamsında internet bağlantımız olması gerekmektedir.Dolayısı ile
benim önerim ethernet bağlantısı sağlamanız yönünde.Eğer kurulum
sırasında kablosuz bağlantı kullanacaksanız tebrikler ilk kez arch
wiki'yi kullanacaksınız demektir.

İlk olarak türkçe klavye kullanmak için

`# loadkeys trq`

komutunu veriniz.Bağlantı kontrolunuz için

`# ping -c 3 www.google.com`

Komutunun ekran çıksını size yol gösterecektir.Eğer her şey yolunda ise
bir sonraki adıma geçebilirsiniz.

### **Aşama\#2 [Disk Bölümleme](https://wiki.archlinux.org/index.php/Beginners%27_Guide#Prepare_the_storage_drive)** {style="text-align: justify;"}

Bu aşamada çok dikkatli olmasılısınz.Yanlış bir adım sizi veri kaybına
ve belkide delirmenize yol açabilir.Bu aşamayı elle gerçekleyeceğiniz
için önceden kendinize göre plan yaparak bölümleme işlemine geçiniz.

Bölümlendirme aşamasında temel olarak genellikle dört bölüm
yaratılır.Bunlar boot , / ( Kök dizini) , home ve swap alanlarıdır.Ben
şahsen tek bölüm yaratıp o şekilde kullanmayı tercih ediyorum sizde
yedekleme için kullandığınız ayrı bir disk bölümü varsa home dizini
oluşturmanıza gerek yoktur.Swap alanı ise RAM'e bağlıdır.Eğer 4GB ve
üstü RAM kullanıyorsanız bu alanada ihtiyacınız yoktur.

-   /boot için = 100 MB
-   Swap ( Takas alanı) için = 2 GB
-   / kök için = 20-25 GB
-   home için ise kişisel olarak oluşturmak istediğiniz miktarı
    verebilirsiniz

İlk olarak lsblk komutunu çalıştırarak daha önceden olan
bölümlemelerinizi kontrol edin ve bu aşamadan sonra tek bir disk
kullandığınızı varsayarak

`# cfdisk dev/sda`

komutu sonrası görüntünüz şu şekilde olacaktır.

![Disk Bölümleme](/images/arch_linux/Selection_024.png)

Temel olarak bölüm ayırırken boş alan seçiliyken "New - \> Alan
boyutu - \> Tamam" şeklinde bir yol izleyeceğiz.Şimdi alanları ayırmaya
başlayalım ve ilk olarak boot alanı ayıralım.

1.  /boot için 100 MB bölüm oluşturmak için New seçin ve alan oluştuktan
    sonra alt tarafdaki özelliklerden Bootable özelliği verdikten sonra
    Type kısmına 83 yazarak bir sonraki alana geçin.
2.  Swap (takas) alanı için bölüm oluşturulmalıdır. Ben 2GB ayırdım.
    Sizde kendinize göre ayırabilirsiniz. Type kısmına 82 yazdıktan
    sonra bir sonraki alana geçin.
3.  Kök ( / ) için bölüm oluşturulacaktır.Kök dizini için 20-25 GB kadar
    alan ayırın. Type kısmına 83 yazın.
4.  Aynı yol ile isteğiniz doğrultusunda home için dilediğiniz kadar
    alan ayırdıktan sonra alt tarafdan Write kullanarak oluşturduğunuz
    bölümleri yazın ve bir sonraki aşama için Quit ile çıkın.

`# lsblk`

komutu ile kontrol edelim.

>  sda1 – BIOS Boot  
>  sda2 – root  
>  sda3 – swap  
>  sda4 – home

tabiki sizde durum farklı olabilir.Bu aşamadan sonrada sizdeki duruma
göre şekil veriniz.

### **Aşama\#3 [Dosya Sistemlerini Oluşturma](https://wiki.archlinux.org/index.php/Beginners%27_Guide#Create_filesystems)** {style="text-align: justify;"}

Şimdi sırada oluşturduğumuz parçalara şekil vermeye geldi.Linux dosya
sistemi olarak ext4 kullanır.İlk olarak aşağıdaki komutları root ve home
dizinleri için yürütün.Bendeki şekli ile şu şekilde olacaktır.

`# mkfs.ext4 /dev/sda2`  
`# mkfs.ext4 /dev/sda4`

Şimdi swap bölümümüz için bendeki şekli ile

`# mkswap /dev/sda3`  
`# swapon /dev/sda3`

ve bu aşamanın son kısmı olarak son kez kontrol edelim bir sorun yoksa
diğer aşamaya geçebiliriz

`# lsblk /dev/sda`

**[Temel Sistem
Kurulumu](https://wiki.archlinux.org/index.php/Beginners%27_Guide#Install_the_base_system)**

Her şey yerli yerinde ise sırada temel sistem kurulumumuz
bulunmaktadır.Öncelikle kök dizinimizi bağlayalım.

`# mount /dev/sda2 /mnt`

ve "home" isimli bir klasör yaratalım.Evet home için oluşturduğumuz
parçayıda buraya bağlayacağız.

`# mkdir /mnt/home`  
`# mount /dev/sda4 /mnt/home`

### **Aşama\#4 Temel paketlerin Kurulumu** {style="text-align: justify;"}

Sırada sistemimizin temelini kurma aşamamız var.Bu aşamada iskelet
oluşacaktır.

`# pacstrap -i /mnt base base-devel`

### **Aşama\#5 [fstab Güncelleme](https://wiki.archlinux.org/index.php/Beginners%27_Guide#Generate_an_fstab)** {style="text-align: justify;"}

Tüm temel paketlerin kurulumu başarı ile gerçekleştiyse fstab'a tüm
değişiklikleri bildirebiliriz.

`# genfstab -U -p /mnt >> /mnt/etc/fstab`  
(Not:Kesinlikle bir problem ile karşılaşmamış olmamız gerekmektedir)

Linux'da her zaman yap kontrol et mekanizması işlemektedir.Bizde
yaptığımız değişikliği kontrol edelim.

`# nano /mnt/etc/fstab`

Bir problem gözükmüyorsa CTRL + X ile çıkış yapabiliriz.

Bu aşamalarda bir problem ile karşılaşmadıysak root ve home dizinlerinin
başarı ile bağlanmış olduğunu görebiliriz.Kök dizinimizi değiştirerek
diskte kurduğumuz temel sisteme bürünelim.

`# arch-chroot /mnt ve bin/bash`

### **Aşama\#6 [Dil ve Bölge ayarları](https://wiki.archlinux.org/index.php/Beginners%27_Guide#Chroot_and_configure_the_base_system)** {style="text-align: justify;"}

Ayarlarımız için sırası ile

`#nano /etc/locale.conf `  
açılan dosyaya

> LANG=tr\_TR.UTF-8

yazıp CTRL + O ile kayıt edip CTRL + X ile çıkalım.

`# nano /etc/vconsole.conf`  
açılan dosyaya

> KEYMAP=trq  
>  FONT=iso09,16

yazarak aynı şekilde kaydedip çıkalım.

`# nano /etc/timezone`

> Europe/Istabul

yazıp aynı şekilde kayıt edip çıkalım ve yaptığımız dil değişikliğini
yazmak için

`# locale-gen`

Hostname değiştirmek için

`# echo ... > /etc/hostname`  
(Not : ... olan yere dilediğinizi yazınız)

### **Aşama\#7 Depo Ayarları** {style="text-align: justify;"}

Sırada depomuzu ayarlamaya geldik."pacman.conf" dosyamızı açalım

`# nano /etc/pacman.conf`

Eğer 64 bit sistem kullanıyorsak

> [multilib]  
>  Include = /etc/pacman.d/mirrorlist

bu kısmı aktif etmemiz gerkeiyor.Başındaki \# işaretini kaldırmanız
yeterlidir.Daha sonra CTRL + O ile kayıt edip CTRL+X ile çıkalım.

`# pacman -Sy`  
ile depoyu güncelleyelim.

### **Aşama\#8 [Kullanıcı işlemleri](https://wiki.archlinux.org/index.php/Users_and_Groups#User_management)** {style="text-align: justify;"}

Kullanıcı işlemlerine geçmeden önce bir root şifresi atayalım.Bunu
kesinlikle yapmalısınız.Linux kullanırken root ile işlem yapmamaya
dikkat edin.Dolayısı ile root kullanıcısından başka bir sistemi
kullanacağınız bir kullanıcı oluşturacağız fakat ilk olarak root
şifresi...

`# passwd`

komutunu yürüttükten sonra root kullanıcısına şifre atayınız.Tamamdır
şimdi sırada kullanıcı oluşturma var.

`# useradd -m -g users -G wheel,storage,power -s /bin/bash ...`  
(Not: ... yerine kullanıcı adınızı giriniz)

ve daha sonra

`# passwd ...`  
(Not: ... yerinde yukarıda oluşturduğunuz kullanıcı adı olacak)

ile bu kullanıcıya bir şifre atamalıyız.Sırada sudo kurulumu var.Bu bize
root olmadan sistem üzerinde işlemler yapmamıza olanak sağlayacak

`# pacman -S sudo`

daha sonra kişisel önerim olarak

`# pacman -S bash-completion`

kurulumu yapınız.Adındanda anlaşılacağı gibi otomatik tamamlamalarda
yardımcı olur.

### **Aşama\#9 Linux çekirdeğini derleme** {style="text-align: justify;"}

Bu aşamada kernel konfigirasyonunu tamamlamak ve yazmak için aşağıdaki
komutu yürütün.

`#mkinitcpio -p linux `

### **Aşama\#10 [Boot yükleyicisi](https://wiki.archlinux.org/index.php/Boot_Loaders)** {style="text-align: justify;"}

Bu aşamada grub kurulumu yapmalıyız.

`# pacman -S grub # grub-install --recheck /dev/sda`

grub kurulumumuz tamamdır eğer sistemde birden fazla işletim sistemi
yüklüyse diğerlerinin algılanması için

`#pacman -S os-prober`

komutunu yürütelim.Şimdi grubu güncelleyelim.

`# grub-mkconfig -o /boot/grub/grub.cfg`

ve sistem açılışında bağlantı alabilmemiz için

`# systemctl enable dhcpcd.service`  
`# systemctl start dhcpcd.service`

sonrasında

`# exit`  
`# umount -R /mnt`  
`# reboot`

komutlarını yürüttükten sonra sistem yeniden başlayacaktır.(Not: Yükleme
yaptığınız birimi(CD,USB...) çıkartınız.

### **Aşama\#11 Boot sonrası** {style="text-align: justify;"}

Bir sorun yoksa karşınızda Arch Linux sizi selamlamalıdır.Basit kurulum
bitmiş olup kurulum sonrası yapılandırma aşamasına geçmiş
bulunmaktayız.Bundan sonraki yapılandırmalar size kalmış olsada basit
olarak temel bir yapılandırma olarak şunları yapabilirsiniz.Unutmayın
archwiki en yakın dostunuz.

**X server Kurulumu**  
` # pacman -S xorg-server xorg-server-utils xorg-xinit`

**Mesa Kurulumu**

`# pacman -S mesa`

Şimdi sırada ekran kartı kurulumu bulunmaktadır.Bu aşama genelde
kullanıcıların başına bela açan bir aşamadır(Bende dahil).Eğer
sisteminizde optimus teklonojili bir ekran kartınız varsa yani çift
ekran kartlıysanız sizi burada hiç oyalamadan Arch Linux Wiki sayfasına
yönlendireceğim.Yapmanız gerekenler orada harika bir şekilde anlatılmış
olup tüm adımları dikkatlice adım adım izlemelisiniz.

<http://archtr.org/wiki/index.php?title=Bumblebee>  
<https://wiki.archlinux.org/index.php/NVIDIA_Optimus>  
<https://wiki.archlinux.org/index.php/bumblebee>

Eğer normal ekran kartı kullanıcısıysanız bile bu aşamada Arch Wiki'den
yardım alabilirsiniz.Kendinize uygun seçeneği kurun.Ben şu şekilde devam
ediyorum.

`# pacman -S nvidia`

`# pacman -S xf86-video-intel`

`# pacman -S xf86-video-ati`

![graphicsdoc.jpg](/images/arch_linux/graphicsdoc.jpg)

Eğer laptop kullanıcısıysanız

`# pacman -S xf86-input-synaptics`

daha sonrasında temel x server bileşenleri için

`# pacman -S xorg-twm xorg-xclock xterm`

ve test etmek için sistemi yeniden başlatıp

`#startx`

Her şey yolunda ise devam edebilirsiniz lakin değilse muhtemelen ekran
kartı kısmında bir yanlışlık yaptınız demektir.Arch wiki'den destek
alabilirsiniz.

**Ses sürücüsü için**

`# pacman -S alsa-lib alsa-utils`

**Dbus Kurulumu**

`# pacman -S dbus`

**Gamin Kurulumu**

`# pacman -S gamin`

### **Aşama\#12 Masaüstü Kurulumu** {style="text-align: justify;"}

**Kde Masaüstü Kurulumu:**

Uçbirimden devam ediyoruz.

`# pacman -S kde kde-l10n-tr`

komutunu uygulayın

**Gnome Masaüstü Kurulumu:**

`# pacman -S gnome`

Yükleme bittikten sonra tekrardan

`# pacman -S gnome-extra`  
`# pacman -S gnome-tweak-tool`

**Cinnamon Kurulumu**

`# pacman -S cinnamon`

komutunu uygulayıp soruları (Y) ile onaylayın.Eğer yukarıdaki örnekler
dışında kurmak istediğiniz bir masaüstü varsa siz istediğinizi
kurabilirisiniz.

Açılışta aktif etmek için aşağıdakilerden hangisi size uygunsa onu
yürütün.

`# systemctl enable gdm.service # systemctl enable kdm.service # systemctl enable lxdm.service # systemctl enable slim.service # systemctl enable xdm.service`

**Firefox** için

`#pacman -S firefox`

### **Aşama\#13 [Ağ](https://wiki.archlinux.org/index.php/Beginners%27_Guide#Configure_the_network)** {style="text-align: justify;"}

`# pacman -S networkmanager`

arayüz için

`# pacman -S kdeplasma-applets-plasma-nm`

ve

`# systemctl enable NetworkManager`  
`# systemctl start NetworkManager`

Ben kablosuz ağ kullanmak için yaptığımız aşamalarda nedenini bilmediğim
bir sorun ile karşılaştım.Bu sorunun çözümü için

`# systemctl disable dhcpcd.service`

komutu ile çözdüm.

ve son , artık gönül rahatlığı ile Arch Linux kullanabilirsiniz ,
unutmayın baş ucu kaynağı olarak Arch Wiki vazgeçilmeziniz olsun.

Umarım işinize yarayan bir yazı olmuştur.

BURAK KÖSE
