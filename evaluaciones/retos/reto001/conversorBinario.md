# Conversor a binario

## Analisis recursivo

- Entrada: `n` entero >= 0.
- Salida: representacion binaria en cadena.
- Caso base: `n < 2` -> "0" o "1".
- Caso recursivo: `f(n) = f(n / 2) + (n % 2)`.

## Seudocodigo

```text
funcion aBinario(n)
    si n < 2
        retornar convertirAString(n)
    return aBinario(n / 2) + convertirAString(n % 2)
```
