def joinList(lst):
    if len(lst) <= 0:
        return ''
    if len(lst) == 1:
        return lst[0]
    return ', '.join(lst[:-1]) + ', and ' + lst[-1]

spam = ['apples', 'bananas', 'tofu', 'cats', 'jun']
print(joinList(spam))