import random

class Password:
    class Generator:
        def __init__(self, end, companyName, lengthOfKeyword):
            self.end = end
            self.companyName = companyName
            self.lengthOfKeyword = lengthOfKeyword

        def genRandomString(self):
            letters = ['a', 'B', 'c', 'D', 'e', 'F', 'g', 'H', 'i', 'J', 'k', 'L', 'm', 'N', 'o', 'P', 'q', 'R', 's', 'T', 'u', 'V', 'w', 'X', 'y', 'Z']
            keyword = ''
            for i in range(int(self.lengthOfKeyword)): 
                letter = random.choice(letters)

                keyword = keyword + letter

            return str(keyword)
        
        def compilePassword(self):
            keyword = self.genRandomString()
            firstCompanyLetter = str(self.companyName[0])
            
            password = firstCompanyLetter + keyword + self.end
            
            return str(password)
