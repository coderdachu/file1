x = input('enter anything: ')
y = input('which character do you want:')
z = x[int(y)-1]
if int(y) > len(x):
 print(z)
else:
 print('character value is higher than length of sentence')