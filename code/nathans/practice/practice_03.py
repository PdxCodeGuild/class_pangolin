#practice_03.py

def within(a):
    if a > 109:
        return False    
    if a <= 90:
        return False    
    else:
        return True


print(within(110))
