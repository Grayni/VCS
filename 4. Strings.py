# Output of strings
string = input('Enter string: ')
lst = string.split()

for i, word in enumerate(lst):
    print(f'{i+1}. {word[:10]}')
