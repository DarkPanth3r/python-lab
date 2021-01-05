# https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/networking-using-urllib-in-python

import urllib.request, urllib.parse, urllib.error

#fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
fhand = urllib.request.urlopen('https://tools.ietf.org/rfc/rfc8032.txt')


counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)        