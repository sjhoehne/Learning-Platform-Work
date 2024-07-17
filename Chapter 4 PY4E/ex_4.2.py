#Example One From 4.2
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'
print(greet('en'), 'Glenn')
print(greet('es'), 'Sally')
print(greet('fr'), 'Michael')

#Example Two From 4.2
def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)