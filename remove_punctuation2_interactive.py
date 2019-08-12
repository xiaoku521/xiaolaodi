Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:24:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s = 'you\'re'
>>> lst = s.split('\'')
>>> lst
['you', 're']
>>> s = '\'you\'re'
>>> s
"'you're"
>>> lst = s.split('\'')
>>> lst
['', 'you', 're']
>>> '\''.join(lst)
"'you're"
>>> list(filter(lambda x: x != '', lst))
['you', 're']
>>> ================================ RESTART ================================
>>> 
>>> remove_punctuation2('\'you\'re')
"you're"
>>> remove_punctuation2('\'you\'re\'')
"you're"
>>> remove_punctuation2('\'you\'re\' a boy.')
"you're' a boy "
>>> ================================ RESTART ================================
>>> 
>>> remove_punctuation2('\'you\'re\' a boy.')
['', 'you', 're', ' a boy ']
"you're' a boy "
>>> filter(True, ['a','b','b','c'])
<filter object at 0x03B3C8D0>
>>> list(filter(True, ['a','b','b','c']))
Traceback (most recent call last):

  File "<pyshell#14>", line 1, in <module>
    list(filter(True, ['a','b','b','c']))
TypeError: 'bool' object is not callable
>>> def isa(x):
	return x == 'a'

>>> list(filter(isa, ['a','b','b','c']))
['a']
>>> def isb(x):
	return x == 'b'

>>> list(filter(isb, ['a','b','b','c']))
['b', 'b']
>>> 
