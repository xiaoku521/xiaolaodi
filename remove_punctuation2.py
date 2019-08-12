
import string


def remove_punctuation2(s):
    ''' 功能： 去除s中的标点符号。
        注意事项： s 只能包含一个单词。'''

    special_characters = '.,?!:;#()"' # 把里面的字符都去掉

    for c in special_characters:

        s = s.replace(c, ' ') # 防止出现把 apple,apple 移掉逗号后变成 appleapple 情况

    s = s.replace('--', ' ')
    
    lst = s.split('\'')
    lst2 = list( filter(lambda x: x != '', lst) )
    return '\''.join(lst2)



def remove_punctuation(s):

    special_characters = '.,?!:;#()"' # 把里面的字符都去掉

    for c in special_characters:

        s = s.replace(c, ' ') # 防止出现把 apple,apple 移掉逗号后变成 appleapple 情况

    s = s.replace('--', ' ')

    s = s.strip() # 去除前后的空格

    

    if '\'' in s:

        n = len(s)

        t = '' # 用来收集我需要保留的字符

        for i in range(n):

            if s[i] == '\'':

                i_is_ok = i - 1 >= 0 and i + 1 < n

                if i_is_ok and s[i-1] in string.ascii_letters and s[i+1] in string.ascii_letters:

                    t += s[i]

            else:

                t += s[i]

        return t

    else:

        return s
