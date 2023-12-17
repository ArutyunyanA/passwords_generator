import string
from secrets import choice

def passwordGen(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(choice(alphabet) for char in range(length))

def saveToFile(passwords, filename='passwords.txt'):
    with open(filename, 'w') as txt_file:
        for password in passwords:
            txt_file.write(password + '\n')

def main(user_input=''):
    while user_input.lower() != 'exit':
        user_input = input('Please, choose the length of passwords (10, 12, 15).\nTo terminate programe, please type "exit": ')
        if user_input.isdigit():
            length = int(user_input)
            if length in [10, 12, 15]:
                passwords = [passwordGen(length) for char in range(10)]
                for password in passwords:
                    print(password)
                save_option = input('Do you want to save this passwords to file? (yes/no): ')
                if save_option.lower() == 'yes':
                    saveToFile(passwords)
                    print(f'Passwords saved to "passwords.txt"')
            else:
                print('Error: Please enter a valid length (10, 12, 15).')
        elif user_input.lower() == 'exit':
            print('Goodbye!, Have fun!')
        else:
            print('Error: Please enter a valid input.')
            
if __name__ == '__main__':
    main()