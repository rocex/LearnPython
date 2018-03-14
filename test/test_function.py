def func(a, b=5):
    c = a + b
    print('\na:', a, 'b:', b, 'c:', c)

    return c


def report(name, *grades):
    total_grade = 0

    for grade in grades:
        total_grade += grade

    print('\n' + name, 'total_grade is', total_grade)


def report2(name, **keyVale):
    print('\n' + name)

    for k, v in keyVale.items():
        print('\t', k, v)


report("Tom")
report("Tom", 4)
report("Tom", 4, 8, 10)

report2('John', age=10, country='China', education='bachelor[本科]')

print('func(2):', func(2))
print('func(b=3, a=2):', func(b=3, a=2))
print("func(b=4, a=3):", func(b=4, a=3))
