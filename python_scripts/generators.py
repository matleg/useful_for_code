"""examples from sametmax"""


def creerGenerateur():
    mylist = range(3)
    for i in mylist:
        yield i * i


generateur1 = creerGenerateur()  # cree un generateur
print(generateur1)  # generateur1 est un objet !

for i in generateur1:
    print(i)
print("une fois")

for i in generateur1:
    print(i)
print("pas 2 fois")

generateur2 = creerGenerateur()  # cree un generateur
print(generateur2)  # generateur2 est un objet !

for i in generateur2:
    print(i)
print("une fois gene2")


# ----------------------------------------------------------------------
def read_large_file(file_object):
    """
    Uses a generator to read a large file lazily
    """
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data


# ----------------------------------------------------------------------
def process_file(path):
    """process large file without taking all memory"""
    try:
        with open(path) as file_handler:
            for line in read_large_file(file_handler):
                # process line
                print(line)
    except (IOError, OSError):
        print("Error opening / processing file")


# ----------------------------------------------------------------------


# other example:
gen = (ord(i) for i in "ABCDEFGHI")
print(gen)  # generator object
# on genere une liste a partir du generateur
print("essai 1: " + str(list(gen)))  # premiere fois
print("essai 1: " + str(list(gen)))  # deuxieme fois


# ----------------------------------------------------------------------


def countdown():
    yield 3
    yield 2
    yield 1
    yield 'Blast off!'


# generator
g = countdown()
next(g)  # 2
x = next(g)  # 2
print(x)
y, z = next(g), next(g)  # 1, 'Balst off'
print(z)
next(g)  # 'erro'

# ----------------------------------------------------------------------

# Tip to get started with generators: find places in your code where you do the following:
#
# def something():
#     result = []
#     for ... in ...:
#         result.append(x)
#     return result
#
# And replace it by:
#
# def iter_something():
#     for ... in ...:
#         yield x

# def something():  # Only if you really need a list structure
#     return list(iter_something())
