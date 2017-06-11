Title: Üs alma işlemi (a^x) - Divide and Conquer
Date: 2015-10-11 08:00
Author: Burak
Category: Algoritma
Tags: algorithm, divide and conquer
Slug: pow-daq

Üs alma işlemi kullanılan programlama dilinin standart olarak verdiği işlemler ile gayet kolay olarak yapılabilen bir işlemdir.En basit hali ile çözüm şu şekildedir.

```
def brute(num, x):
    result = 1
    for i in range(x):
        result *= num
    return result
```

Bu çözüm iteratif olarak yazılmış ve `O(n)` karmaşıklığına sahip hoş olmayan bir çözümdür. Şimdi bu çözümü `Divide and Conquer` mantığına uygun bir çözüm ile yazalım.

```
def div_conq(num, x):
    if x == 0:
        return 1
    elif x % 2 == 0:
        return div_conq(num, x / 2) * div_conq(num, x / 2)
    else
        return num * div_conq(num, x / 2) * div_conq(num, x / 2)
```

Çözümü divide and conquer mantığına göre çözsekte karmaşıklıkta hala değişiklik olmadı ve zaman karmaşıklığımız `O(n)`. Biraz dikkat ederseniz gereksiz tekrarlar olduğunu fark edebilirsiniz. Bunları önlemek için aşağıdaki gibi bir yol izleyebiliriz.

```
def div_conq(num, x):
    if x == 0:
        return 1
    temp = div_conq(num, x / 2)
    if x % 2 == 0:
        return temp * temp
    else:
        return num * temp * temp
```

Artık karmaşıklığımız `O(logn)` olmuştur. Fakat yazdığımız kod negatif sayısal için çalışmayacaktır. Ufak bir ekleme ile şu hale getirebilriz.

```
def div_conq(num, x):
    if x == 0:
        return 1
    temp = div_conq(num, x / 2)
    if x % 2 == 0:
        return temp * temp
    else:
        if(x > 0):
            return num*temp*temp;
        else:
            return (temp*temp)/num;
```
