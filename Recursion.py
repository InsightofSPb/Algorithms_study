def countdown(i):
    print(i)
    if i <= 0:
        return  # базовый случай
    else:
        countdown(i-1)  # то есть можно без return возвращать


'''
Стек
'''


def greet(name='Sasha'):
    print(f'hello, {name}!')
    greet2(name)
    print("getting ready to say bye...")
    bye()


def greet2(name):
    print(f'how are you, {name}!')


def bye():
    print('ok bye!')


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
