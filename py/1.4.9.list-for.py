n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
    result = ""
    for rr in range(len(words)):
        result += words[rr]
    return result

print join_strings(n)