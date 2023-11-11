def censor(text, word):
    words = text.split()
    for i in range(len(words)):
        if words[i] == word:
            words [i] = "*" * len(word)
    return " ".join(words)