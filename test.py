import numpy as np

a = np.array([1,2,3,4,5])
print(type(a))
if type(a) == 'numpy.ndarray':
    print('wohoo')
else:
    print('sjit')


if type(a) == type(np.zeros(2)):
    print('im a baws')

b = 5
c = 5.5
if type(b) == type(2): 
    print('int bruv')

def chek(B):
    if type(B) == type(2) or type(2.1): 
        print('master mind')


chek(b)
chek(c)

arr = np.array([1,2,3,4])
lis = (1,2,3,4)

print('arr' , type(arr))
print('lis', type(lis))
print(arr*3)
print(lis+lis)