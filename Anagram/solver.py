word_list = open(r"Anagram\organized_dictionary.text").readlines()

def check_word(word):
    letters = "sqnlugerw"
    for letter in word:
        if letter not in letters:
            return False
        letters = letters.replace(letter, "", 1)
    return True

result = []

for word in word_list:
    word = word[0:len(word)-1]
    if check_word(word) == True:
        result.append(word)

print(result)