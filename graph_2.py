# Representación de un grafo con un alfabeto definido por a, b
# Determina si la palabra introducida es parte del alfabeto. Para ver la tabla
# del grafo, dirigirse al README.md

def main():
    word = str(input("Ingrese una palabra: "))
    paths = {'q0': lambda letter: 'q1' if letter == 'a' else 'q4',
            'q1': lambda letter: 'Error' if letter == 'a' else 'q2',
            'q2': lambda letter: 'q2' if letter == 'a' else 'q3',
            'q3': lambda letter: 'q3' if letter == 'a' else 'Error',
            'q4': lambda letter: 'q4' if letter == 'a' else 'q5',
            'q5': lambda letter: 'q5' if letter == 'a' else 'Error'
            }
    s = 'q0' #Estado actual

    for letter in word:
        if letter not in ['a', 'b'] or s == 'Error':
            print("No pertenece al diccionartio")
            break
        else:
            s = paths[s](letter)

        print("Entrada: ", str(letter))
        print("Estado actual: ", s)

if __name__ == "__main__":
    main()
