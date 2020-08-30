'''
This is Markov module.
This is docstring for the module.

>>>m= Markov('ab')
>>>m.predict('a')
'b'

'''
import argparse
import random
import sys
import urllib.request as req

def fetch_url(url, fname):
    fin = req.urlopen(url)
    data = fin.read()
    fout = open(fname, mode='wb')#writebinary
    fout.write(data)
    fout.close()
    #with open(fname, mode='wb') as fout:
        #fout.write(data), no closing needed here
    
def from_file(fname, size=1):
    fin = open(fname, encoding='utf8')
    return Markov(fin.read(), size=size)

def repl(m):
    print('Welcom to REPL!')
    print('Hit ctc-c to exit')
    while True:
        try:
            txt = input('> ')
        except KeyboardInterrupt:
            print('Goodbye')
            break
            
        try:
            pred = m.predict(txt)
        except IndexError:
            print('too long, try again!')
        except KeyError:
            print('not found try again')
        else:
            print(pred)
    
class Markov:
    def __init__(self, txt, size = 1):
        #self.table = get_table(txt)
        self.tables = []
        for i in range(size):
            self.tables.append(get_table(txt, size=i+1))

    def predict(self, txt):
        table = self.tables[len(txt)-1]
        options = table.get(txt, {})
        #options = self.table.get(txt, {})
        if not options:
            raise KeyError(f'{txt} not found')

        possible = []
        for key in options:
            count = options[key]
            for i in range(count):
                possible.append(key)
        return random.choice(possible)
                

def get_table(txt, size=1):
    '''
    This is function docstring. This function returns a transitition table.

    >>> get_table('ab')
    {'a':{'b' : 1}}
    
    '''
    results = {}
    for i in range(len(txt)):
        chars = txt[i:i+size]
        try:
            out = txt[i+size]
        except IndexError:
            break

        char_dict = results.get(chars, {})

        char_dict.setdefault(out, 0)
        char_dict[out] += 1
        
        results[chars] = char_dict
    return results

def main(args):
    ap = argparse.ArgumentParser()
    ap.add_argument('-f', '--file', help='File to read')
    ap.add_argument('-s', '--size', help='Markov size default 1', default=1, type=int)
    opts = ap.parse_args(args)
    if opts.file:
        m = from_file(opts.file, size=opts.size)
        repl(m)
        
if __name__ == '__main__':
    #m = from_file('pp.txt', size=4)
    #repl(m)
    main(sys.argv[1:])
    
