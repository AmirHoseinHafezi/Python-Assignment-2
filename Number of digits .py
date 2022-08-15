
num = int(input('Enter the correct number: '))
end_counter = 0
O_counter = 0
E_counter = 0
while end_counter != 1:
    num1 = num % 10
    num //= 10
    if num1 % 2 == 0:
        E_counter += 1
    elif num1 % 2 != 0:
        O_counter += 1
    if num == 0:
        if O_counter > E_counter:
            print('Number of digits is odd')
        elif E_counter > O_counter:
            print('Number of digits is even')
        elif E_counter == O_counter:
            print('The number of odd and even digits is equal')
        end_counter = 1