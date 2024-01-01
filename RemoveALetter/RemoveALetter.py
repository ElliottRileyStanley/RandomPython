word_list = open(r'C:\Users\Ellio\OneDrive\Desktop\Python\Random\Dictionary.txt').readlines()
for word_index in range(0, len(word_list)):
    word_list[word_index] = word_list[word_index][:-1]


def remove_letter(word):
    result = []
    for letter in range(0, len(word)):
        result.append(word[:letter] + word[letter+1:])
    return result

def is_valid(word):
    removed_letters = remove_letter(word)
    for word in removed_letters:
        if word not in word_list:
            return False
    return True

valid_words = []
for word in word_list:
    if is_valid(word):
        print(word)
        valid_words.append(word)

print(valid_words)