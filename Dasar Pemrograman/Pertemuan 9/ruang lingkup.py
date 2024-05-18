#Variabel Global
total = 0

def sum( arg1, arg2 ):
    total = arg1 + arg2;
    print("Di dalam fungsi nilai total : ", total)
    return total

sum( 10, 20 )
print ("Di luar fungsi, nilai total : ", total )