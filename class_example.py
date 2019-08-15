def add_helper(s):
    K = s.split()
    sum1 = 0
    sum2 = 0
    for x in K:
        lst = x.split('/')
        sum1 += int(lst[0])
        sum2 += int(lst[1])
    return '%d/%d' % (sum1, sum2)


class Score:
    def __init__(self, school, subject, grade, date):
        self.school = school
        self.subject = subject
        self.grade = grade
        self.date = date

    def __str__(self):
        return '%s -- %s %s %s' % (self.school, self.subject, self.grade, self.date)

    def __add__(self, other):
        if self.subject == other.subject:
            return add_helper(self.grade + ' ' + other.grade)
        else:
            return 'Different subjects.  Cannot add.'
    
    

class Student:
    def __init__(self, name):
            self.name = name
            self.score_lst = []
            
    def add_score(self, score):
        self.score_lst.append(score)

    def __str__(self):
        s = self.name + ':\n'
        for x in self.score_lst:
            s += ' ' +x.__str__() + '\n'
        return s
        



english_score = Score('Shuguang Primary School', 'English', '110/120', '2019-06-30')
wyh = Student('Wang Yuheng')
wyh.add_score(english_score)
math_score = Score('Jinwai', 'Math', '119/120', '2018-3-01')
wyh.add_score(math_score)
math_score2 = Score('Jinwai', 'Math', '96/120', '2019-06-01')
print(math_score + math_score2)
