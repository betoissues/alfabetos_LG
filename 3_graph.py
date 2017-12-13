# Representación de un grafo con un alfabeto definido por 1, 0
# Determina si la palabra introducida es parte del alfabeto. Para ver la tabla
# del grafo, dirigirse al README.md

def main():
    word = str(input("Ingrese una palabra (1,0): "))
    paths = {'s1': lambda letter: 's2' if letter == '0' else 's1',
            's2': lambda letter: 's1' if letter == '0' else 's2'
            }
    s = 's1' #Estado actual

    for letter in word:
        if letter not in ['0', '1']:
            print("No pertenece al diccionario")
            break
        else:
            s = paths[s](letter)

        print("Entrada: ", str(letter))
        print("Estado actual: ", s)

if __name__ == "__main__":
    main()
