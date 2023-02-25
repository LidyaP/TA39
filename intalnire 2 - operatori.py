# x = 3
# x += 3 # x = x+3
# x -= 3 # x = x-3
# x *= 3 # x = x*3
# x /= 3 # x = x/3
# print(x)

# aritmeci

# x = int(input('Introdu numarul x\n''))
# y = int(input('Introdu numarul y\n''))
# z = x + y
# n = x - y
# p = x * y
# l = x / y
# k = x % y #(modulo)
# i = x ** y #(restul)

# comparare
# a = 5
# b = 6
# assert a == b
# assert a != b # a este diferit de b
# assert a < b
# assert a > b
# assert a >= b
# assert a <= b

# operatori logici
# and - returneaza true daca toate statementuri sunt adevarate
# or - returneaza true daca cel putin una din stat este adevarata
# not - returneaza inverseaza raspunsul (adica daca e adevarat, el o sa returneze fals) mai are echivalent si !=
# ex a != 5 (echivalent la not)

x = 5
y = 6
z = 21

# assert x == 5 and y == 6 and z == 21
# print('assert is ok')
# assert x == 5 or y == 6 and z == 55
# print('assert is ok')
# assert (not x > 7 and y == 6)
# print('assert is ok')

# IF
# a = 3
# b = 10
#
# if not a == 3:
#     print( 'A nu este 3')
# else :
#     print(' A este  3')

# a = 5
# b = 7

# if a == 5:
#     if b == 7:
#         print ('test')
#     else :
#         print ('Test2')
# else :
#     print('Test3')

# if, else if, (elif) else = toate astea functioneaza pe scheme logica
# else este un controler, controleaza flow-ul

# a = 5
# if a == 1:
#     print('ati ales limba romana')
# elif a == 2:
#     print('ati ales limba englez')
# elif a == 3:
#     print('ati ales limba franceza')
# else :
#     print('nu ati ales nicio limba')
