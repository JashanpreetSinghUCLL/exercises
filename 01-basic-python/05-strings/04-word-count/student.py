def word_count(string):
    if len(string) != 0:
        return len(string.split(" "))
    else:
        return 0


print(word_count("Jashan is cool hello"))