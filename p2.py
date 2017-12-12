if __name__ == "__main__":
    status = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'error']
    word = str(input("Ingrese una palabra: "))
    s = status[0] #Estado actual
    i = 0

    while(i < len(word) and s != 'error'):
        if (word[i] != 'a' and word[i] != 'b'):
            s = status[6]
        else:
            if s == 'q0':
                if word[i] == 'a':
                    s = status[1]
                elif word[i] == 'b':
                    s = status[4]
            elif s == 'q1':
                if word[i] == 'a':
                    s = status[6]
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
                    s = status[6]
            elif s == 'q4':
                if word[i] == 'a':
                    s = status[4]
                elif word[i] == 'b':
                    s = status[5]
            elif s == 'q5':
                if word[i] == 'a':
                    s = status[5]
                elif word[i] == 'b':
                    s = status[6]

        print("Entrada: ", word[i])
        print("Estado actual: ", s)
        i = i + 1

    if (s == 'q3' or s == 'q5'):
        print("La palabra pertenece al diccionario.")
    else:
        print("La palabra no pertenece al diccionario.")
