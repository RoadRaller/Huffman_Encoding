INPUT_STR = 'didy on epstien island six seven tung tung tung sahur'

def collect(data):
    index = {}
    for letter in data:
        if letter in index:
            index[letter] += 1
        else:
            index[letter] = 1
    return index


def max_lst(lst):
    big = lst[0][1]
    big_ind = 0
    for item in lst:
        if item[1] > big:
            big = item[]

def sort_dict(index):
    lst = []
    for key in index:
        sublst = [key,index[key]]
        lst.append(sublst)
    
    for i in range(len(lst)):


    
    




index = collect(INPUT_STR)
print(sort_dict(index))

