# En una lista, duplicar sus elementos ([1,2,3] convertirla en [1,1,2,2,3,3])

## Analisis recursivo

- Entrada: `lista` de numeros.
- Salida: lista con cada elemento duplicado en posicion contigua.
- Caso base: lista vacia -> lista vacia.
- Caso recursivo: duplicar cabeza y procesar cola.

## Seudocodigo

```text
funcion duplicarElementos(lista)
    si lista es vacia
        retornar []
    cabeza = lista[0]
    cola = lista[1..fin]
    retornar [cabeza, cabeza] + duplicarElementos(cola)
```
