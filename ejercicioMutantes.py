def isMutant(dna):
    rows = len(dna)
    cols = len(dna[0])

    # Verifica si hay secuencias iguales en forma horizontal, vertical o diagonal
    def check_sequence(sequence):
        return 'AAAA' in sequence or 'TTTT' in sequence or 'CCCC' in sequence or 'GGGG' in sequence

    # Verifica si hay secuencias iguales en forma horizontal
    def check_horizontal(matrix):
        count = 0
        for row in matrix:
            for col in range(cols - 3):
                sequence = ''.join(row[col:col + 4])
                if check_sequence(sequence):
                    print(sequence)
                    count += 1
        return count
    count = check_horizontal(dna) 
    print(count)
    if count >= 2:
        return True
    else:
    # Verifica si hay secuencias iguales en forma vertical
        def check_vertical(matrix, count):
            for col in range(cols):
                for row in range(rows - 3):
                    sequence = ''.join(matrix[row + i][col] for i in range(4))
                    if check_sequence(sequence):
                        count += 1
            return count
        count2 = check_vertical(dna,count)
        print(count2)
        if count2 >= 2:
            return True
        else:
    # Verifica si hay secuencias iguales en forma diagonal (de izquierda a derecha)
            def check_diagonal(matrix, count):
                for row in range(rows - 3):
                    for col in range(cols - 3):
                        sequence = ''.join(matrix[row + i][col + i] for i in range(4))
                        if check_sequence(sequence):
                            count += 1
                return count
            count3 = check_diagonal(dna,count2)
            print(count3)
            if count3 >=2:
                return True
            else:
    # Verifica si hay secuencias iguales en forma diagonal (de derecha a izquierda)
                def check_reverse_diagonal(matrix, count):
                    for row in range(rows - 3):
                        for col in range(3, cols):
                            sequence = ''.join(matrix[row + i][col - i] for i in range(4))
                            if check_sequence(sequence):
                                count += 1
                    return count
                count4 = check_reverse_diagonal(dna,count3)
                print(count4)
                if count4 >= 2:
                    return True
                else:
                    return False
# Llamamos a la función
# Ejemplo de uso con una matriz 6x6
dna_example = [
    "ATGCTA",
    "CCGTGC",
    "TTATGT",
    "AGAAGG",
    "CCCCTA",
    "TCAAAA"
]
print("||| Bienvenido a GenomeSpy Ultra |||\nPor favor, siga las instrucciones:")
# Ingresar las filas de la matriz por teclado
#dna = [input(f"Ingrese la fila {i + 1} de la matriz: ").upper() for i in range(6)]

# Verificar si es mutante y mostrar el resultado
result = isMutant(dna_example)
print(result)
if result:
    print("ES mutante")
    print("Comienza fase de aislamiento...")
else:
    print("NO es mutante")