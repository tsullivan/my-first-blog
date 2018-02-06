print(True and True)
print(False and True)
print(True or 1 == 1)
print(1 != 2)

print('Hello, Django girls!')

if 3 > 2:
    print('3 is indeed greater than 2')
else:
    print('3 is not greater than 2')

name = 'Tim'
if name == 'Henry':
    print('Hey Henry!')
elif name == 'Tim':
    print('Hey Tim!')
else:
    print('Hey anonymous!')

volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")
