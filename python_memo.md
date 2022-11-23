# PYMEMO

##  for...else syntax 

```python
for i in foo:
    if i == 0:
        break
else:
    print("i was never 0")
```
 
 

##  underscores 

__double_leading_underscore : __foo replaced by the interpreter by  _classname__foo so that it does not overlap

_single_leading_underscore : _internal_name : private variable : ignored in "from xxx import *",
unless specified in __all__ , can be accessed directly inside a class (no name replacement) however
IDEs will issue warning

single_trailing_underscore_ : avoid conflicts with keywords and build_exe_options



##  multiple inheritance 

multiple inheritance : copy of the first method found
class C(B,A): __init__ from B is copied, not from A.
super() returns the 1st method of the first parent (or grandparent) found



##  instances 

instance.value : looked for in : 1-instance, 2-subclass, 3-superclass, 4-object

keep track of instances:
```python
class A:
    instances = []
    def __init__(self, foo):
        self.foo = foo
        A.instances.append(self)
```

At the end of the program :
```python
foo_vars = {id(instance):instance.foo for instance in A.instances}
```



##  force reinstall 

reinstall package when it really does not work!
```bash
pip install --user --force-reinstall --ignore-installed --no-binary :all: package name
```






## imports / packages 

```python
import mod
mod.__file__
> 'C:\\users\\mat\\mod.py'
```
python >=3.3 : __init__.py not necessary to make a package




##  pytest 

pytest: assert an error is raised:
```python
with pytest.raises(ValueError):
    fibonacci(-1)
```




    
##  mutual imports 

Mutual top-level imports: from SO

If you do import foo inside bar and import bar inside foo, it will work fine. 
By the time anything actually runs, both modules will be fully loaded and will have references to each other.

The problem is when instead you do from foo import abc and from bar import xyz. 
Because now each module requires the other module to already be imported 
(so that the name we are importing exists) before it can be imported.





##  sequence 

Why is “1000000000000000 in range(1000000000000001)” so fast in Python 3?  from SO

The Python 3 range() object doesn't produce numbers immediately; 
it is a smart sequence object that produces numbers on demand.
The object also implements the object.__contains__ hook, and calculates if your number is part of its range. 

For example, 994 is in range(4, 1000, 2) because:
    4 <= 994 < 1000, and
    (994 - 4) % 2 == 0.


range is not a generator:
```python
>>> a = range(5)
>>> print(list(a))
[0, 1, 2, 3, 4]
>>> print(list(a))
[0, 1, 2, 3, 4]

range actually is a sequence, just like a list:
>>> import collections.abc
>>> isinstance(a, collections.abc.Sequence)
True
```



## default values parameters & mutable arguments

For functions:

```python
In [7]: def f(l=[1,2,3]):
   ...:     l.append(4)
   ...:     return l
   ...:

In [8]: f()
Out[8]: [1, 2, 3, 4]

In [9]: f([5,5])
Out[9]: [5, 5, 4]

In [10]: f()
Out[10]: [1, 2, 3, 4, 4]
```

For class variables:

```python
class A:
    v = ['c', 'p']
 
>>> g1 = A()
>>> g2 = A()
>>> g1.v.pop()
'p'
>>> g2.v
['c']
```


```python
def foo(x=[]):
...     x.append(1)
...     print x
...
>>> foo()
[1]
>>> foo()
[1, 1]
>>> foo()
[1, 1, 1]
```

Instead, you should use a sentinel value denoting "not given" and replace with the mutable you'd like as default:

```python
>>> def foo(x=None):
...     if x is None:
...         x = []
...     x.append(1)
...     print x
>>> foo()
[1]
>>> foo()
[1]
```





##  build with cx_Freeze 

windows command : "python setup.py build"

in setup.py:

```python

from cx_Freeze import setup, Executable

packages = ["pkg_resources",
            "os",
            ... ,
            "os"]

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": packages}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
# if sys.platform == "win32":
#     base = "Win32GUI"

setup(name="esiam_server",
      version="0.1",
      description="grpc aum esiam server",
      options={"build_exe": build_exe_options},
      executables=[Executable("esiam_server.py", base=base)])
```








##  pip trick 

Use pip (version 6 or later) with the -t <directory> flag to
copy the libraries into the folder you created in the previous step. For example:
```
pip install -t lib/ <library_name>

from https://pip.pypa.io/en/stable/reference/pip_install/:
-t, --target <dir>

Install packages into <dir>. 
By default this will not replace existing files/folders in <dir>. 
Use –upgrade to replace existing packages in <dir> with new versions.
```



##  subprocess popen VS call 

from SO:
```python
returncode = call(*args, **kwargs)
```

is basically the same as calling

```python
returncode = Popen(*args, **kwargs).wait()
```

call is just a convenience function. It's implementation in CPython is in subprocess.py:

```python
def call(*popenargs, timeout=None, **kwargs):
    """Run command with arguments.  Wait for command to complete or
    timeout, then return the returncode attribute.
    The arguments are the same as for the Popen constructor.  Example:
    retcode = call(["ls", "-l"])
    """
    with Popen(*popenargs, **kwargs) as p:
        try:
            return p.wait(timeout=timeout)
        except:
            p.kill()
            p.wait()
            raise
```
it's a thin wrapper around Popen.



##  bitwise operations 


bin         = 00000100000  
~bin        = 11111011111  

nb          = 00011111100  
nb &~ bin   = 00011011100  

~x = -x-1  
x    = 0000100110  
-x   = 1111011000  --> NOT ...001!  
-x-1 = 1111011001 = ~x  




##  python composition 

from http://blog.thedigitalcatonline.com/blog/2014/08/20/python-3-oop-part-3-delegation-composition-and-inheritance/

```python
class A:
    def __init__(self, number, status):
        self.number = number
        self.status = status

    def extract(self):
        return ....

    def add(self):
        return ....


class B:
    def __init__(self, number, status):
        self.a = A(number, status)

    def extract(self):
        self.a.extract()

    def add(self):
        self.a.add()

    def __getattr__(self, attr):
        return getattr(self.a, attr)

```

##  sort dict by value 

from realpython:

```python
dx = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

>>> sorted(dx.items(), key=lambda x: x[1])
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]
```


##  namedtuple 

from realpython:

```python
from collections import namedtuple
Car = namedtuple('Car', 'color mileage')
my_car = Car('red', 3812.4)

>>> my_car.color
'red'
>>> my_car.mileage
3812.4

>>> my_car
Car(color='red' , mileage=3812.4)

# Like tuples, namedtuples are immutable:
>>> my_car.color = 'blue'
AttributeError: "can't set attribute"
```


##  site.py 

automatically started when running python executable: python -m site 
(site is imported from pythonpath and executed)





##   
##   
##   
##   
##   



