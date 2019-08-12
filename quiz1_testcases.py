# We do Test Driven Development (TDD). 测试驱动开发
# Please run this script in the command line using the following command:
#
#   pip3 install pytest --user
#
#   python -m pytest quiz1_testcases.py


from remove_punctuation2 import remove_punctuation2


def test_remove_punctuation_01():
    assert remove_punctuation2('') == ''
    
def test_remove_punctuation_02():
    assert remove_punctuation('.') == ''
    
def test_remove_punctuation_03():
    assert remove_punctuation(',') == ''

def test_remove_punctuation_04():
    assert remove_punctuation('apple.') == 'apple'

def test_remove_punctuation_05():
    assert remove_punctuation(', apple') == 'apple'

def test_remove_punctuation_06():
    assert remove_punctuation(',apple.') == 'apple'
    
def test_remove_punctuation_07():
    assert remove_punctuation(', apple.') == 'apple'

def test_remove_punctuation_08():
    assert remove_punctuation('apple .') == 'apple'

def test_remove_punctuation_09():
    assert remove_punctuation(None) == None
    
def test_remove_punctuation_10():
    assert remove_punctuation('apple..') == 'apple'

def test_remove_punctuation_11():
    assert remove_punctuation('you\'re') == 'you\'re'

def test_remove_punctuation_12():
    assert remove_punctuation('\'you\'re') == 'you\'re'

def test_remove_punctuation_13():
    assert remove_punctuation('you\'re\'') == 'you\'re' 
