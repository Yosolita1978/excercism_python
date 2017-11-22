def is_isogram(string):
    word_lower = list(string.lower())
    for char in word_lower:
        if char.isalpha():
            if word_lower.count(char) > 1:
                return False
    return True
