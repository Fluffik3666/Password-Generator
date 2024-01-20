import passwordGen

def main():
    print('Welcome to the password generator! \n')
    print('How long should the keyword be?')
    lengthOfKeyword = str(input())
    print('What should go at the end of your password?')
    end = str(input())
    print('What is the name of the company that you are using this password for?')
    companyName = str(input())
    print('Starting generation...')
    
    passwordGenerator = passwordGen.Password.Generator(end, companyName, lengthOfKeyword)
    
    print(str(passwordGenerator.compilePassword()))
    
    print('Make sure to keep this passord safe and not share it with anybody!')
    
    
if __name__ == '__main__':
    main()

