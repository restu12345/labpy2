def tes():
    a=int(input("bilangan1 ="))
    b=int(input("bilangan2 ="))
    c=int(input("bilangan3 ="))

    if a>b and a>c:
        print(a, 'Terbesar')
    elif b>a and b>c:
        print (b, 'Terbesar')
    else:
        print (c, 'Terbesar')

tes()
