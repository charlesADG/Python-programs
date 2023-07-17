
myDict = {}

def searchBirthday():
    print('Search a Brithday')
    name = input('Enter a name: ')
    if name in myDict.keys():
        print('Result', myDict[name])
    
def addBirthday():
    print('Add a new Birthday')
    name = input('Enter a name: ')
    birthday = input('Enter a Birthday: ')
    myDict[name] = birthday

def changeBirthday():
    print('Change a Birthday')
    name = input('Enter a name you want to change the birthday: ')
    if name in myDict.keys():
        newBirthday = input('Enter a new Birthday: ')
        myDict[name] = newBirthday

def deleteBirthday():
    print('Delete a Birthday')
    name = input('Enter a name: ')
    del myDict[name]

def printDictionary():
    print(myDict)
    
def main():
    print('''Friends and Their Birthdays
------------------------------
1. Search a Birthday
2. Add a new Birthday
3. Change a Birthday
4. Delete a Birthday
5. Print the Dictionary
6. Quit the Program
''')
    ans = 'y'
    while ans.lower() == 'y':
        choice = int(input('Enter your choice: '))
        if choice == 1:
            searchBirthday()
            print()
            main()
        elif choice == 2:
            addBirthday()
            print()
            main()
        elif choice == 3:
            changeBirthday()
            print()
            main()
        elif choice == 4:
            deleteBirthday()
            print()
            main()
        elif choice == 5:
            printDictionary()
            print()
            main()
        elif choice == 6:
            exit()
            
        else:
            print('Invalid Input')
        
main()

