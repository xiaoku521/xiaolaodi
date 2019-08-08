Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:24:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from collections import Counter
>>> Counter(['apple', 'apple', 'banana'])
Counter({'apple': 2, 'banana': 1})
>>> c = Counter(['apple', 'apple', 'banana'])
>>> c.most_common()
[('apple', 2), ('banana', 1)]
>>> 
