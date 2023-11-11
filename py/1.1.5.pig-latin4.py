pyg = 'ay'

original = raw_input('Enter a word:').lower()

word = original
first = word[0]
new_word = word + first + pyg

if len(original) > 0 and original.isalpha():
    if first == "a":
        print new_word
    elif first == "e":
        print new_word
    elif first == "i":
        print new_word
    elif first == "o":
        print new_word
    elif first == "u":
        print new_word
    else:
        print "consonant"
else:
    print 'empty'