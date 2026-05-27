Juego del Ahorcado en Python

Aplicación de escritorio desarrollada en Python que implementa el clásico juego del ahorcado mediante una interfaz gráfica interactiva creada con Tkinter.

El sistema permite que un usuario ingrese una palabra secreta mientras otro jugador intenta adivinarla letra por letra antes de completar el muñeco colgado.



Descripción del proyecto

Este proyecto fue desarrollado como práctica para fortalecer habilidades en:

- Desarrollo de interfaces gráficas
- Programación orientada a objetos
- Lógica de videojuegos
- Manejo de eventos
- Validación de entradas


Funcionalidades

- Ingreso personalizado de palabra secreta
- Validación de palabras ingresadas
- Sistema de intentos limitados
- Detección automática de victoria
- Detección automática de derrota
- Dibujo progresivo del ahorcado
- Registro de letras utilizadas
- Reinicio completo del juego
- Interfaz gráfica interactiva



Tecnologías utilizadas

- Python
- Tkinter
- Tkinter MessageBox
- Tkinter Font
- Programación orientada a objetos


Estructura del proyecto

```text
juego_ahorcado.py
README.md
```


Funcionamiento del sistema

El programa sigue el siguiente flujo:

1. Un jugador ingresa la palabra secreta
2. El sistema valida la entrada
3. Se genera la interfaz del juego
4. El segundo jugador ingresa letras
5. El sistema verifica aciertos o errores
6. El dibujo del ahorcado avanza con cada fallo
7. El juego termina al ganar o perder



Reglas del juego

El jugador debe adivinar la palabra letra por letra.

Condiciones de victoria:

- Descubrir todas las letras antes de agotar los intentos

Condiciones de derrota:

- Alcanzar el máximo de errores permitidos

Cantidad máxima de intentos fallidos:

6



Interfaz gráfica

La aplicación incluye:

- Campo de ingreso de palabra
- Tablero visual
- Área de dibujo del ahorcado
- Registro de letras usadas
- Indicador de intentos restantes
- Botón de reinicio



Cómo ejecutar

Ejecutar desde terminal:

```bash
python juego_ahorcado.py
```



Conceptos aplicados

Durante este proyecto se implementaron:

- Clases y métodos
- Encapsulamiento
- Eventos de teclado
- Manipulación de widgets
- Validación lógica
- Gestión de estados
- Renderizado gráfico en canvas



Aprendizajes obtenidos

Este proyecto permitió reforzar conocimientos sobre:

- Diseño de interfaces gráficas avanzadas
- Manejo de eventos en Python
- Programación orientada a objetos
- Lógica condicional compleja
- Desarrollo de videojuegos básicos



Objetivo del proyecto

Construir una aplicación interactiva que combine lógica de programación, diseño gráfico y estructuras orientadas a objetos para simular el juego clásico del ahorcado.



Autor

Nicolas

Desarrollador en formación enfocado en Python, interfaces gráficas y desarrollo de aplicaciones interactivas.
