import string

[letter for letter in string.ascii_lowercase if letter not in 'aoeuiy'] 
# ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
[letter if letter not in 'aoeuiy' else '!' for letter in string.ascii_lowercase]
# ['!', 'b', 'c', 'd', '!', 'f', 'g', 'h', '!', 'j', 'k', 'l', 'm', 'n', '!', 'p', 'q', 'r', 's', 't', '!', 'v', 'w', 'x', '!', 'z']

[letter + '!' for letter in string.ascii_lowercase if letter not in 'aoeuiy']
#['b!', 'c!', 'd!', 'f!', 'g!', 'h!', 'j!', 'k!', 'l!', 'm!', 'n!', 'p!', 'q!', 'r!', 's!', 't!', 'v!', 'w!', 'x!', 'z!']
[letter + '!' if letter not in 'aoeuiy' else '?' for letter in string.ascii_lowercase]
# ['?', 'b!', 'c!', 'd!', '?', 'f!', 'g!', 'h!', '?', 'j!', 'k!', 'l!', 'm!', 'n!', '?', 'p!', 'q!', 'r!', 's!', 't!', '?', 'v!', 'w!', 'x!', '?', 'z!']


my_list = []
for num in range(10):
    my_list.append(num + 10)
 
my_list
 #[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
my_list2 = []
for num2 in my_list:
     my_list2.append(num2 - 100)
 
my_list2
#[-90, -89, -88, -87, -86, -85, -84, -83, -82, -81]
[num2 - 100 for num2 in [num + 10 for num in range(10)]]
#[-90, -89, -88, -87, -86, -85, -84, -83, -82, -81]