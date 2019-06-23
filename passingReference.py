def eggs(some_parameter):
    some_parameter.append('hello')

def bacon(some_parameter):
    some_parameter = 'ham'


spam = [1,2,3]
meat = 'beaf'

eggs(spam)
print(spam)

bacon(meat)
print(meat)
