def anti_vowel(text):
    word = ""
    for char in text:
        if not char in "aeiouAEIOU":
            word += char
    return word