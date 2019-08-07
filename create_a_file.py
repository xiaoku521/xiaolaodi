Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:24:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s = 'apple banana'
>>> ================================ RESTART ================================
>>> 
{'apple': 2, 'banana': 3, 'orange': 4}
>>> s
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> s = 'apple banana'
>>> f = open('a.txt', 'w')
>>> f
<_io.TextIOWrapper name='a.txt' mode='w' encoding='cp936'>
>>> f.write(s)
12
>>> f.close()
>>> 
KeyboardInterrupt
>>> f = open('a.txt', 'w')
>>> f.write('orange')
6
>>> f.close()
>>> f = open('a.txt', 'a')
>>> f.write('avocado')
7
>>> f.close()
>>> f = open('a.txt', 'a')
>>> f.write('\navocado')
8
>>> f.close()
>>> f.close()
>>> s
'apple banana'
>>> 
