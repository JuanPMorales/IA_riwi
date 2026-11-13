# Entrega IA Riwi

Este repositorio reúne tres ejercicios relacionados con algoritmos, análisis
de decisiones con inteligencia artificial y diseño de una plataforma web
educativa.

## Estructura del proyecto

```text
IA_riwi/
├── Ejercicio 1 – Algoritmo/
│   └── ordenamiento.py
├── Ejercicio 2 – Archivo descargable/
│   └── riwi-tres-cupos-borrador.txt
└── Ejercicio 3 – Página web con IA/
    └── README.md
```

## Ejercicios y carpetas

### 1. Ejercicio 1 – Algoritmo

Carpeta: `Ejercicio 1 – Algoritmo/`

Contiene un algoritmo en Python para ordenar tres números.

#### `ordenamiento.py`

- Define la función `ordenar_tres_numeros(a, b, c, descendente=False)`.
- Ordena los valores mediante comparaciones e intercambios, sin utilizar una
  función de ordenamiento externa.
- Permite obtener el resultado en orden ascendente o descendente.
- Incluye una función `main()` que solicita tres números al usuario y valida:
  - Que se ingresen exactamente tres valores.
  - Que todos los valores sean numéricos.
  - Que la dirección sea `ascendente` o `descendente`.
- Muestra en consola el orden final de los números.

Para ejecutarlo:

```bash
python "Ejercicio 1 – Algoritmo/ordenamiento.py"
```

### 2. Ejercicio 2 – Archivo descargable

Carpeta: `Ejercicio 2 – Archivo descargable/`

Contiene el desarrollo escrito de un caso de análisis para asignar tres cupos
de acompañamiento entre ocho estudiantes.

#### `riwi-tres-cupos-borrador.txt`

El archivo documenta:

- La elección individual inicial de estudiantes.
- Una primera consulta a una IA y su respuesta.
- Una segunda consulta con información adicional sobre el Programa B.
- La comparación entre ambas respuestas.
- Los criterios usados para incluir o excluir a cada estudiante.
- Las limitaciones de las recomendaciones generadas por la IA.
- La importancia de que la decisión final sea revisada por una persona.

El ejercicio muestra cómo una recomendación puede cambiar cuando se agregan
datos sobre el objetivo y los recursos concretos de un programa.

### 3. Ejercicio 3 – Página web con IA

Carpeta: `Ejercicio 3 – Página web con IA/`

Esta carpeta contiene la documentación y los prompts usados para idear y
especificar una plataforma web educativa llamada **DevForge**.

#### `README.md`

El documento recopila:

- La idea inicial de una plataforma de cursos de programación.
- Las características de una comunidad tipo foro.
- La propuesta de mentorías y chats privados.
- La paleta de colores y el sistema visual.
- Los requisitos funcionales y no funcionales.
- Prompts para herramientas de generación de interfaces y funcionalidades.
- La autenticación y la base de datos local simulada.
- El panel de tutores y el reproductor LMS.
- Los retos de programación tipo Codewars.
- El foro, las notificaciones y la personalización.
- El sistema de mensajería y nuevas conversaciones.
- La migración pendiente hacia una base de datos en la nube y sincronización
  en tiempo real.

Este archivo funciona como historial de diseño, requerimientos y evolución
propuesta para la plataforma.

## Prompt incluido

> Generame un README.md donde enumeres cada ejercicio y cada carpeta diciendo
> qué es lo que hace.
>
> Estructura inicial del espacio de trabajo:
>
> ```text
> /IA_riwi
> Ejercicio 1 – Algoritmo/
>     ordenamiento.py
> Ejercicio 2 – Archivo descargable/
>     riwi-tres-cupos-borrador.txt
> Ejercicio 3 – Página web con IA/
>     README.md
> ```

