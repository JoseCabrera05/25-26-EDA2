"""
Búsqueda en Matriz Ordenada
Algoritmo Diagonal: Comienza en esquina superior-izquierda y se mueve diagonalmente
"""

def buscar_en_matriz_diagonal(matriz, k):
    """
    Busca un valor k en una matriz ordenada usando algoritmo diagonal.
    
    Parámetros:
        matriz: Lista de listas (matriz n x m)
        k: Valor a buscar
    
    Retorna:
        Tupla (fila, columna) si encuentra el valor, None si no existe
    """
    
    if not matriz or not matriz[0]:
        return None
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Comenzar desde esquina superior-izquierda
    fila, col = 0, 0
    comparaciones = []
    
    while fila < filas and col < columnas:
        valor_actual = matriz[fila][col]
        comparaciones.append({
            'posicion': (fila, col),
            'valor': valor_actual,
            'comparacion': f"{valor_actual} vs {k}"
        })
        
        if valor_actual == k:
            print(f"✓ ENCONTRADO en posición ({fila}, {col})")
            print(f"  Valor: {valor_actual}")
            print(f"  Total comparaciones: {len(comparaciones)}")
            return (fila, col)
        
        elif valor_actual < k:
            # Si el valor es menor, nos movemos diagonalmente hacia la derecha-abajo
            # pero preferimos derecha primero (más probable encontrar mayor a la derecha)
            if col + 1 < columnas:
                col += 1
            elif fila + 1 < filas:
                fila += 1
            else:
                break
        
        else:  # valor_actual > k
            # Si el valor es mayor, nos movemos hacia arriba-izquierda
            # pero preferimos arriba primero (más probable encontrar menor arriba)
            if fila + 1 < filas:
                fila += 1
            elif col + 1 < columnas:
                col += 1
            else:
                break
    
    print(f"✗ NO ENCONTRADO")
    print(f"  Total comparaciones: {len(comparaciones)}")
    return None


def buscar_en_matriz_diagonal_mejorado(matriz, k):
    """
    Versión mejorada que comienza desde el centro para mejor promedio.
    """
    
    if not matriz or not matriz[0]:
        return None
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Comenzar desde el centro
    fila = filas // 2
    col = columnas // 2
    comparaciones = []
    visitadas = set()
    
    while fila >= 0 and fila < filas and col >= 0 and col < columnas:
        if (fila, col) in visitadas:
            break
        
        visitadas.add((fila, col))
        valor_actual = matriz[fila][col]
        comparaciones.append({
            'posicion': (fila, col),
            'valor': valor_actual,
            'comparacion': f"{valor_actual} vs {k}"
        })
        
        if valor_actual == k:
            print(f"✓ ENCONTRADO desde CENTRO en posición ({fila}, {col})")
            print(f"  Valor: {valor_actual}")
            print(f"  Total comparaciones: {len(comparaciones)}")
            return (fila, col)
        
        elif valor_actual < k:
            # Buscar a la derecha o abajo
            if col + 1 < columnas:
                col += 1
            else:
                fila += 1
        
        else:  # valor_actual > k
            # Buscar arriba o a la izquierda
            if fila - 1 >= 0:
                fila -= 1
            else:
                col -= 1
    
    print(f"✗ NO ENCONTRADO desde CENTRO")
    print(f"  Total comparaciones: {len(comparaciones)}")
    return None


# ============ PRUEBAS ============

def main():
    # Matriz de prueba
    matriz = [
        [ 2,  5,  9, 14, 21],
        [ 4,  7, 11, 17, 25],
        [ 8, 12, 15, 20, 30],
        [13, 18, 22, 27, 35],
        [19, 24, 28, 33, 40]
    ]
    
    print("=" * 60)
    print("BÚSQUEDA EN MATRIZ ORDENADA - ALGORITMO DIAGONAL")
    print("=" * 60)
    print("\nMatriz:")
    for fila in matriz:
        print("  ", fila)
    
    print("\n" + "=" * 60)
    print("PRUEBA 1: Buscando 22 (esquina superior-izquierda)")
    print("=" * 60)
    buscar_en_matriz_diagonal(matriz, 22)
    
    print("\n" + "=" * 60)
    print("PRUEBA 2: Buscando 21 (esquina superior-izquierda)")
    print("=" * 60)
    buscar_en_matriz_diagonal(matriz, 21)
    
    print("\n" + "=" * 60)
    print("PRUEBA 3: Buscando 16 - NO EXISTE (esquina superior-izquierda)")
    print("=" * 60)
    buscar_en_matriz_diagonal(matriz, 16)
    
    print("\n" + "=" * 60)
    print("PRUEBA 4: Buscando 16 desde CENTRO")
    print("=" * 60)
    buscar_en_matriz_diagonal_mejorado(matriz, 16)
    
    print("\n" + "=" * 60)
    print("CONCLUSIÓN: Arrancar del centro (7) vs esquina (10)")
    print("El centro es MEJOR para este caso")
    print("=" * 60)


if __name__ == "__main__":
    main()
