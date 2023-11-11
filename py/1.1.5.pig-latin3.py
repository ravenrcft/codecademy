pyg = 'ay'

original = raw_input('Enter a word:').lower()

if len(original) > 0 and original.isalpha():
    print original
else:
    print 'empty'

word = original
first = word[0]

print word 
print first