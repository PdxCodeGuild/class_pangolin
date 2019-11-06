keys = ['name', 'movie', 'color']
values = ['al', 'edge of tomorrow', 'sunset orange']
tups = [(keys[i], values[i]) for i in range(min(len(keys), len(values)))]
print('tuple list from comp:'.rjust(35), tups)
print('dictionary made from tuple list:'.rjust(35),dict(tups))
tups = list(zip(keys, values))
print('tuple list from zip:'.rjust(35), tups)
print('dictionary made from tuple list:'.rjust(35),dict(tups))
print('dictionary made from dict comp with zip:'.rjust(35), {k:v for k, v in zip(keys, values)})
'''
>>> def al_add(num1, num2):   
...     output = print(num1 + num2)
...     return output                                         
>>> al_add(3, 5)                                        
8  
>>> al_add(3, 5) + 2
8
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
>>> None
>>>
>>> my_var = 2 + 3
>>> print(my_var)
5
>>> my_var = 2 == 3
>>> print(my_var)
False
>>>
>>> import string
>>> abc_list = list(string.ascii_lowercase)
>>> abc_list
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
>>> [let.append('a') for let in abc_list]
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "<stdin>", line 1, in <listcomp>
AttributeError: 'str' object has no attribute 'append'
>>>
>>> list_of_lists = [string.ascii_lowercase[i:i+3] for i in range(0, len(string.ascii_lowercase), 3)]
>>> list_of_lists
['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']
>>>
>>> list_of_lists = [list(string.ascii_lowercase[i:i+3
    ]) for i in range(0, len(string.ascii_lowercase), 3)]
>>>
>>> list_of_lists
[['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r'], ['s', 't', 'u'], ['v', 'w', 'x'], ['y', 'z']]
>>> list_of_lists[2][1]
'h'
>>> list_of_lists[4].update(['a'])
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'update'
>>> list_of_lists[4].extend(['a'])
>>> list_of_lists
[['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o', 'a'], ['p', 'q', 'r'], ['s', 't', 'u'], ['v', 'w', 'x'], ['y', 'z']]
>>> list_of_lists[3][0].extend(['a'])
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'extend'
>>> list_of_lists.extend([['?', '&']])
>>> list_of_lists
[['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o', 'a'], ['p', 'q', 'r'], ['s', 't', 'u'], ['v', 'w', 'x'], ['y', 'z'], ['?', '&']]
>>>
>>> maplist = [{0:'a'}, {1:'b'}]
>>> maplist[0][0] = 'z'
>>> maplist
[{0: 'z'}, {1: 'b'}]
>>> dict([(0,'a'), (1, 'b')])
{0: 'a', 1: 'b'}
>>> tuple_list = []
>>> tuple_list.append(('name': 'terry'))
File "<stdin>", line 1
tuple_list.append(('name': 'terry'))
SyntaxError: invalid syntax
>>> tuple_list.append(('name', 'terry'))
>>>
>>> tuple_list = []
>>> tuple_list.append(('name', 'terry'))~
File "<stdin>", line 1
tuple_list.append(('name', 'terry'))~
>>> tuple_list.append(('name', 'terry'))
>>>
>>> tuple_list = []
>>> tuple_list.append(('name', 'terry'))
>>> tuple_list.append(('movie', 'inception'))
>>> tuple_list.append(('color', 'blue'))
>>> tuple_list
[('name', 'terry'), ('movie', 'inception'), ('color', 'blue')]
>>> dict(tuple_list)
{'name': 'terry', 'movie': 'inception', 'color': 'blue'}
>>> {key: value for key, value in tuple_list}
{'name': 'terry', 'movie': 'inception', 'color': 'blue'}
>>>
>>> keys = ['name', 'movie', 'color']
>>> values = ['terry', 'inception', 'blue']
>>> zip(keys, values)
<zip object at 0x7f37a1684c08>
>>> list(zip(keys, values))
[('name', 'terry'), ('movie', 'inception'), ('color', 'blue')]
>>> dict(zip(keys, values))
{'name': 'terry', 'movie': 'inception', 'color': 'blue'}
'''