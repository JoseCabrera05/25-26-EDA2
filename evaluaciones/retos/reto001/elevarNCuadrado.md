# Elevar n al cuadrado

## Analisis recursivo

- Entrada: `n` entero.
- Salida: `n^2`.
- Caso base: `n == 0` -> 0.
- Caso recursivo: usando `n^2 = (n - 1)^2 + 2n - 1` para `n > 0`.
  - Para `n < 0`, usar `(-n)^2`.

## Seudocodigo

```text
funcion cuadrado(n)
    si n < 0
        retornar cuadrado(-n)
    si n == 0
        retornar 0
    retornar cuadrado(n - 1) + 2 * n - 1
```
