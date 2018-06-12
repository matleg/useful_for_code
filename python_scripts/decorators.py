"""examples from sametmax"""


def benchmark(func):
    """
    decorator to print function execution time
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print(func.__name__, time.clock() - t)
        return res

    return wrapper


def logging(func):
    """
    Un decorateur qui log l'activite d'un script.
    (Ok, en vrai ça fait un print, mais ça pourrait logger !)
    """

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(func.__name__, args, kwargs)
        return res

    return wrapper


def counter(func):
    """
    Un compter qui compte et affiche le nombre de fonction qu'une fonction
    a ete executee
    """

    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print("{0} a ete utilisee: {1}x".format(func.__name__, wrapper.count))
        return res

    wrapper.count = 0
    return wrapper


@counter
@benchmark
@logging
def reverse_string(string):
    return string[::-1]


print(reverse_string("Karine alla en Irak"))
print(reverse_string("Sa nana snob porte de trop bons ananas"))

## reverse_string ('Karine alla en Irak',) {}
## wrapper 0.000132
## wrapper a ete utilisee: 1x
## karI ne alla eniraK
## reverse_string ('Sa nana snob porte de trop bons ananas',) {}
## wrapper 0.000128
## wrapper a ete utilisee: 2x
## sanana snob port ed etrop bons anan aS


import httplib


@counter
@benchmark
@logging
def citation_de_futurama_au_hasard():
    conn = httplib.HTTPConnection("slashdot.org:80")
    conn.request("HEAD", "/index.html")
    for key, value in conn.getresponse().getheaders():
        if key.startswith("x-b") or key.startswith("x-f"):
            return value
    return "No, I'm ... doesn't!"


print(citation_de_futurama_au_hasard())
print(citation_de_futurama_au_hasard())
