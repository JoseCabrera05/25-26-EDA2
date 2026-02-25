# En una lista, sumar elementos en posiciones pares

## Analisis recursivo

- Entrada: `lista` de numeros (indices desde 0).
- Salida: suma de elementos en posiciones pares (0, 2, 4...).
- Caso base: lista vacia -> 0.
- Caso recursivo: sumar `lista[0]` y avanzar dos posiciones.
  - Si solo hay un elemento, se suma y termina.

## Seudocodigo

```text
funcion sumaPosicionesPares(lista)
    si lista es vacia
        retornar 0
    si longitud(lista) == 1
        retornar lista[0]
    return lista[0] + sumaPosicionesPares(lista[2..fin])
```
