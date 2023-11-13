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
                        return True
    # Verifica si hay secuencias iguales en forma vertical
        def check_vertical(matrix, count):
            for col in range(cols):
                for row in range(rows - 3):
                    sequence = ''.join(matrix[row + i][col] for i in range(4))
                    if check_sequence(sequence):
                        return True

    # Verifica si hay secuencias iguales en forma diagonal (de izquierda a derecha)
        def check_diagonal(matrix, count):
            for row in range(rows - 3):
                for col in range(cols - 3):
                    sequence = ''.join(matrix[row + i][col + i] for i in range(4))
                    if check_sequence(sequence):
                        return True

    # Verifica si hay secuencias iguales en forma diagonal (de derecha a izquierda)
        def check_reverse_diagonal(matrix, count):
            for row in range(rows - 3):
                for col in range(3, cols):
                    sequence = ''.join(matrix[row + i][col - i] for i in range(4))
                    if check_sequence(sequence):
                        return True

# Ejemplo de uso con una matriz 6x6
dna_example = [
    "AAAACG",
    "CCTTGC",
    "AAAAAT",
    "TTGCTG",
    "CGCTCC",
    "AATAAA"
]

result = isMutant(dna_example)
print(result)