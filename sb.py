def create_table():
    SPACE = ' '
    L_S = '0abcdefghij '
    
    f = [[i if j * i == 0 else SPACE for j in range(12)] for i in range(12)]
    f[0] = [L_S[i] for i in range(12)]

    for l in f:
        print(l)

        

print(create_table())
