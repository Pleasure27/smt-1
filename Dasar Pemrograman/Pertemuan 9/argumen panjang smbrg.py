def print_info( arg1, *vartuple ):
    print("Outputnya adalah : ")
    print(arg1)
    for var in vartuple:
        print (var)
        
print_info( 10 )

print_info( 10, 30, 50, 70 )
