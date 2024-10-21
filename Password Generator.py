import random

abc = 'qwertzuiopasdfghjklyxcvbnm'
extras = '0123456789#_!*&$%§?.,'
new_password = ''
for i in range(16):
    x = random.randint(1,2)
    if x == 1:
        new_password += abc[random.randint(0,25)]
    else:
        new_password += extras[random.randint(0,20)]
print(new_password)