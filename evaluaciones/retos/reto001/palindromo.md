# Validar si una palabra es un palindromo

## Analisis recursivo

- Entrada: `texto` cadena.
- Salida: `true` si es palindromo, `false` si no.
- Caso base: longitud 0 o 1 -> `true`.
- Caso recursivo: comparar extremos y recortar.
  - Si `texto[0] != texto[fin]` -> `false`.
  - Si son iguales -> `f(resto)` sin extremos.

## Seudocodigo

```text
funcion esPalindromo(texto)
    si longitud(texto) <= 1
        retornar true
    si texto[0] != texto[fin]
        retornar false
    resto = texto[1..fin-1]
    retornar esPalindromo(resto)
```
