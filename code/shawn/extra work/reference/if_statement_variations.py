# good reference: https://stackoverflow.com/questions/2802726/putting-a-simple-if-then-else-statement-on-one-line

temp = 82
temp_toasty = False
temp_toasty_ternary = False
temp_toasty_compressed = False

########################## Ordinary Syntax   ##########################
if temp > 80: 
    temp_toasty = True
else:
    temp_toasty = False

############# Ternary operator / "conditional expressions" ###########
# syntax: condition_if_true if condition else condition_if_false
temp_toasty_ternary = True if temp > 80 else False

############ Ordinary syntax compressed to one line ##################
if temp > 80: temp_toasty_compressed = True 
else: False

######################################################################
print(temp_toasty)             # prints True
print(temp_toasty_ternary)     # prints true
print(temp_toasty_compressed)  # prints true