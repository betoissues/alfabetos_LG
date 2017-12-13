# Representación de un grafo con un alfabeto definido por a, b
# Determina si la palabra introducida es parte del alfabeto. Para ver la tabla
# del grafo, dirigirse al README.md

def main():
    word = str(input("Ingrese una palabra: "))
    paths = {'q0': lambda letter: 'q0' if letter == 'a' else 'q1',
            'q1': lambda letter: 'q1' if letter == 'a' else 'q2',
            'q2': lambda letter: 'q2' if letter == 'a' else 'q3',
            'q3': lambda letter: 'q3' if letter == 'a' else 'Error'}
    s = 'q0' # Estado Actual

    for letter in word:
        if letter not in ['a', 'b'] or s == 'Error':
            print("No pertenece al diccionario")
            break
        else:
            s = paths[s](letter)

        print("Entrada: ", str(letter))
        print("Estado actual: ", s)

if __name__ == "__main__":
    main()
