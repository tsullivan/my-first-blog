def unstrictName(name):
    print('Hi ' + name + '!')

unstrictName('Tim')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']

def strictName(name):
    if name in girls:
        print('Hi ' + name + '!')
    else:
        print('Hi anonymous!')

for name in girls:
    strictName(name)
    print('Next girl')

strictName('Tim')

for i in range(1, 6):
    print(i)
