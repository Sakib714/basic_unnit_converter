# Basic Unit Converter 

# Math Functions

def meter2centimeter(int):
    return int * 100


def centimeter2meter(int):
    return int / 100


def meter2milimeter(int):
    return int * 1000


def milimeter2meter(int):
    return int / 1000


def centimeter2milimeter(int):
    return int * 10


def milimeter2centimetter(int):
    return int / 10


def meter2feet(int):
    return int * 3.28


def feet2meter(int):
    return int / 3.28


def meter2inch(int):
    return int * 39.97


def inch2meter(int):
    return int / 39.97


def feet2inch(int):
    return int * 12


def inch2feet(int):
    return int / 12


def inch2milimeter(int):
    return int * 25.4


def milimeter2inch(int):
    return int / 25.4


def inch2centimeter(int):
    return int * 2.54


def centimeter2inch(int):
    return int / 2.54


def yard2inch(int):
    return int * 36


def inch2yard(int):
    return int / 36


def meter2yard(int):
    return int * 1.0936


def yard2meter(int):
    return int / 11.0936


line = '*'
for i in range(20):
    line = line + '*'

print(line)

print('  Choose one:         ')

line = '*'
for i in range(20):
    line = line + '*'

print(line)
print('1. Meter to Centimeter')
print('2. centimeter to  Meter')
print('3. Meter to Millimeter')
print('4. Millimeter to Meter')
print('5. Centimeter to Meter')
print('6. Millimeter to Centimeter')
print('7. Meter  to Feet')
print('8. Feet to Meter')
print('9. Meter too Inch')
print('10. Inch to Meter')
print('11. Feet to Inch')
print('12. Inch to Feet')
print('13.. inch to Millimeter')
print('14. Millimeter to inch')
print('15. Inch to Centimeter')
print('16. Centimeter to Inch')
print('17. Yard to Inch')
print('18. Inch to Yard')
print('19. Meter to Yard')
print('20. Yard to Meter')

# User Input

gg = int(input('Which one you choose from the list: '))
integer = int(input('Enter a value: '))

if gg == 1:
    x= meter2centimeter(integer)
    print('Outpput: ', x)
elif gg == 2:
    x = centimeter2meter(integer)
    print('Outpput: ', x)

elif gg == 3:
    x = meter2milimeter(integer)
    print('Outpput: ', x)

elif gg == 4:
    x = milimeter2meter(integer)
    print('Outpput: ', x)

elif gg == 5:
    x = centimeter2milimeter(integer)
    print('Outpput: ', x)

elif gg == 6:
    x = milimeter2centimetter(integer)
    print('Outpput: ', x)

elif gg == 7:
    x = meter2feet(integer)
    print('Outpput: ', x)

elif gg == 8:
    x = feet2meter(integer)
    print('Outpput: ', x)

elif gg == 10:
    x = inch2meter(integer)
    print('Outpput: ', x)

elif gg == 11:
    x = feet2inch(integer)
    print('Outpput: ', x)

elif gg == 12:
    x = inch2feet(integer)
    print('Outpput: ', x)

elif gg == 13:
    x= inch2milimeter(integer)
    print('Outpput: ', x)

elif gg == 14:
    x = milimeter2inch(integer)
    print('Outpput: ', x)

elif gg == 15:
    x = inch2centimeter(integer)
    print('Outpput: ', x)

elif gg == 16:
    x = centimeter2inch(integer)
    print('Outpput: ', x)

elif gg == 17:
    x = yard2inch(integer)
    print('Outpput: ', x)

elif gg == 18:
    x = inch2yard(integer)
    print('Outpput: ', x)

elif gg == 19:
    x = meter2yard(integer)
    print('Outpput: ', x)
elif gg == 20:
    x= yard2meter(integer)
    print('Outpput: ', x)

else:
    Exception('Something went wrong!')
