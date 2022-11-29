words = ["hello", "hey", "yo", "yello"]

def print_upper_words(words, letter):
    for word in words:
        if word.startswith(letter):
            print(word.upper())

print_upper_words(words, "y")