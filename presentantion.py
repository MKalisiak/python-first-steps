print('print(2 + 2)')
print(2 + 2)

print()

print('a = 2 + 3.5')
print('print(a)')
a = 2 + 3.5
print(a)

print()

print('Division always returns floating point')
print("print(4 / 2)")
print(4 / 2)

print()

print('To do floor division - discard fractional part (like int division in C) - use // operator instead of /')
print('print(5 // 2)')
print(5 // 2)

print()

print('Use ** operator for power operation')
print('print(2 ** 3)')
print(2 ** 3)

print()

print('===================================================================================================')
print()

print("Strings can use either single quote or double quote")
print("a = 'Hello world'")
print("print(a)")
a = 'Hello world'
print(a)
print('a = "Hello world"')
print("print(a)")
a = "Hello world"
print(a)

print()

print("Building strings - different methods")
print("name = 'Michał'")
name = 'Michał'
print("print('Hello ' + name)")
print('Hello ' + name)
print("print('Hello {}'.format(name))")
print('Hello {}'.format(name))
print("print('Hello {username}'.format(username=name))")
print('Hello {username}'.format(username=name))
print("print(f'Hello {name}')")
print(f'Hello {name}')

print()

print("Strings can be multiplied")
print("print('xyz' * 3)")
print('xyz' * 3)

print()

print("Strings can be indexed")
print("a = 'My first string'")
a = 'My first string'
print("print(a[0])")
print(a[0])
print("print(a[5])")
print(a[5])
print("print(a[-1])")
print(a[-1])
print("print(a[3:8])")
print(a[3:8])
print("print(a[3:])")
print(a[3:])

print()

print("Strings are immutable")
print("a = 'I love Python'")
a = 'I love Python'
print("Calling a[0] = 'U' would throw an error (try it if you dare)")
# a[0] = 'U'
print("You need to build a new string e.g.")
print("a = 'We' + a[1:]")
print("print(a)")
a = 'We' + a[1:]
print(a)

print()

print("To get string length use builtin function len()")
print("print(len(a))")
print(len(a))

print()

print('===================================================================================================')
print()

print("Lists are created using square brackets")
print("a = [1, 0, 2, 3, 5, 8, 13]")
a = [1, 1, 2, 3, 5, 8, 13]
print("Lists can be indexed just like strings")
print("print(a[4])")
print(a[4])
print("print(a[-1])")
print(a[-1])

print()

print("Lists are mutable (unlike strings)")
print("a[1] = 1")
a[1] = 1
print("print(a)")
print(a)

print()

print("You can append items to lists")
print("a.append(21)")
a.append(21)
print("print(a)")
print(a)

print()

print("len() function applies to lists as well")
print("print(len(a))")
print(len(a))

print()

print("Lists can contain values of different types (even lists!)")
print("a = [1, 2.5, 'foo', [1,2,3]]")
a = [1, 2.5, 'foo', [1,2,3]]
print("print(a)")
print(a)
print("print(a[3])")
print(a[3])
print("print(a[3][1])")
print(a[3][1])

print()

print('===================================================================================================')
print()

print("Multiple values can be assigned at once")
print("a, b = 2, 4")
a, b = 2, 4
print("print(a)")
print(a)
print("print(b)")
print(b)

print()

print("It can be used to effectively swap values of variables")
print("a, b = b, a")
a, b = b, a
print("print(a)")
print(a)
print("print(b)")
print(b)

print()

print('===================================================================================================')
print()

print("Boolean values are capitalized in Python")
print("a, b = True, False")
a, b = True, False
print("print(a, b)")
print(a, b)

print()

print("If works with anything that can be cast to boolean value")
print("The conditional block has to be indented")
print("c = 'test'")
c = 'test'
print('''\
if a:
    print("a is True")
if b:
    print("b is True")
if 2 > 3:
    print("2 is greater than 3")
else:
    print("2 is not greater than 3")
if c == "test":
    print("c is equal to string "test")
if []:
    print("[] is not empty")
else:
    print("empty list equals False")
print("this print statement is unconditional")
''')
if a:
    print("a is True")
if b:
    print("b is True")
if 2 > 3:
    print("2 is greater than 3")
else:
    print("2 is not greater than 3")
if c == "test":
    print("c is equal to string 'test'")
if []:
    print("[] is not empty")
else:
    print("empty list casts to False")

print()

print("Boolean operators are words 'and', 'or', 'not', 'in'")
print('''\
if 2 == 2 and True:
    print("'and' works")
if 2 == 3 or 2 == 2:
    print("'or' works")
if not []:
    print("'not' works")
if 'bar' in ['foo', 'test', 'bar']:
    print("'in' works")
''')
if 2 == 2 and True:
    print("'and' works")
if 2 == 3 or 2 == 2:
    print("'or' works")
if not []:
    print("'not' works")
if 'bar' in ['foo', 'test', 'bar']:
    print("'in' works")

print()

print('===================================================================================================')
print()

print("for loop iterates over an iterable (e.g. list) given to it")
print("The looped block has to be indented")
print('''\
for item in ['foo', 'test', 'bar']:
    print(len(item))
    print(item)
''')
for item in ['foo', 'test', 'bar']:
    print(len(item))
    print(item)

print()

print("Instead of for(int i = 0; i < 5; i++) you can use range() function:")
print("Using range() does not create a list in memory, so it is more efficient than using [0, 1, 2, 3, 4]")
print('''\
for i in range(5):
    print(i)
''')
for i in range(5):
    print(i)

print()

print("A list can be created using range()")
print("print( list( range(5) ) )")
print(list(range(5)))

print()

print("range() takes up to 3 arguments")
print("When 2 arguments are present, they are lower (inclusive) and upper (exclusive) bounds")
print("print( list( range(2, 5) ) )")
print(list(range(2, 5)))

print()

print("Single argument range(x) is equivalent to range(0, x)")

print()

print("When 3 arguments are present, the third one is a step")
print("print( list( range(0, 10, 2) ) )")
print(list(range(0, 10, 2)))

print()

print("Use break and continue keywords to control loop flow even more")
print('''\
for i in range(10):
    if i % 2 == 0:
        print(f"{i} is even")
        continue
    if i % 7 == 0:
        print(f"{i} is a multiple of 7, aborting...")
        print("(because why not)")
        break
    print(f"{i} is odd")
else:
    print("Loop completed without breaking")
''')
for i in range(10):
    if i % 2 == 0:
        print(f"{i} is even")
        continue
    if i % 7 == 0:
        print(f"{i} is a multiple of 7, aborting...")
        print("(because why not)")
        break
    print(f"{i} is odd")
else:
    print("Loop completed without breaking")

print()

print("Use for...else to do something if a loop doesn't break")
print('''\
for i in range(3):
    if i == 3:
        break
else:
    print("Loop completed without breaking")
''')
for i in range(3):
    if i == 3:
        break
else:
    print("Loop completed without breaking")