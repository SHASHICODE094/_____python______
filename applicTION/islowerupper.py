print('Check if word is Upper or Lower.')
word = input('Enter the word')
# if(word.lower()):
#   print('true')
# else:
#   print('false')
if word.isupper():
    print('WORD IS IN UPPERCASE!')
elif word.islower():
    print('word is in lowercase')   
else :
    print('Word is in Mixeds')