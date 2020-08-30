Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import urllib
>>> import urllib.request as req
>>> req
<module 'urllib.request' from 'C:\\Users\\Prachi\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\urllib\\request.py'>
>>> url = 'https://www.gutenberg.org/files/1342/1342-0.txt'
>>> fin = req.urlopen(url)
>>> data = fin.read()
>>> len(data)
799738
>>> data[:100]
b'\xef\xbb\xbf\r\nThe Project Gutenberg EBook of Pride and Prejudice, by Jane Austen\r\n\r\nThis eBook is for the use'
>>> txt = data.decode('utf-8')
>>> txt[1:100]
'\r\nThe Project Gutenberg EBook of Pride and Prejudice, by Jane Austen\r\n\r\nThis eBook is for the use o'
>>> 
= RESTART: C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py
>>> fetch_url('https://www.gutenberg.org/files/11/11-0.txt', 'alice.txt')
>>> fetch_url('https://www.gutenberg.org/files/1342/1342-0.txt', 'pp.txt')
>>> 
= RESTART: C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py
>>> 
= RESTART: C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py
>>> fetch_url('https://www.gutenberg.org/files/1342/1342-0.txt', 'pp.txt')
>>> fetch_url('https://www.gutenberg.org/files/11/11-0.txt', 'alice.txt')
>>> m = from_file('pp.txt', size=4)

>>> m.predict('D')
'a'
>>> m.predict('Dar')
'c'
>>> m.predict('Darc')
'y'
>>> m.predict('Darcy')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    m.predict('Darcy')
  File "C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py", line 33, in predict
    table = self.tables[len(txt)-1]
IndexError: list index out of range
>>> m.predict('rcys')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    m.predict('rcys')
  File "C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py", line 37, in predict
    #options = self.table.get(txt, {})
KeyError: 'rcys not found'
>>> m.predict('rcy'')
	  
SyntaxError: EOL while scanning string literal
>>> m.predict('arcy')
' '
>>> m.predict('arcy')
'.'
>>> m.predict('arcy')
'\n'
>>> m.predict('arcy')
','
>>> m.predict('arcy')
'\n'
>>> m.predict('arcy')
','
>>> m.predict('arcy')
' '
>>> m.predict('arcy')
'.'
>>> m.predict('arcy')
','
>>> m.predict('arcy')
'’'
>>> m.predict('rcy’')
's'
>>> len(m.tables)
4
>>> len(m.tables[0])
92
>>> len(m.tables[-1])
29195
>>> help(open)
Help on built-in function open in module io:

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    Open file and return a stream.  Raise OSError upon failure.
    
    file is either a text or byte string giving the name (and the path
    if the file isn't in the current working directory) of the file to
    be opened or an integer file descriptor of the file to be
    wrapped. (If a file descriptor is given, it is closed when the
    returned I/O object is closed, unless closefd is set to False.)
    
    mode is an optional string that specifies the mode in which the file
    is opened. It defaults to 'r' which means open for reading in text
    mode.  Other common values are 'w' for writing (truncating the file if
    it already exists), 'x' for creating and writing to a new file, and
    'a' for appending (which on some Unix systems, means that all writes
    append to the end of the file regardless of the current seek position).
    In text mode, if encoding is not specified the encoding used is platform
    dependent: locale.getpreferredencoding(False) is called to get the
    current locale encoding. (For reading and writing raw bytes use binary
    mode and leave encoding unspecified.) The available modes are:
    
    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================
    
    The default mode is 'rt' (open for reading text). For binary random
    access, the mode 'w+b' opens and truncates the file to 0 bytes, while
    'r+b' opens the file without truncation. The 'x' mode implies 'w' and
    raises an `FileExistsError` if the file already exists.
    
    Python distinguishes between files opened in binary and text modes,
    even when the underlying operating system doesn't. Files opened in
    binary mode (appending 'b' to the mode argument) return contents as
    bytes objects without any decoding. In text mode (the default, or when
    't' is appended to the mode argument), the contents of the file are
    returned as strings, the bytes having been first decoded using a
    platform-dependent encoding or using the specified encoding if given.
    
    'U' mode is deprecated and will raise an exception in future versions
    of Python.  It has no effect in Python 3.  Use newline to control
    universal newlines mode.
    
    buffering is an optional integer used to set the buffering policy.
    Pass 0 to switch buffering off (only allowed in binary mode), 1 to select
    line buffering (only usable in text mode), and an integer > 1 to indicate
    the size of a fixed-size chunk buffer.  When no buffering argument is
    given, the default buffering policy works as follows:
    
    * Binary files are buffered in fixed-size chunks; the size of the buffer
      is chosen using a heuristic trying to determine the underlying device's
      "block size" and falling back on `io.DEFAULT_BUFFER_SIZE`.
      On many systems, the buffer will typically be 4096 or 8192 bytes long.
    
    * "Interactive" text files (files for which isatty() returns True)
      use line buffering.  Other text files use the policy described above
      for binary files.
    
    encoding is the name of the encoding used to decode or encode the
    file. This should only be used in text mode. The default encoding is
    platform dependent, but any encoding supported by Python can be
    passed.  See the codecs module for the list of supported encodings.
    
    errors is an optional string that specifies how encoding errors are to
    be handled---this argument should not be used in binary mode. Pass
    'strict' to raise a ValueError exception if there is an encoding error
    (the default of None has the same effect), or pass 'ignore' to ignore
    errors. (Note that ignoring encoding errors can lead to data loss.)
    See the documentation for codecs.register or run 'help(codecs.Codec)'
    for a list of the permitted encoding error strings.
    
    newline controls how universal newlines works (it only applies to text
    mode). It can be None, '', '\n', '\r', and '\r\n'.  It works as
    follows:
    
    * On input, if newline is None, universal newlines mode is
      enabled. Lines in the input can end in '\n', '\r', or '\r\n', and
      these are translated into '\n' before being returned to the
      caller. If it is '', universal newline mode is enabled, but line
      endings are returned to the caller untranslated. If it has any of
      the other legal values, input lines are only terminated by the given
      string, and the line ending is returned to the caller untranslated.
    
    * On output, if newline is None, any '\n' characters written are
      translated to the system default line separator, os.linesep. If
      newline is '' or '\n', no translation takes place. If newline is any
      of the other legal values, any '\n' characters written are translated
      to the given string.
    
    If closefd is False, the underlying file descriptor will be kept open
    when the file is closed. This does not work when a file name is given
    and must be True in that case.
    
    A custom opener can be used by passing a callable as *opener*. The
    underlying file descriptor for the file object is then obtained by
    calling *opener* with (*file*, *flags*). *opener* must return an open
    file descriptor (passing os.open as *opener* results in functionality
    similar to passing None).
    
    open() returns a file object whose type depends on the mode, and
    through which the standard file operations such as reading and writing
    are performed. When open() is used to open a file in a text mode ('w',
    'r', 'wt', 'rt', etc.), it returns a TextIOWrapper. When used to open
    a file in a binary mode, the returned class varies: in read binary
    mode, it returns a BufferedReader; in write binary and append binary
    modes, it returns a BufferedWriter, and in read/write mode, it returns
    a BufferedRandom.
    
    It is also possible to use a string or bytearray as a file for both
    reading and writing. For strings StringIO can be used like a file
    opened in a text mode, and for bytes a BytesIO can be used like a file
    opened in a binary mode.

>>> 
= RESTART: C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py
>>> m = from_file('pp.txt', size=4)
>>> repl(m)
Welcom to REPL
Hit ctc-c to exit
> D
a
> Da
r
> Dar
c
> Darc
y
> Darcy
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    repl(m)
  File "C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py", line 32, in repl
    pred = m.predict(txt)
  File "C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py", line 43, in predict
    table = self.tables[len(txt)-1]
IndexError: list index out of range
>>> 
= RESTART: C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py
Traceback (most recent call last):
  File "C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py", line 84, in <module>
    if __name == '__main__':
NameError: name '__name' is not defined
>>> 
= RESTART: C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py
Welcom to REPL
Hit ctc-c to exit
> Darcy
too long
Traceback (most recent call last):
  File "C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py", line 86, in <module>
    repl(m)
  File "C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py", line 36, in repl
    print(pred)
UnboundLocalError: local variable 'pred' referenced before assignment
>>> 
= RESTART: C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py
Welcom to REPL!
Hit ctc-c to exit
> Darcy
too long, try again!
Traceback (most recent call last):
  File "C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py", line 86, in <module>
    repl(m)
  File "C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py", line 36, in repl
    print(pred)
UnboundLocalError: local variable 'pred' referenced before assignment
>>> 
= RESTART: C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py
Welcom to REPL!
Hit ctc-c to exit
> Darcy
too long, try again!
> rcy


> cy S
Traceback (most recent call last):
  File "C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py", line 87, in <module>
    repl(m)
  File "C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py", line 33, in repl
    pred = m.predict(txt)
  File "C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py", line 51, in predict
    raise KeyError(f'{txt} not found')
KeyError: 'cy S not found'
>>> cy s
SyntaxError: invalid syntax
>>> 
= RESTART: C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py
Welcom to REPL!
Hit ctc-c to exit
> cy s
m
> soo
n
> soon
;
> 
= RESTART: C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py
Welcom to REPL!
Hit ctc-c to exit
> cy S
not found try again
> anim
a
> raja
not found try again
> 
Traceback (most recent call last):
  File "C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py", line 89, in <module>
    repl(m)
  File "C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py", line 31, in repl
    txt = input('> ')
KeyboardInterrupt
>>> 
= RESTART: C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py
Welcom to REPL!
Hit ctc-c to exit
> D
a
> 
Goodbye
>>> name = 'prachi'
>>> last = 'ghadge'
>>> f 'Hello \U0001600 {name[:5])} {last.title()}'
SyntaxError: invalid syntax
>>> f'Hello \U0001600 {name[:5])} {last.title()}'
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 6-14: truncated \UXXXXXXXX escape
>>> f'Hello \U0001f600 {name[:5])} {last.title()}'
SyntaxError: f-string: unmatched ')'
>>> f'Hello \U0001f600 {name[:5]} {last.title()}'
'Hello 😀 prach Ghadge'
>>> f'Hello \U0001f600 {name[:5].title()} {last.title()}'
'Hello 😀 Prach Ghadge'
>>> 
= RESTART: C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py
Traceback (most recent call last):
  File "C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py", line 10, in <module>
    import argpars
ModuleNotFoundError: No module named 'argpars'
>>> 
= RESTART: C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py
Traceback (most recent call last):
  File "C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py", line 105, in <module>
    main(sys.argv[1:])
  File "C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py", line 97, in main
    opts = ap.parse_arg(args)
AttributeError: 'ArgumentParser' object has no attribute 'parse_arg'
>>> 
= RESTART: C:\Users\Prachi\Desktop\My Folders\03.Personal Fun Projects\Python\markov.py
>>> 