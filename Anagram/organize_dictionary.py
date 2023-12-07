old = open(r'Anagram\dictionary_defs.txt').readlines()
new = open(r'Anagram\organized_dictionary.text', "a")
for word in old:
    word = word.rsplit("\t")[0]
    if len(word) > 3 and len(word) < 10:
        new.write(word.lower() + "\n")
