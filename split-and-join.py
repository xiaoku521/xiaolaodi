Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:24:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> name = 'wyh'
>>> assert name == 'wyh'
>>> assert name == 'Wyh'
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    assert name == 'Wyh'
AssertionError
>>> t = 'i am                    ok'
>>> t
'i am                    ok'
>>> t.split()
['i', 'am', 'ok']
>>> t = ' i am                    ok '
>>> t.split()
['i', 'am', 'ok']
>>> '#'
join(t.split())
SyntaxError: multiple statements found while compiling a single statement
>>> '#'.join(t.split())
'i#am#ok'
>>> '-'.join(t.split())
'i-am-ok'
>>> 'Z'.join(t.split())
'iZamZok'
>>> 'Zzzz....Z...'.join(t.split())
'iZzzz....Z...amZzzz....Z...ok'
>>> fruit_basket = ['apple', 'banana', 'pear', 'tomato']
>>> fruit_basket.pop()
'tomato'
>>> fruit_basket
['apple', 'banana', 'pear']
>>> fruit_basket.pop(0)
'apple'
>>> fruit_basket
['banana', 'pear']
>>> lst = [ 'apple', 'orange', 'banana' ]

num = 300 # 多少个水果

import random
s = ''
for i in range(num):
        w = random.choice(lst) # 随机在lst中选一个元素
        if i % 3 == 0: # 百分号%代表模
                s += ' ' + w.upper()
        if i % 3 == 1:
                s += ' ' + w.title()
        if i % 3 == 2:
                s += ' ' + w
fruit = s.strip()
print(fruit)

SyntaxError: multiple statements found while compiling a single statement
>>> 
