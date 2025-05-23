def check(word):
    while(len(word) != 0):
        if word[0] in symbols:
            word = word[1:]
        elif word[0:2] in symbols:
            word = word[2:]
        else:
            return False
    return True


words = open(r'Dictionary.txt').readlines()
for i in range(len(words)):
    words[i] = words[i][0:-1]

symbols = ["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"]
for i in range(len(symbols)):
    symbols[i] = symbols[i].lower()

count = 0

for word in words:
    if check(word):
        count += 1

print(count)
print(count/len(words))