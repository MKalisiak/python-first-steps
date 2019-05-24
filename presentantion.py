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

print()

print('===================================================================================================')
print()

print("To define functions use 'def' keyword followed by function name, arguments and indented body")
print('''
def print_greeting(name):
    print(f"Hello {name}")

print_greeting('Michał')
''')

def print_greeting(name):
    print(f"Hello {name}")

print_greeting('Michał')

print()

print("Arguments can optionally have a desired type with syntax 'argument_name: type'")
print("Also, a function can have a return type with syntax 'def function_name(arguments) -> return_type'")
print('''
def print_fibonacci(bound: int) -> None:
    a, b = 0, 1
    while a < bound:
        print(a, end=" ")
        a, b = b, a+b
    print()

print_fibonacci(2000)
''')
def print_fibonacci(bound: int) -> None:
    a, b = 0, 1
    while a < bound:
        print(a, end=" ")
        a, b = b, a+b
    print()

print_fibonacci(2000)

print()

print("Arguments can have default values so that if they are not passed\n"
      "when the function is called they take on their default values")
print("Arguments without a default value are required")
print('''
def alien_greeting(name, planet="Squanch", attitude="love"):
    print(f"I am {name} from planet {planet}. I {attitude} mankind.")

alien_greeting("Squanchy")\
''')

def alien_greeting(name, planet="Squanch", attitude="love"):
    print(f"I am {name} from planet {planet}. I {attitude} mankind.")

alien_greeting("Squanchy")
print('alien_greeting("Abradolf Lincler", "Earth", "hate")')
alien_greeting("Abradolf Lincler", "Earth", "hate")

print()

print("Arguments can be given by name (they are then called keyword arguments), then their order does not matter")
print()
print("alien_greeting(attitude='despise', name='Thanos', planet='Titan')")
alien_greeting(attitude='despise', name='Thanos', planet='Titan')

print()
print("Positional arguments (not given by name) have to go before the keyword arguments")
print()
print("alien_greeting('Thanos', attitude='despise', planet='Titan')")
alien_greeting('Thor Odinson', attitude='like', planet='Asgard')
print()
print("Calling a function like this would throw an error:")
print("alien_greeting(attitude='despise', 'Thanos', planet='Titan')")
print("(which is actually fine, because it would be unreadable)")

print()

print('===================================================================================================')
print()

print("Tuples are similar to lists, but are immutable (like strings)")
print("They can be indexed, iterated over")
print("Usually lists are used to store the same type of data and are iterated over,")
print("while tuples are usually used with different types of data and are indexed")
print("Tuples can be unpacked (see below) to assign their values to several variables")
print('''
person = ("Michał", "Kalisiak", 22)
first_name, last_name, age = person
print(f"{first_name} {last_name} aged {age}")
''')

person = ("Michał", "Kalisiak", 22)
first_name, last_name, age = person
print(f"{first_name} {last_name} aged {age}")

print()

print('===================================================================================================')
print()

print("Sets are similar to lists with a few differences:")
print(" - they cannot contain duplicates")
print(" - they cannot be indexed - the elements are not in order")
print(" - they are created with curly braces {item, item2}")

print('''
a = {1, 1, 2, 3, 3}
for item in a:
    print(item)
''')

a = {1, 1, 2, 3, 3}
for item in a:
    print(item)

print()

print('===================================================================================================')
print()

print("Dictionaries (or dicts) are sets of 'key: value' pairs")
print("Dictionaries are indexed by keys, keys can be strings or numbers")
print('''
person = {"first_name": "Michał", "last_name": "Kalisiak", "age": 22}
print(person["first_name"])\
''')
person = {"first_name": "Michał", "last_name": "Kalisiak", "age": 22}
print(person["first_name"])

print()

print("Iterating over a dict iterates over its keys")
print('''
for key in person:
    print(key, person[key])
''')
for key in person:
    print(key, person[key])

print()

print("A more elegant of doing the same would be:")
print('''
for key, value in person.items():
    print(key, value)
''')
for key, value in person.items():
    print(key, value)

print()

print('===================================================================================================')
print()

print("List comprehension is a powerful mechanism of creating lists")
print('''
squares = [i**2 for i in range(11)]
print(squares)\
''')
squares = [i**2 for i in range(11)]
print(squares)

print()

print("Conditions can be used in list comprehension")
print('''
even = [i for i in range(11) if i % 2 == 0]
print(even)\
''')
even = [i for i in range(11) if i % 2 == 0]
print(even)

print()

print("Dict comprehension is very similar but for dictionaries")
print('''
squares = {x: x ** 2 for x in range(11)}
print(squares)\
''')
squares = {x: x ** 2 for x in range(11)}
print(squares)

print()

print('===================================================================================================')
print()

print("Be careful when accessing dict values.")
print("If you try to use a key which is not in the dict an error will be thrown")
print('''
d = {'foo': 'bar'}

Calling d['unknown'] would throw an error (try it for yourself)
What you could do is catch the error and handle it somehow:

try:
    print(d['unknown'])
except KeyError:
    print("Dict has no such key")
''')

d = {'foo': 'bar'}

try:
    print(d['unknown'])
except KeyError:
    print("Dict has no such key")

print()
print("You could also use dict.get(key) method which returns None if the key is not present")
print("print(d.get('unknown'))")
print(d.get('unknown'))

print()

print("Or check if the key is present in a dict")
print('''
if "unknown" in d:
    print(d["unknown"])
else:
    print("It's not there")
''')

if "unknown" in d:
    print(d["unknown"])
else:
    print("It's not there")

print()

print('===================================================================================================')
print()

print("To get user input use builtin input() function")
print("It prompts the user to type something and takes an optional argument used as a prompt")

print('''
user_input = input('Echo: ')
''')

user_input = input('Echo: ')
print("print(user_input)")
print(user_input)

print()

print("User input is always treated as a string, so if you want to use it as\n"
      "something else, you will have to cast it (for example with builtin int() function)")
print('''
user_input = input('Type any number of ints (space separated): ')
''')
user_input = input('Type any number of ints (space separated): ')
print("print(sum([int(x) for x in user_input.strip().split(' ')]))")
print(sum([int(x) for x in user_input.strip().split(' ')]))