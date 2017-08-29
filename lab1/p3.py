if __name__ == "__main__":
    status = ['s1', 's2', 'error']
    word = str(input("Ingrese una palabra (1,0): "))
    s = status[0] #Estado actual
    i = 0

    while(i < len(word) and s != 'error'):
        if (word[i] != '1' and word[i] != '0'):
            s = status[3]
        else:
            if s == 's1':
                if word[i] == '0':
                    s = status[1]
                elif word[i] == '1':
                    s = status[0]
            elif s == 's2':
                if word[i] == '0':
                    s = status[0]
                elif word[i] == '1':
                    s = status[1]

        print("Entrada: ", word[i])
        print("Estado actual: ", s)
        i = i + 1

    if (s == 's1'):
        print("La palabra pertenece al diccionario.")
    else:
        print("La palabra no pertenece al diccionario.")
