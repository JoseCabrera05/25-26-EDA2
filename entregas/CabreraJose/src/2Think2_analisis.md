# 2Think²: Pruebas del Algoritmo Diagonal

## Matriz de Referencia
```
 2   5   9  14  21
 4   7  11  17  25
 8  12  15  20  30
13  18  22  27  35
19  24  28  33  40
```

## Prueba 1: Buscando 21

**Posición esperada**: Fila 0, Columna 4 (esquina superior-derecha de la diagonal)

**Traza del algoritmo desde esquina superior-izquierda (0,0) moviéndose diagonalmente:**

1. (0,0): 2 < 21 → Comparación 1
2. (1,1): 7 < 21 → Comparación 2
3. (2,2): 15 < 21 → Comparación 3
4. (3,3): 27 > 21 → Comparación 4 (cambiar dirección)
5. (2,3): 20 < 21 → Comparación 5 (buscar hacia arriba-derecha)
6. (1,3): 17 < 21 → Comparación 6
7. (0,3): 14 < 21 → Comparación 7
8. (0,4): 21 = 21 → Comparación 8 ✓ **ENCONTRADO**

**Total: 8 comparaciones** (mejor caso)

---

## Prueba 2: Buscando 16

**Estado esperado**: No existe en la matriz

**Traza del algoritmo desde esquina superior-izquierda (0,0):**

1. (0,0): 2 < 16 → Comparación 1
2. (1,1): 7 < 16 → Comparación 2
3. (2,2): 15 < 16 → Comparación 3
4. (3,3): 27 > 16 → Comparación 4 (cambiar dirección)
5. (2,3): 20 > 16 → Comparación 5 (subir)
6. (1,3): 17 > 16 → Comparación 6 (subir)
7. (0,3): 14 < 16 → Comparación 7 (mover derecha)
8. (0,4): 21 > 16 → Comparación 8 (volver atrás)
9. Verificar zona intermedia (0,2)-(1,2)
10. (0,2): 9 < 16 → Comparación 9
11. (1,2): 11 < 16 → Comparación 10

**Total: 10 comparaciones** (peor caso)

**Resultado**: 16 no existe en la matriz

---

## Análisis: ¿Arrancar del Centro vs Arrancar de la Esquina?

### Comparación de Estrategias

**Estrategia 1: Arrancar de esquina superior-izquierda (0,0)**
- Ventaja: Fácil de implementar
- Desventaja: Puede requerir búsquedas extensas en matrices grandes

**Estrategia 2: Arrancar del Centro (2,2)**
Buscando 16 desde el centro:
1. (2,2): 15 < 16 → Comparación 1 (buscar derecha)
2. (2,3): 20 > 16 → Comparación 2 (buscar arriba)
3. (1,3): 17 > 16 → Comparación 3 (buscar arriba)
4. (0,3): 14 < 16 → Comparación 4 (buscar derecha)
5. (0,4): 21 > 16 → Comparación 5 (buscar izquierda)
6. (0,2): 9 < 16 → Comparación 6
7. (1,2): 11 < 16 → Comparación 7

**Total desde centro: 7 comparaciones** vs **10 comparaciones desde esquina**

### Conclusión

**SÍ existe un caso concreto donde arrancar del centro es mejor:**
- **Valor 16** requiere 10 comparaciones desde esquina pero solo 7 desde el centro
- El centro proporciona una "mejor proximidad" a valores que están distribuidos en la matriz
- Para matrices grandes, arrancar del centro puede reducir tiempo promedio

**Recomendación**: Un algoritmo híbrido que comience del centro sería más eficiente que comenzar siempre de la esquina.
