num = int(input('Enter a Number: '))

reversed_num = 0
num1 = num

while num1 != 0:
    reversed_num = num1 % 10 + (10 * reversed_num)
    num1 //= 10
if num == reversed_num:
    print('The number is equal to its maxim')
else:
    print('The number is not equal to its maxim.')
