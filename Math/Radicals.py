a, d = input(), input()
b = 1
for x in range(2,int(round((int(a)/2), 0))):
    if round(int(a)/pow(int(x),int(d)), 0) == int(a)/pow(int(x),int(d)):
        b *= int(x)
        a = round(int(a)/pow(int(x),int(d)),0)
        print(str(b)+" times radical "+str(a))