Title: Type class nedir? - FP
Date: 2017-06-10 19:00
Author: Burak
Category: Fonksiyonel Programlama
Tags: fp, scala
Slug: typeclass

Yazıya başlamadan önce belirtmem gerekir ki örnekleri Scala üzerinden verdiğim için Scala ve temel düzeyde implicit kavramını bildiğinizi varsaymaktayım.

Type class'ı basitçe anlatmak gerekirse, uygulamamız sahip olmak istediğimiz bazı işlevsellikleri sağlayan bir arayüzdür. Scala'da çoğunlukla trait ile birlikte en az bir type parametresi ile tanımlanır. En önemli özelliklerinden biri `ad-hoc polymorphism` sağlamasıdır. Örnek vermeden önce `parametric polymorphism` ve `ad-hoc polymorphism` terimlerine biraz değinmek isterim.

Parametric polymorphism kısaca, implementasyonu tüm tipler için aynı olan kod parçasıdır. Scala standard kütüphanesinden örnek vermek istersek, `head` methodunu örnek verebiliriz. Düşünün elimizde bir string listesi ve bir inteğer listesi bulunmakta.
```
val sList = List("a", "b", "c")
val iList = List(1, 2, 3)
sList.head
// res0: String = a
iList.head
// res1: Int = 1
```
Yapılan iş, elimizde olan listenin ilk elemanın döndürmektir. Değişen tek şey sahip olduğumuz type.

Ad-hoc polymorphism ise biraz daha farklı ve kısaca method overloading olarak anlatabilirz. Sahip olduğumuz methodun işlevi değişmektedir. Type class kısaca bu özelliği bize sağlamaktadır. Örnek vermek için ilk olarak ADT tanımlamalarından başlayalım.

```
sealed trait Shape
case class Rectangle(width: Double, height: Double) extends Shape
case class Circle(radius: Double) extends Shape
```

Devamında Encoder type class'ımızı tanımlayalım.

```
trait Encoder[A] {
  def encode(value: A): List[String]
}
```

Genelde aşağıdaki gibi bir companion object tanımlaması güzel bir pratiktir.

```
object Encoder {
  // "Summoner" method
  def apply[A](implicit enc: Encoder[A]): Encoder[A] = enc

  // "Constructor" method
  def instance[A](func: A => List[String]): Encoder[A] =
    new Encoder[A] {
      def encode(value: A): List[String] =
        func(value)
    }
}
```

Kısaca yapmak istediğimiz, elimizde olan adt'leri string listesi şeklinde tanımlamak. Bunun için;

```
implicit val rectangleEncoder = Encoder.instance[Rectangle] { rec =>
  List(
    rec.width.toString,
    rec.height.toString
  )
}

implicit val circleEncoder = Encoder.instance[Circle] { cir =>
  List(cir.radius.toString)
}
```

tanımlamalarını yapalım. Şimdi gerçek işi yapacak olan kodu yazalım.

```
def print[A](value: Seq[A])(implicit encoder: Encoder[A]): Unit = {
  println(
    value
      .map(value => encoder.encode(value).mkString("|"))
      .mkString("{\n", "\n", "\n}"))
}
```

Kod oldukça basit. Parametre olarak Seq[A] alıyor ve implicit olarak bu type için tanımlanmış encoder'a bakıyor ve encode edilmiş stringi ekrana yazdırıyor.

```
val circles = List(
  Circle(5),
  Circle(6)
)

print(circles)
// {
//  5.0
//  6.0
// }

val rectangles = List(
  Rectangle(1, 2),
  Rectangle(2, 3)
)

print(rectangles)
// {
// 1.0|2.0
// 2.0|3.0
// }
```

Kodun üzerine biraz daha düşünelim. Mesela şunu denersek;

```
val shapes: Seq[Shape] = List(
  Circle(5),
  Circle(6),
  Rectangle(1, 2),
  Rectangle(2, 3)
)

print(shapes)
```

Şu hatayı verecektir.

> could not find implicit value for parameter encoder: Encoder[Shape]

Encoder type class'ı sadece shape için olduğundan kodu geliştirmek için şunu yazabiliriz;

```
implicit val shapeEncoder = Encoder.instance[Shape] {
  case rec: Rectangle =>
    List(
      rec.width.toString,
      rec.height.toString
    )
  case circle: Circle => List(circle.radius.toString)
}
```

ve çıktı.

```
{
5.0
6.0
1.0|2.0
2.0|3.0
}
```

Burak KOSE