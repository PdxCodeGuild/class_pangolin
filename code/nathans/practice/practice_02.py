## practice_02.py
 
def pos_neg(a, b):
    if a < 0 and b < 0:
        return False

    if a > 0 and b > 0:
            return False

    if a == 0 or b == 0:
            return False               

    else:
        return True 

print(pos_neg(0, 2))
