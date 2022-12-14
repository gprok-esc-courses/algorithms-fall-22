
def test1(a, *args):
    print(a)
    print(args)

def test2(a, **kwargs):
    print(a)
    print(kwargs)

def test3(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)


test1('A', 1, 2, 3)
test1('B')

test2('C', type='sample', weight=56)

test3('D', 7, 8, 9, type='sample', weight=56)