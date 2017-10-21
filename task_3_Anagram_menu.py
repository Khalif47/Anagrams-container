from task_3_Anagram import Anagram


def menu():
    test = Anagram()
    while True:
        print('-----------------Anagram Checker---------------------------\n\n\n\n')
        print('1. Add Word\n')
        print('2. Search\n')
        print('3. Print\n')
        print('4. Read file\n')
        print('5. Quit\n')
        command = int(input('Enter your choice\n'))
        if command == 1:
            word = input('Enter a word\n')
            test.add_word(word)
        if command == 2:
            word = input('Enter a word to search\n')
            print(test.query(word))

        if command == 3:
            test.print()
        if command == 4:
            filer = input('Enter file to read\n')
            test.file_read(filer)
        if command == 5:
            break


menu()
