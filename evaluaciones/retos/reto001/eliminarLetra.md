# En una palabra/frase, eliminar todas las apariciones de una letra

## Analisis recursivo

- Entrada: `texto` cadena, `letra` caracter.
- Salida: `texto` sin apariciones de `letra`.
- Caso base: cadena vacia -> vacia.
- Caso recursivo: tomar primer caracter y procesar el resto.
  - Si `texto[0] == letra`, no se incluye.
  - Si no, se incluye `texto[0]`.

## Seudocodigo

```text
funcion eliminarLetra(texto, letra)
    si texto es vacio
        retornar ""
    primero = texto[0]
    resto = texto[1..fin]
    si primero == letra
        retornar eliminarLetra(resto, letra)
    retornar primero + eliminarLetra(resto, letra)
```
