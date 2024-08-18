def outer_Func(a, b):
    def inner_func():
        return a + b

    result = inner_func() + 5
    return result


result = outer_Func(5, 10)
print(result)
