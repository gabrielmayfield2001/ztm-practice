from collections import Counter, defaultdict, OrderedDict

li = [1, 2, 3, 4, 5, 6, 7, 7]
print(Counter(li))


dictionary = defaultdict(lambda:'does not exist',{
    'a': 1,
    'b': 2
})

print(dictionary['c'])


d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

print(d == d2)