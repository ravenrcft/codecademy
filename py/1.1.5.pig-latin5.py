pyg = 'ay'

#original = raw_input('Enter a word:').lower()
original = "Albert".lower()

word = original
first = word[0]
new_word = word + pyg

if len(original) > 0 and original.isalpha():
    if first == "a":
        print(new_word)
    elif first == "e":
        print(new_word)
    elif first == "i":
        print(new_word)
    elif first == "o":
        print(new_word)
    elif first == "u":
        print(new_word)
    else:
        new_word = word[1:] + first + pyg
        print(new_word)
else:
    print('empty')