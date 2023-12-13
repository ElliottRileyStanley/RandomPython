def is_word_possible(word, guesses, results):
    possible_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for word_index in range(0, len(guesses)):
        for letter_index in range(0, 4):
            if results[word_index][letter_index] == "b":
                if guesses[word_index][letter_index] in possible_letters:
                    possible_letters.remove(guesses[word_index][letter_index])
    
    print(word)
    for letter in range(0, 4):
        if word[letter] not in possible_letters:
            return False

    return True
                
def choice(guesses, results):
    possible_answers = open(r'Wordle\Answers.text').readlines()
    for word in range(0, len(possible_answers)-1):
        possible_answers[word] = possible_answers[word][:-1]

    for word_index in range(0, len(possible_answers)):
        if is_word_possible(possible_answers[word_index], guesses, results) == False:
            possible_answers.pop(word_index)
    
    return len(possible_answers)


print(choice([["a", "b", "a", "c", "k"], ["s", "h", "o", "o", "t"]], [["b", "b", "b", "b", "b"], ["g", "b", "b", "b", "b"]]))