# A = 97 Z = 122

a = list(str("rambB zen").lower())
print(a)

b = ['e', 'n', 'z','o','b',' ', 'm', 'r', 'a'] 

encrypted_list = []

def rot_encrypt(lst, rot):
    global encrypted_list
    for i in lst:
        b = int(str(ord(i) + rot))
        while b > 122:
            b -= 26
        if b - rot == 32:
            b = 32
        encrypted_list.append(chr(b))
   
rot_encrypt(a, 13)
print(encrypted_list, "First encrypt")
encrypted_list.clear()

rot_encrypt(b, 13)
print(encrypted_list, "Second decrypt")

listToStr = ''.join([str(elem) for elem in encrypted_list]) 

print(listToStr)


