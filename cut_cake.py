def cut_cake(parts):
    try:
        return 1 / int(parts)
    except (ZeroDivisionError, TypeError, ValueError):
        return 'You, normal?'

cake = cut_cake([1, 2, 5])
print(cake)

def do_something(x):
   try:
       print(x)
   except:
       print('Bye!!!')


x = 0
while x < 10:
   do_something(x)
x += 1
