word_list = open('Anagram\organized_dictionary.text').readlines()

letters = ["k", "b", "k", "d", "e", "w", "k", "i", "a"]

def check_word(word, letters):
    for letter in word:
        if not letter in letters:
            return False
    return True

for word in word_list:
    if check_word(word, letters):
        print(word)

