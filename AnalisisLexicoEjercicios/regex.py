import re

opcion = 0
while opcion != 6:

    print("\nSelecion un Opcion")
    print("1.-Variables Validas")
    print("2.-Enteros y decimales")
    print("3.-Operadores Aritmeticos")
    print("4.-Operadores Relacionales")
    print("5.-Palabras Reservadas")
    print("6.-PARA SALIR")

    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        filename = "loremipsum.txt"
        textfile = open(filename, "r")
        regex = "\VAR|var\s\w+(\d\w)*"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 2:
        filename = "loremipsum.txt"
        textfile = open(filename, "r")
        regex = "\d+(\.\d+)?"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 3:
        filename = "loremipsum.txt"
        textfile = open(filename, "r")
        regex = "(\+)|(-)|(\*)|(/)"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 4:
        filename = "loremipsum.txt"
        textfile = open(filename, "r")
        regex = "(=)|(!)|(<)|(>)"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 5:
        filename = "loremipsum.txt"
        textfile = open(filename, "r")
        regex = "(main|MAIN)|(void|VOID)|(int|INT)|(print|PRINT)"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    else:
        print("GRACIAS POR HABER USADO EL PROGRAMA")