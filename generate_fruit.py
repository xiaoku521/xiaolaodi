lst = [ 'apple', 'orange', 'banana' ]

num = 6 # 多少个水果

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
