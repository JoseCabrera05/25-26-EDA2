# En una palabra/frase, reemplazar una letra por otra

## Analisis recursivo

- Entrada: `texto` cadena, `origen` caracter, `destino` caracter.
- Salida: `texto` con `origen` reemplazado por `destino`.
- Caso base: cadena vacia -> vacia.
- Caso recursivo: procesar primer caracter y el resto.

## Seudocodigo

```text
funcion reemplazarLetra(texto, origen, destino)
    si texto es vacio
        retornar ""
    primero = texto[0]
    resto = texto[1..fin]
    si primero == origen
        retornar destino + reemplazarLetra(resto, origen, destino)
    retornar primero + reemplazarLetra(resto, origen, destino)
```
