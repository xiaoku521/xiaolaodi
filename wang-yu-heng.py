Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:24:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
ORANGE Orange apple ORANGE Banana banana BANANA Banana apple ORANGE Orange apple ORANGE Apple banana BANANA Banana banana APPLE Apple apple APPLE Banana banana APPLE Orange banana BANANA Banana banana ORANGE Orange orange ORANGE Orange orange ORANGE Apple apple APPLE Orange banana BANANA Banana orange BANANA Banana orange ORANGE Apple apple APPLE Orange orange APPLE Orange orange APPLE Orange orange APPLE Orange banana BANANA Orange apple APPLE Banana banana BANANA Orange apple BANANA Apple orange BANANA Banana apple BANANA Banana orange APPLE Apple banana APPLE Apple banana BANANA Orange orange BANANA Apple apple APPLE Apple banana ORANGE Apple orange APPLE Apple apple ORANGE Apple banana APPLE Banana orange APPLE Banana banana APPLE Apple orange APPLE Orange orange BANANA Banana orange ORANGE Apple apple BANANA Banana banana APPLE Banana banana ORANGE Apple orange BANANA Apple apple ORANGE Banana apple BANANA Apple apple BANANA Orange apple ORANGE Apple apple APPLE Orange orange APPLE Apple orange APPLE Orange banana ORANGE Banana banana BANANA Apple banana BANANA Apple apple APPLE Apple orange APPLE Apple banana BANANA Apple banana ORANGE Banana orange ORANGE Apple apple BANANA Banana apple BANANA Orange apple APPLE Orange apple BANANA Orange apple BANANA Orange orange APPLE Orange apple APPLE Banana orange APPLE Orange banana ORANGE Banana orange BANANA Apple orange APPLE Apple orange BANANA Orange banana APPLE Banana apple ORANGE Banana orange APPLE Apple banana BANANA Orange apple BANANA Orange apple BANANA Apple banana BANANA Apple apple APPLE Banana orange ORANGE Apple apple BANANA Banana banana BANANA Apple apple APPLE Apple banana ORANGE Apple apple BANANA Apple banana ORANGE Apple banana ORANGE Banana apple ORANGE Apple apple ORANGE Banana orange BANANA Apple orange BANANA Banana apple BANANA Orange apple APPLE Orange orange ORANGE Orange apple APPLE Apple apple APPLE Apple orange APPLE Banana apple APPLE Orange banana ORANGE Orange orange
>>> fruit1 = fruit.lower()
>>> fruit1
'orange orange apple orange banana banana banana banana apple orange orange apple orange apple banana banana banana banana apple apple apple apple banana banana apple orange banana banana banana banana orange orange orange orange orange orange orange apple apple apple orange banana banana banana orange banana banana orange orange apple apple apple orange orange apple orange orange apple orange orange apple orange banana banana orange apple apple banana banana banana orange apple banana apple orange banana banana apple banana banana orange apple apple banana apple apple banana banana orange orange banana apple apple apple apple banana orange apple orange apple apple apple orange apple banana apple banana orange apple banana banana apple apple orange apple orange orange banana banana orange orange apple apple banana banana banana apple banana banana orange apple orange banana apple apple orange banana apple banana apple apple banana orange apple orange apple apple apple orange orange apple apple orange apple orange banana orange banana banana banana apple banana banana apple apple apple apple orange apple apple banana banana apple banana orange banana orange orange apple apple banana banana apple banana orange apple apple orange apple banana orange apple banana orange orange apple orange apple apple banana orange apple orange banana orange banana orange banana apple orange apple apple orange banana orange banana apple banana apple orange banana orange apple apple banana banana orange apple banana orange apple banana apple banana banana apple apple apple banana orange orange apple apple banana banana banana banana apple apple apple apple banana orange apple apple banana apple banana orange apple banana orange banana apple orange apple apple orange banana orange banana apple orange banana banana apple banana orange apple apple orange orange orange orange apple apple apple apple apple apple orange apple banana apple apple orange banana orange orange orange'
>>> fruit2 = fruit1.split()
>>> fruit2
['orange', 'orange', 'apple', 'orange', 'banana', 'banana', 'banana', 'banana', 'apple', 'orange', 'orange', 'apple', 'orange', 'apple', 'banana', 'banana', 'banana', 'banana', 'apple', 'apple', 'apple', 'apple', 'banana', 'banana', 'apple', 'orange', 'banana', 'banana', 'banana', 'banana', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'apple', 'apple', 'apple', 'orange', 'banana', 'banana', 'banana', 'orange', 'banana', 'banana', 'orange', 'orange', 'apple', 'apple', 'apple', 'orange', 'orange', 'apple', 'orange', 'orange', 'apple', 'orange', 'orange', 'apple', 'orange', 'banana', 'banana', 'orange', 'apple', 'apple', 'banana', 'banana', 'banana', 'orange', 'apple', 'banana', 'apple', 'orange', 'banana', 'banana', 'apple', 'banana', 'banana', 'orange', 'apple', 'apple', 'banana', 'apple', 'apple', 'banana', 'banana', 'orange', 'orange', 'banana', 'apple', 'apple', 'apple', 'apple', 'banana', 'orange', 'apple', 'orange', 'apple', 'apple', 'apple', 'orange', 'apple', 'banana', 'apple', 'banana', 'orange', 'apple', 'banana', 'banana', 'apple', 'apple', 'orange', 'apple', 'orange', 'orange', 'banana', 'banana', 'orange', 'orange', 'apple', 'apple', 'banana', 'banana', 'banana', 'apple', 'banana', 'banana', 'orange', 'apple', 'orange', 'banana', 'apple', 'apple', 'orange', 'banana', 'apple', 'banana', 'apple', 'apple', 'banana', 'orange', 'apple', 'orange', 'apple', 'apple', 'apple', 'orange', 'orange', 'apple', 'apple', 'orange', 'apple', 'orange', 'banana', 'orange', 'banana', 'banana', 'banana', 'apple', 'banana', 'banana', 'apple', 'apple', 'apple', 'apple', 'orange', 'apple', 'apple', 'banana', 'banana', 'apple', 'banana', 'orange', 'banana', 'orange', 'orange', 'apple', 'apple', 'banana', 'banana', 'apple', 'banana', 'orange', 'apple', 'apple', 'orange', 'apple', 'banana', 'orange', 'apple', 'banana', 'orange', 'orange', 'apple', 'orange', 'apple', 'apple', 'banana', 'orange', 'apple', 'orange', 'banana', 'orange', 'banana', 'orange', 'banana', 'apple', 'orange', 'apple', 'apple', 'orange', 'banana', 'orange', 'banana', 'apple', 'banana', 'apple', 'orange', 'banana', 'orange', 'apple', 'apple', 'banana', 'banana', 'orange', 'apple', 'banana', 'orange', 'apple', 'banana', 'apple', 'banana', 'banana', 'apple', 'apple', 'apple', 'banana', 'orange', 'orange', 'apple', 'apple', 'banana', 'banana', 'banana', 'banana', 'apple', 'apple', 'apple', 'apple', 'banana', 'orange', 'apple', 'apple', 'banana', 'apple', 'banana', 'orange', 'apple', 'banana', 'orange', 'banana', 'apple', 'orange', 'apple', 'apple', 'orange', 'banana', 'orange', 'banana', 'apple', 'orange', 'banana', 'banana', 'apple', 'banana', 'orange', 'apple', 'apple', 'orange', 'orange', 'orange', 'orange', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'orange', 'apple', 'banana', 'apple', 'apple', 'orange', 'banana', 'orange', 'orange', 'orange']
>>> for x in fruit2:
	if 'apple' == x:
		print(x)

		
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
apple
>>> for x in fruit2:
	if 'apple' != x:
		print(x)

		
orange
orange
orange
banana
banana
banana
banana
orange
orange
orange
banana
banana
banana
banana
banana
banana
orange
banana
banana
banana
banana
orange
orange
orange
orange
orange
orange
orange
orange
banana
banana
banana
orange
banana
banana
orange
orange
orange
orange
orange
orange
orange
orange
orange
banana
banana
orange
banana
banana
banana
orange
banana
orange
banana
banana
banana
banana
orange
banana
banana
banana
orange
orange
banana
banana
orange
orange
orange
banana
banana
orange
banana
banana
orange
orange
orange
banana
banana
orange
orange
banana
banana
banana
banana
banana
orange
orange
banana
orange
banana
banana
banana
orange
orange
orange
orange
orange
orange
banana
orange
banana
banana
banana
banana
banana
orange
banana
banana
banana
orange
banana
orange
orange
banana
banana
banana
orange
orange
banana
orange
banana
orange
orange
orange
banana
orange
orange
banana
orange
banana
orange
banana
orange
orange
banana
orange
banana
banana
orange
banana
orange
banana
banana
orange
banana
orange
banana
banana
banana
banana
orange
orange
banana
banana
banana
banana
banana
orange
banana
banana
orange
banana
orange
banana
orange
orange
banana
orange
banana
orange
banana
banana
banana
orange
orange
orange
orange
orange
orange
banana
orange
banana
orange
orange
orange
>>> for x in fruit2:
	if 'apple' != x:
		print(x)
		remove(apple)

		
orange
Traceback (most recent call last):
  File "<pyshell#13>", line 4, in <module>
    remove(apple)
NameError: name 'remove' is not defined
>>> fruit
'ORANGE Orange apple ORANGE Banana banana BANANA Banana apple ORANGE Orange apple ORANGE Apple banana BANANA Banana banana APPLE Apple apple APPLE Banana banana APPLE Orange banana BANANA Banana banana ORANGE Orange orange ORANGE Orange orange ORANGE Apple apple APPLE Orange banana BANANA Banana orange BANANA Banana orange ORANGE Apple apple APPLE Orange orange APPLE Orange orange APPLE Orange orange APPLE Orange banana BANANA Orange apple APPLE Banana banana BANANA Orange apple BANANA Apple orange BANANA Banana apple BANANA Banana orange APPLE Apple banana APPLE Apple banana BANANA Orange orange BANANA Apple apple APPLE Apple banana ORANGE Apple orange APPLE Apple apple ORANGE Apple banana APPLE Banana orange APPLE Banana banana APPLE Apple orange APPLE Orange orange BANANA Banana orange ORANGE Apple apple BANANA Banana banana APPLE Banana banana ORANGE Apple orange BANANA Apple apple ORANGE Banana apple BANANA Apple apple BANANA Orange apple ORANGE Apple apple APPLE Orange orange APPLE Apple orange APPLE Orange banana ORANGE Banana banana BANANA Apple banana BANANA Apple apple APPLE Apple orange APPLE Apple banana BANANA Apple banana ORANGE Banana orange ORANGE Apple apple BANANA Banana apple BANANA Orange apple APPLE Orange apple BANANA Orange apple BANANA Orange orange APPLE Orange apple APPLE Banana orange APPLE Orange banana ORANGE Banana orange BANANA Apple orange APPLE Apple orange BANANA Orange banana APPLE Banana apple ORANGE Banana orange APPLE Apple banana BANANA Orange apple BANANA Orange apple BANANA Apple banana BANANA Apple apple APPLE Banana orange ORANGE Apple apple BANANA Banana banana BANANA Apple apple APPLE Apple banana ORANGE Apple apple BANANA Apple banana ORANGE Apple banana ORANGE Banana apple ORANGE Apple apple ORANGE Banana orange BANANA Apple orange BANANA Banana apple BANANA Orange apple APPLE Orange orange ORANGE Orange apple APPLE Apple apple APPLE Apple orange APPLE Banana apple APPLE Orange banana ORANGE Orange orange'
>>> fruit=fruit.lower
>>> frut
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    frut
NameError: name 'frut' is not defined
>>> fruit
<built-in method lower of str object at 0x03380848>
>>> fruit=fruit.lower()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    fruit=fruit.lower()
AttributeError: 'builtin_function_or_method' object has no attribute 'lower'
>>> ================================ RESTART ================================
>>> 
BANANA Banana orange BANANA Orange banana APPLE Banana orange BANANA Banana orange APPLE Orange apple APPLE Banana apple ORANGE Orange apple ORANGE Orange orange BANANA Apple banana ORANGE Banana orange APPLE Apple banana APPLE Orange apple APPLE Orange apple APPLE Orange orange ORANGE Apple banana ORANGE Banana apple BANANA Orange orange BANANA Banana apple ORANGE Apple orange BANANA Banana orange BANANA Banana apple ORANGE Orange banana APPLE Banana banana BANANA Orange orange BANANA Orange banana BANANA Orange orange APPLE Apple apple BANANA Apple apple BANANA Orange banana APPLE Orange orange APPLE Apple orange ORANGE Banana apple ORANGE Banana banana ORANGE Banana banana APPLE Apple apple APPLE Orange apple BANANA Orange apple APPLE Apple orange BANANA Orange orange BANANA Apple apple ORANGE Apple apple BANANA Apple banana BANANA Banana orange BANANA Apple apple BANANA Orange banana APPLE Orange apple ORANGE Apple apple ORANGE Orange apple ORANGE Banana orange APPLE Apple orange BANANA Orange banana ORANGE Apple apple BANANA Apple banana ORANGE Apple orange BANANA Apple banana BANANA Apple banana BANANA Apple banana BANANA Banana banana BANANA Banana apple ORANGE Apple apple ORANGE Orange orange ORANGE Apple apple APPLE Apple orange BANANA Banana apple ORANGE Apple apple ORANGE Orange orange BANANA Banana banana BANANA Orange orange APPLE Orange orange BANANA Orange banana APPLE Apple banana ORANGE Orange apple APPLE Apple banana ORANGE Banana banana ORANGE Banana apple ORANGE Orange banana ORANGE Apple apple ORANGE Orange apple BANANA Apple apple BANANA Orange apple ORANGE Banana orange ORANGE Orange banana APPLE Apple apple BANANA Apple orange APPLE Banana apple APPLE Orange orange ORANGE Orange apple ORANGE Orange apple APPLE Orange apple ORANGE Banana orange BANANA Apple apple ORANGE Banana banana APPLE Apple banana ORANGE Apple apple ORANGE Apple apple ORANGE Banana orange APPLE Apple banana BANANA Apple banana APPLE Apple orange APPLE Banana banana
>>> fruit=fruit.lower()
>>> fruit
'banana banana orange banana orange banana apple banana orange banana banana orange apple orange apple apple banana apple orange orange apple orange orange orange banana apple banana orange banana orange apple apple banana apple orange apple apple orange apple apple orange orange orange apple banana orange banana apple banana orange orange banana banana apple orange apple orange banana banana orange banana banana apple orange orange banana apple banana banana banana orange orange banana orange banana banana orange orange apple apple apple banana apple apple banana orange banana apple orange orange apple apple orange orange banana apple orange banana banana orange banana banana apple apple apple apple orange apple banana orange apple apple apple orange banana orange orange banana apple apple orange apple apple banana apple banana banana banana orange banana apple apple banana orange banana apple orange apple orange apple apple orange orange apple orange banana orange apple apple orange banana orange banana orange apple apple banana apple banana orange apple orange banana apple banana banana apple banana banana apple banana banana banana banana banana banana apple orange apple apple orange orange orange orange apple apple apple apple orange banana banana apple orange apple apple orange orange orange banana banana banana banana orange orange apple orange orange banana orange banana apple apple banana orange orange apple apple apple banana orange banana banana orange banana apple orange orange banana orange apple apple orange orange apple banana apple apple banana orange apple orange banana orange orange orange banana apple apple apple banana apple orange apple banana apple apple orange orange orange orange apple orange orange apple apple orange apple orange banana orange banana apple apple orange banana banana apple apple banana orange apple apple orange apple apple orange banana orange apple apple banana banana apple banana apple apple orange apple banana banana'
>>> lst=fruit.split()
>>> list(filter(lambda x: x !='apple',lst))
['banana', 'banana', 'orange', 'banana', 'orange', 'banana', 'banana', 'orange', 'banana', 'banana', 'orange', 'orange', 'banana', 'orange', 'orange', 'orange', 'orange', 'orange', 'banana', 'banana', 'orange', 'banana', 'orange', 'banana', 'orange', 'orange', 'orange', 'orange', 'orange', 'banana', 'orange', 'banana', 'banana', 'orange', 'orange', 'banana', 'banana', 'orange', 'orange', 'banana', 'banana', 'orange', 'banana', 'banana', 'orange', 'orange', 'banana', 'banana', 'banana', 'banana', 'orange', 'orange', 'banana', 'orange', 'banana', 'banana', 'orange', 'orange', 'banana', 'banana', 'orange', 'banana', 'orange', 'orange', 'orange', 'orange', 'banana', 'orange', 'banana', 'banana', 'orange', 'banana', 'banana', 'orange', 'banana', 'orange', 'orange', 'banana', 'orange', 'orange', 'banana', 'orange', 'banana', 'banana', 'banana', 'banana', 'orange', 'banana', 'banana', 'orange', 'banana', 'orange', 'orange', 'orange', 'orange', 'orange', 'banana', 'orange', 'orange', 'banana', 'orange', 'banana', 'orange', 'banana', 'banana', 'orange', 'orange', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana', 'banana', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'banana', 'banana', 'orange', 'orange', 'orange', 'orange', 'banana', 'banana', 'banana', 'banana', 'orange', 'orange', 'orange', 'orange', 'banana', 'orange', 'banana', 'banana', 'orange', 'orange', 'banana', 'orange', 'banana', 'banana', 'orange', 'banana', 'orange', 'orange', 'banana', 'orange', 'orange', 'orange', 'banana', 'banana', 'orange', 'orange', 'banana', 'orange', 'orange', 'orange', 'banana', 'banana', 'orange', 'banana', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'banana', 'orange', 'banana', 'orange', 'banana', 'banana', 'banana', 'orange', 'orange', 'orange', 'banana', 'orange', 'banana', 'banana', 'banana', 'orange', 'banana', 'banana']
>>> filter(lambda x: x !='apple',lst)
<filter object at 0x03D903B0>
>>> lambda x: x !='apple'
<function <lambda> at 0x03B22108>
>>> 
