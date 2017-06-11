def foo():
    'Bu method hileli olarak 1 veya 0 döndürür'
    pass


def my_foo():
    val1 = foo()
    val2 = foo()
    if val1 == 0 and val2 == 1:
        return 0  # 0.24 olasılık
    if val1 == 1 and val2 == 0:
        return 1  # 0.24 olasılık
    return my_foo()  # 1 - 0.24 - 0.24 olasılık
