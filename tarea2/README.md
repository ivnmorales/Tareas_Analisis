# Tarea 2 - Algoritmos de ordenamiento

En esta tarea resolví los problemas 88. Merge Sorted Array y 75. Sort Colors de LeetCode para resolverlos no utilice las funciones de ordenamiento de Python implemente los algoritmos directamente.

## 88. Merge Sorted Array

**Problema:**
https://leetcode.com/problems/merge-sorted-array/

Para este problema utilice una **fusión desde el final**. Como `nums1` y `nums2` ya vienen ordenados no es necesario volver a ordenar todos los elementos con un sort comparativo Comparo los últimos elementos válidos de los dos arreglos y coloco el mayor en la última posicion disponible de `nums1`.

Se hace desde el final porque así no se sobrescriben los elementos de `nums1` que todavia faltan por revisar para esto utilizo tres indices: uno recorre `nums1`, otro recorre `nums2` y el ultimo indica la posicion donde se debe colocar el siguiente elemento.

Donde `m` es la cantidad de elementos validos de `nums1` y `n` es la cantidad de elementos de `nums2`.

La complejidad de tiempo es `O(m + n)`, ya que en el peor caso se revisan todos los elementos de ambos arreglos y la complejidad de espacio es `O(1)` porque solamente se utilizan algunos indices y se modifica `nums1` directamente.

### Evidencia

[Ver evidencia de Merge Sorted Array](evidencias/merge-sorted-array-accepted.png)

## 75. Sort Colors

**Problema:**
https://leetcode.com/problems/sort-colors/

Para este problema utilice un algoritmo de **tres punteros (`low`, `mid` y `high`)**, conocido como bandera holandesa.

La idea es separar el arreglo en tres partes: los ceros quedan a la izquierda, los unos en el centro y los doses a la derecha.

El puntero `mid` revisa cada elemento si encuentra un `0` lo intercambia hacia la izquierda y avanzan `low` y `mid`. Si encuentra un `1` solamente avanza `mid`. Si encuentra un `2` lo intercambia con el elemento que está en `high` y disminuye `high`.

Cuando se encuentra un `2` no se aumenta `mid` porque el elemento que llego desde la derecha todavia no ha sido revisado.

No utilicé un sort comparativo ni las funciones `sort()` o `sorted()` como solamente existen tres valores posibles (`0`, `1` y `2`) el problema se puede resolver directamente con los tres punteros en tiempo lineal y una sola pasada.

Donde `n` es la cantidad de elementos del arreglo.

La complejidad de tiempo es `O(n)`. La complejidad de espacio es `O(1)` ya que solo se utilizan los tres punteros y no se crea otro arreglo.

### Evidencia

[Ver evidencia de Sort Colors](evidencias/sort-colors-accepted.png)
