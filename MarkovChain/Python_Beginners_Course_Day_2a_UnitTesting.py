Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> m = Markov('this is interesting')
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    m = Markov('this is interesting')
NameError: name 'Markov' is not defined
>>> 
= RESTART: C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py
>>> m = Markov('this is interesting')
>>> m.predict('s')
't'
>>> import test_markov
loading
>>> test_markov.__name__
'test_markov'
>>> 
= RESTART: C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py
E
======================================================================
ERROR: test_predict (__main__.TestMarkov)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py", line 5, in test_predict
    m = Markov('ab')
NameError: name 'Markov' is not defined

----------------------------------------------------------------------
Ran 1 test in 0.011s

FAILED (errors=1)
>>> 
= RESTART: C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py
E
======================================================================
ERROR: test_predict (__main__.TestMarkov)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py", line 6, in test_predict
    m = Markov('ab')
NameError: name 'Markov' is not defined

----------------------------------------------------------------------
Ran 1 test in 0.058s

FAILED (errors=1)
>>> 
= RESTART: C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py
.
----------------------------------------------------------------------
Ran 1 test in 0.071s

OK
>>> dir()
['TestMarkov', '__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'markov', 'unittest']
>>> import sys
>>> sys.path
['C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python', 'C:\\Users\\Prachi', 'C:\\Users\\Prachi\\AppData\\Local\\Programs\\Python\\Python38-32\\python38.zip', 'C:\\Users\\Prachi\\AppData\\Local\\Programs\\Python\\Python38-32\\DLLs', 'C:\\Users\\Prachi\\AppData\\Local\\Programs\\Python\\Python38-32\\lib', 'C:\\Users\\Prachi\\AppData\\Local\\Programs\\Python\\Python38-32', 'C:\\Users\\Prachi\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages']
>>> import missing
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    import missing
ModuleNotFoundError: No module named 'missing'
>>> 
= RESTART: C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py
.
----------------------------------------------------------------------
Ran 1 test in 0.031s

OK
>>> 
= RESTART: C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py
.
----------------------------------------------------------------------
Ran 1 test in 0.075s

OK
>>> 
= RESTART: C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py
.
----------------------------------------------------------------------
Ran 1 test in 0.008s

OK
>>> 
= RESTART: C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py
E.
======================================================================
ERROR: test_get_table (__main__.TestMarkov)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py", line 14, in test_get_table
    self.asserEqual(res, {})
AttributeError: 'TestMarkov' object has no attribute 'asserEqual'

----------------------------------------------------------------------
Ran 2 tests in 0.016s

FAILED (errors=1)
>>> 
= RESTART: C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py
F.
======================================================================
FAIL: test_get_table (__main__.TestMarkov)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py", line 14, in test_get_table
    self.assertEqual(res, {})
AssertionError: {'a': {'b': 2, 'c': 1}, 'b': {'a': 1}, 'c': {'a': 1}} != {}
- {'a': {'b': 2, 'c': 1}, 'b': {'a': 1}, 'c': {'a': 1}}
+ {}

----------------------------------------------------------------------
Ran 2 tests in 0.026s

FAILED (failures=1)
>>> 
= RESTART: C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.015s

OK
>>> 
= RESTART: C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py
F.
======================================================================
FAIL: test_get_table (__main__.TestMarkov)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py", line 14, in test_get_table
    self.assertEqual(res, {'a': {'b': 2, 'c': 8}, 'b': {'a': 1}, 'c': {'a': 1}})
AssertionError: {'a': {'b': 2, 'c': 1}, 'b': {'a': 1}, 'c': {'a': 1}} != {'a': {'b': 2, 'c': 8}, 'b': {'a': 1}, 'c': {'a': 1}}
- {'a': {'b': 2, 'c': 1}, 'b': {'a': 1}, 'c': {'a': 1}}
?                     ^

+ {'a': {'b': 2, 'c': 8}, 'b': {'a': 1}, 'c': {'a': 1}}
?                     ^


----------------------------------------------------------------------
Ran 2 tests in 0.034s

FAILED (failures=1)
>>> 
= RESTART: C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.023s

OK
>>> 
= RESTART: C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py
.E.
======================================================================
ERROR: test_get_table2 (__main__.TestMarkov)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py", line 17, in test_get_table2
    res = markov.get_table('abacab', size = 2)
TypeError: get_table() got an unexpected keyword argument 'size'

----------------------------------------------------------------------
Ran 3 tests in 0.022s

FAILED (errors=1)
>>> 
= RESTART: C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py
>>> 
= RESTART: C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py
>>> 
= RESTART: C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.029s

OK
>>> import xml.tree
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    import xml.tree
ModuleNotFoundError: No module named 'xml.tree'
>>> import xml.etree
>>> dir(xml.etree)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__']
>>> 
= RESTART: C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py
...E
======================================================================
ERROR: test_predict2 (__main__.TestMarkov)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py", line 13, in test_predict2
    m = markov.Markov('abc', size = 2)
TypeError: __init__() got an unexpected keyword argument 'size'

----------------------------------------------------------------------
Ran 4 tests in 0.044s

FAILED (errors=1)
>>> 
= RESTART: C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py
>>> 
= RESTART: C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py
...E
======================================================================
ERROR: test_predict2 (__main__.TestMarkov)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py", line 13, in test_predict2
    m = markov.Markov('abc', size = 2)
TypeError: __init__() got an unexpected keyword argument 'size'

----------------------------------------------------------------------
Ran 4 tests in 0.040s

FAILED (errors=1)
>>> 
= RESTART: C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py
>>> 
= RESTART: C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py
...E
======================================================================
ERROR: test_predict2 (__main__.TestMarkov)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py", line 14, in test_predict2
    self.assertEqual(res, 'c')
NameError: name 'res' is not defined

----------------------------------------------------------------------
Ran 4 tests in 0.036s

FAILED (errors=1)
>>> 
= RESTART: C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py
...E
======================================================================
ERROR: test_predict2 (__main__.TestMarkov)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py", line 14, in test_predict2
    res = m.predict('ab')
  File "C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python\markov.py", line 19, in predict
    raise KeyError(f'{txt} not found')
KeyError: 'ab not found'

----------------------------------------------------------------------
Ran 4 tests in 0.039s

FAILED (errors=1)
>>> 
= RESTART: C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py
>>> 
= RESTART: C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py
..EE
======================================================================
ERROR: test_predict (__main__.TestMarkov)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py", line 9, in test_predict
    res = m.predict('a')
  File "C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python\markov.py", line 20, in predict
    table = self.tables.get(len(txt)-1)
AttributeError: 'list' object has no attribute 'get'

======================================================================
ERROR: test_predict2 (__main__.TestMarkov)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py", line 14, in test_predict2
    res = m.predict('ab')
  File "C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python\markov.py", line 20, in predict
    table = self.tables.get(len(txt)-1)
AttributeError: 'list' object has no attribute 'get'

----------------------------------------------------------------------
Ran 4 tests in 0.041s

FAILED (errors=2)
>>> 
= RESTART: C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py
>>> 
= RESTART: C:/Users/Prachi/Desktop/My Folders/03.Personal Fun Projects/Python/test_markov.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.038s

OK
>>> greeting = '\U0001F638'
>>> print(greeting)
😸
>>> greeting = '\U0001f361'
>>> print(greeting)
🍡
>>> 