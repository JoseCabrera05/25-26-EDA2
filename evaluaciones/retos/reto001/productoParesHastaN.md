# Producto de pares hasta n

## Analisis recursivo

- Entrada: `n` entero >= 0.
- Salida: producto de los numeros pares entre 2 y `n` (incluye `n` si es par). Para `n < 2`, el producto es 1.
- Caso base: `n < 2` -> 1.
- Caso recursivo:
  - Si `n` es par: `f(n) = n * f(n - 2)`.
  - Si `n` es impar: `f(n) = f(n - 1)` (baja al par anterior).

## Seudocodigo

```text
funcion productoPares(n)
    si n < 2
        retornar 1
    si n % 2 != 0
        retornar productoPares(n - 1)
    retornar n * productoPares(n - 2)
```
