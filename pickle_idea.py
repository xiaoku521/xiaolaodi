# Purpose: dictionary & pickle as a simple means of database.
# Task: incorporate the functions into wordfreqCMD.py such that it will also show cumulative frequency.

import pickle


def lst2dict(lst, d):
    ''' 
    Store the information in list lst to dictionary d. 
    Note: nothing is returned.

    '''
    for x in lst:
        word = x[0]
        freq = x[1]
        if not word in d:
            d[word] = freq 
        else:
            d[word] += freq


def dict2lst(d):
    return list(d.items()) # a list of (key, value) pairs
        

def merge_frequency(lst1, lst2):
    d = {}
    lst2dict(lst1, d)
    lst2dict(lst2, d)
    return d


def load_record(pickle_fname):
    f = open(pickle_fname, 'rb')
    d = pickle.load(f)
    f.close()
    return d


def save_frequency_to_pickle(d, pickle_fname):
    f = open(pickle_fname, 'wb')
    pickle.dump(d, f)
    f.close()



if __name__ == '__main__':

    lst1 = [('apple',2),  ('banana',1)]
    d = {}
    lst2dict(lst1, d) # d will change
    save_frequency_to_pickle(d, 'frequency.p') # frequency.p is our database


    lst2 = [('banana',2), ('orange', 4)]
    d = load_record('frequency.p')
    lst1 = dict2lst(d)
    d = merge_frequency(lst2, lst1)
    print(d)
