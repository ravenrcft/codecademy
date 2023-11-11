def reverse(text):
    length = len(text)
    length = length - 1
    playback = ""
    while length >= 0:
        playback += text[length]
        length -= 1
    return playback

print reverse("abcdefghijklmnopqrstuvwxyz")