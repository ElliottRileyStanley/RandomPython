old = open(r'Anagram\dictionary_defs.txt').readlines()
new = open(r'C:\Users\Ellio\OneDrive\Desktop\Python\Random\Dictionary.txt', "a")
for word in old:
    word = word.rsplit("\t")[0]
    new.write(word.lower() + "\n")
