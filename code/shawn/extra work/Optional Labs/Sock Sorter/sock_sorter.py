# Shawn Stolsig
# PDX Code Guild 
# Assignment: Optional Lab - Sock Sorter
# Date: 11/4/2019

import random

sock_types = ['ankle', 'crew', 'calf', 'thigh']

# generate list of random socks
sock_list = []
for i in range(1000):
    sock_list.append(random.choice(sock_types))

# put list of socks into dictionary
sock_dict = {}
for sock in sock_list:
    if not sock_dict.get(sock):
        sock_dict[sock] = 1
    else:
        sock_dict[sock] += 1
print(sock_dict)

# figure out how many pairs and duplicates of each sock
for sock in sock_dict:
    print(f"There are {int(sock_dict[sock])//2} pairs of {sock} and {int(sock_dict[sock]) % 2 } loaners.")
