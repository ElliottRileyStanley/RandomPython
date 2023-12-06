old = open('Anagram\dictionary_defs.txt').readlines()
new = open('Anagram\organized_dictionary.text', "a")
print (len(old[0]))
for word in old:
    word = word.rsplit("\t")[0]
    if len(word) > 3 and len(word) < 10:
        new.write(word + "\n")
