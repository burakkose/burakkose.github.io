Title: Algebraic Data Types nedir? - FP
Date: 2017-06-09 19:00
Author: Burak
Category: Fonksiyonel Programlama
Tags: fp, scala
Slug: algebraic-data-types

İsmi bu kadar karmaşık olup da arkasındaki fikir bu kadar basit olan bir yapı olduğunu sanmıyorum. Olay tamamen veriyi modellemektir, davranışlar ile ilgilenilmez. Veri modellenirken mantıksal ve(and) ile veya(or) işleminden yararlanılır. Kısaca örnek vermek gerekirse:

```
sealed trait Şekil
case class Çember(v: Double) extends Şekil
case class Üçgen(v1: Int, v2: Int) extends Şekil
```

Örneği anlayabileceğimiz sözlü ifadeye döktüğümüzde ise;

> Şekil bir üçgen `veya` çemberdir

> Üçgen v1 `ve` v2 olmak üzere iki inteğer sahibidir

> Çember v olmak üzere bir inteğer sahibidir

Buradan anlaşılabileceği gibi şekil bir `coproduct`, üçgen ve çember ise `product`'dır. Sahip olduğumuz coproduct ve product ifadelerini daha farklı olarak şu şekilde de tanımlayabiliriz.

```
type Ucgen = (Int, Int)

type Cember = Double

type Sekil = Either[Ucgen, Cember]

val rect: Sekil = Left((3, 4))

val circ: Sekil = Right(1.0)
```

Scala standard kütüphanesinden örnek vermek istersek:

[jtable]
Type, Value Constructors
Option, None ve Some
Either, Left ve Right
Try, Success ve Failure
List, Nil ve ::
[/jtable]

Burak KOSE