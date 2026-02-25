# Contar las cifras de un numero

## Analisis recursivo

- Entrada: `n` entero (puede ser negativo).
- Salida: cantidad de cifras decimales.
- Caso base: `n` entre 0 y 9 -> 1.
- Caso recursivo: `f(n) = 1 + f(n / 10)` con division entera sobre `abs(n)`.

## Seudocodigo

```text
funcion contarCifras(n)
    n = abs(n)
    si n < 10
        retornar 1
    retornar 1 + contarCifras(n / 10)
```
