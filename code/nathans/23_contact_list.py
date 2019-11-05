#23_contact_list.py
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
# print(lines[0])
#### header keys in a list
lines_2 = lines[0].replace(',', ' ')
lines_3 = lines[1].split(',')
lines_4 = lines[2].split(',')
lines_5 = lines[3].split(',')
headers = lines_2.split()
# print(lines_3)
# for i in lines:
#     if i in lines[0]:
#         lines_2.append(i)
# print(headers)
# my_dict = {}
# for i in headers:
#     my_dict = i
# print(my_dict)
#### zips header list with first list
name_to_value_dict = dict(zip(headers, lines_3))
name_to_value_dict_2 = dict(zip(headers, lines_4))
name_to_value_dict_3 = dict(zip(headers, lines_5))
#### add small dict to big_dict
big_dict = {1:name_to_value_dict,
            2:name_to_value_dict_2,
            # 3:name_to_value_dict_3
            }
big_dict[3] = name_to_value_dict_3
print(big_dict)

# print(name_to_value_dict)
# print(name_to_value_dict_2)
# print(name_to_value_dict_3)

# test_dic = set(test_dict)
# print(name_to_value_dict)
# print(name_to_value_dict)




    # print(lines)
#### This will make a list of each row
# dict_list = []
# dict_list_2 = []
# for line in range(0, 4):
#     dict_list.append(line)
    # for j in dict_list:
    #     dict_list_2.append(dict_list[0])
# print(dict_list)
# headers = dict_list[0]
# print(headers)
# dict_dict = {}
# for i in dict_list:
#     dict_dict[i] = 0
# print(dict_list_2) 

    # mydict = {rows[1]:rows[5] for rows in lines}
    # print(mydict)
#### Get the header keys
# my_dict = {}
# headers = []

# for items in range(1):
#     headers.append(lines[0][::])
# print(headers)
# for i in headers:
#     headers_2.append(headers)
# print(headers_2[int(i)])
    

# dict_loop = {}
# for items, values in lines:
#     dict_loop[items] = values


#### use headers to make dictionary keys
#### import all values into dictionary



# headers = []
# headers_2 = []
# for i in lines:
#     headers.append(i)
#     for j in headers:
#         headers_2.append(j)
# print(headers_2)
