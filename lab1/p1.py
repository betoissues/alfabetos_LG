if __name__ == "__main__":
    status = ['q0', 'q1', 'q2', 'q3', 'error']
    word = str(input("Ingrese una palabra: "))
    s = status[0] #Estado actual
    i = 0

    while(i < len(word) and s != 'error'):
        if (word[i] != 'a' and word[i] != 'b'):
            s = status[4]
        else:
            if s == 'q0':
                if word[i] == 'a':
                    s = status[0]
                elif word[i] == 'b':
                    s = status[1]
            elif s == 'q1':
                if word[i] == 'a':
                    s = status[1]
                elif word[i] == 'b':
                    s = status[2]
            elif s == 'q2':
                if word[i] == 'a':
                    s = status[2]
                elif word[i] == 'b':
                    s = status[3]
            elif s == 'q3':
                if word[i] == 'a':
                    s = status[3]
                elif word[i] == 'b':
                    s = status[4]

        print("Entrada: ", word[i])
        print("Estado actual: ", s)
        i = i + 1

    if (s == 'q0'):
        print("La palabra pertenece al diccionario.")
    else:
        print("La palabra no pertenece al diccionario.")
