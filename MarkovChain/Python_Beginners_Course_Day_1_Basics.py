Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = 'Prachi'
>>> print(name)
Prachi
>>> def add(x,y):
	return x + y

>>> add(3,4)
7
>>> 
= RESTART: C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/markov.py
>>> add(7,9)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    add(7,9)
NameError: name 'add' is not defined
>>> class Add:
	def __add__(self, other):
		return other

	
>>> a = Add()
>>> a + 10
10
>>> a.__add__(15)
15
>>> p = Markov('pr')
>>> p
<__main__.Markov object at 0x03ACF1A8>
>>> p.table is None
True
>>> p.predict('p')
'b'
>>> key = 'dog'
>>> definitions = {'dog' : 'barking animal'}
>>> definition[key]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    definition[key]
NameError: name 'definition' is not defined
>>> definitions[key]
'barking animal'
>>> hash(key)
458974790
>>> 'cat' in definitions
False
>>> dir(definitions)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> help(definitions)
Help on dict object:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  
 |  Methods defined here:
 |  
 |  __contains__(self, key, /)
 |      True if the dictionary has the specified key, else False.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the dict keys.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |  
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |  
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |  
 |  get(self, key, default=None, /)
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |  
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |  
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
 |  
 |  popitem(self, /)
 |      Remove and return a (key, value) pair as a 2-tuple.
 |      
 |      Pairs are returned in LIFO (last-in, first-out) order.
 |      Raises KeyError if the dict is empty.
 |  
 |  setdefault(self, key, default=None, /)
 |      Insert key with a value of default if key is not in the dictionary.
 |      
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |  
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Create a new dictionary with keys from iterable and values set to value.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> help(definitions.get)
Help on built-in function get:

get(key, default=None, /) method of builtins.dict instance
    Return the value for key if key is in the dictionary, else default.

>>> definitions.get('dog','wrong')
'barking animal'
>>> definitions.get('cat','wrong')
'wrong'
>>> name = 'Rajas'
>>> 'R' in name
True
>>> 'r' in name
False
>>> 
= RESTART: C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/markov.py
>>> get_table
<function get_table at 0x031AC0B8>
>>> get_table('ab')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    get_table('ab')
  File "C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/markov.py", line 41, in get_table
    result[char] = char_dict
NameError: name 'result' is not defined
>>> 
= RESTART: C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/markov.py
>>> get_table('ab')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    get_table('ab')
  File "C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/markov.py", line 30, in get_table
    out = txt[i+1]
IndexError: string index out of range
>>> 
= RESTART: C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/markov.py
>>> get_table('ab')
{'a': {'b': 1}}
>>> get_table("'aban')
	  
SyntaxError: EOL while scanning string literal
>>> get_table('aban')
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    get_table('aban')
  File "C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/markov.py", line 35, in get_table
    char_dict = result[char]
NameError: name 'result' is not defined
>>> 
= RESTART: C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/markov.py
>>> get_table('aban')
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    get_table('aban')
  File "C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/markov.py", line 35, in get_table
    char_dict = result[char]
NameError: name 'result' is not defined
>>> get_table('ab')
{'a': {'b': 1}}
>>> get_table('aban')
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    get_table('aban')
  File "C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/markov.py", line 35, in get_table
    char_dict = result[char]
NameError: name 'result' is not defined
>>> 
= RESTART: C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/markov.py
>>> get_table('aban')
{'a': {'b': 1, 'n': 1}, 'b': {'a': 1}}
>>> dir()
['Markov', '__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'get_table']
>>> 
= RESTART: C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/markov.py
>>> get_table('ab')
{'a': {'b': 1}}
>>> get_table('aban')
{'a': {'b': 1, 'n': 1}, 'b': {'a': 1}}
>>> 
= RESTART: C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/markov.py
>>> dir()
['Markov', '__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'get_table']
>>> my = Markov()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    my = Markov()
TypeError: __init__() missing 1 required positional argument: 'txt'
>>> my = Markov('abc')
>>> my.table
{'a': {'b': 1}, 'b': {'c': 1}}
>>> get_table('abc')
{'a': {'b': 1}, 'b': {'c': 1}}
>>> 
= RESTART: C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/markov.py
>>> get_table('abc')
{'a': {'b': 1}, 'b': {'c': 1}}
>>> my.table
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    my.table
NameError: name 'my' is not defined
>>> my = Markov('abc')
>>> my.tabel
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    my.tabel
AttributeError: 'Markov' object has no attribute 'tabel'
>>> my.table
{'a': {'b': 1}, 'b': {'c': 1}}
>>> my.predict('a')
'b'
>>> my.predict('a')
'b'
>>> my.predict('a')
'b'
>>> my.table('aban')
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    my.table('aban')
TypeError: 'dict' object is not callable
>>> a = Markov('xyx')
>>> a.table
{'x': {'y': 1}, 'y': {'x': 1}}
>>> food = Markov('Pani puri is my favorite food')
>>> food.table
{'P': {'a': 1}, 'a': {'n': 1, 'v': 1}, 'n': {'i': 1}, 'i': {' ': 2, 's': 1, 't': 1}, ' ': {'p': 1, 'i': 1, 'm': 1, 'f': 2}, 'p': {'u': 1}, 'u': {'r': 1}, 'r': {'i': 2}, 's': {' ': 1}, 'm': {'y': 1}, 'y': {' ': 1}, 'f': {'a': 1, 'o': 1}, 'v': {'o': 1}, 'o': {'r': 1, 'o': 1, 'd': 1}, 't': {'e': 1}, 'e': {' ': 1}}
>>> food.predict('y')
' '
>>> food.predict('t')
'e'
>>> food.predict('e')
' '
>>> 