un= 'amir hosein'
pw = 98457

username = input('Enter username:')
password = int(input("Enter password:"))
if un == username and pw == password :
    print('Acceptable')
elif un != username and pw != password:
    print('Unacceptable')


