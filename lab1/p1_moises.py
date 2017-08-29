io = ['q0', 'q1', 'q2', 'q3', 'qerror']
word = str(input("Ingrese una palabra: "))
a = 0
b = 0
status = 1
e2 = io[b]
while (a < len(word) and status == 1):
    if word[a]=='a' and e2 != io[len(io)-1]:
        e1 = e2
        print("")
        print("Estoy en: ", e1)
        print("Me llego una: ", word[a])
        print("Me quedo en: ", e2)
    elif word[a]=='b' and e2!=io[len(io)-1]:
        b = b + 1
        e1 = e2
        e2 = io[b]
        print("")
        print("Estoy en: ", e1)
        print("Me llego una: ", word[a])
        print("Me quedo en: ", e2)
    elif e2==io[len(io)-1]:
        status = 2
        e1 = e2
        e2 = 'error'
    else:
        status = 0
        e1 = e2
        e2 = 'Letra no definida'
    a = a + 1

if status == 0:
    print("La palabra no pertenece a este alfabeto.")
elif status == 2:
    print("Se llegó al nodo de error")
else:
    print("La palabra pertenece a este alfabeto.")
