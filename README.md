Resolución SLD (Selective Linear Definite-clause resolution) en Python

Instrucciones:
Al terminar subir un proyecto en el github con  un script sld_practice.py que, dado un programa (lista de cláusulas Horn) y un query, devuelva las sustituciones que satisfacen el query  entregado e imprime la ruta de derivación paso a paso. Un archvo con la base de conocimiento  utilizada y un archivo Readme.md con la información que están utilizando, el equipo al que pertenecen y las reglas y hechos que van a usar.

- Paso 1: Base de conocimientos
De la base de conocimiento selecciona las reglas y los hechos que te ayuden a generar  2 cláusulas de horn y poder aplicar la resolución SLD para obtener la respuesta.
- Paso 2: Unificación
Debes generar una función para crear el paso de Unificación para comparar un patrón con un hecho.Si hay conflicto (una variable ya tiene un valor distinto), devuelve None.
- Paso 3: Resolución SLD 
Debe recibir una consulta, realizar la búsqueda, utilizar la Unificación y regresar una respuesta.

Equipo: Sistema Experto Automotriz

Hechos utilizados:
- Las fallas se manifiestan a través de Síntomas (ej., ruidos, olores, luces de advertencia).
- Ciertas Luces en el Tablero (ej., Check Engine) indican la activación de códigos de falla específicos.

Reglas utilizadas:
- Si el motor emite humo blanco, entonces puede haber una fuga de refrigerante dentro del motor y hay un empaque de cabeza dañado.
- Si el motor no arranca y la batería está cargada, entonces puede haber una falla en el sistema de encendido o suministro de combustible.

- Si el vehículo no avanza al acelerar, entonces el embrague está patinando o hay falla en la caja de transmisión. 
- Si se escuchan ruidos metálicos al cambiar de marcha, entonces puede haber desgaste en los engranajes o falta de lubricante.

