# Superposición de Laberinto en Tiempo Real con Cámara Web y OpenCV
Este proyecto te permite superponer un laberinto personalizado sobre una transmisión de video en tiempo real utilizando Python y OpenCV.

## Tabla de Contenidos
- [Demostración](#demostración)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Personalización](#personalización)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Demostración

Puedes ver una demostración del proyecto en el GIF animado de arriba. Este proyecto permite superponer un laberinto personalizado sobre una transmisión de video en tiempo real, lo que resulta en una experiencia visual interactiva.

## Requisitos

Para ejecutar este proyecto, necesitas:

- Python 3.11.
- La librería OpenCV (`opencv-python`).
- Imágenes de las paredes del laberinto.

Asegúrate de tener estos requisitos instalados antes de ejecutar el proyecto.

## Instalación

Clona el repositorio y luego instala las dependencias utilizando pip:

```bash
git clone https://github.com/santiagolassog/Superposicion-Imagen-Laberinto-en-Tiempo-Real-con-Camara-Web-OpenCV.git
cd Superposicion-Imagen-Laberinto-en-Tiempo-Real-con-Camara-Web-OpenCV
```

## Uso
Puedes ejecuta el proyecto por pasos. Primero puedes ejecutar la lectura de cámara con el siguiente comando:
```bash
python 1.Leer_Camara.py
```
Y después puedes correr el código de superposición de cuadrados rojos, y finalmente el código que reemplaza las paredes con tus imágenes:
```bash
python 2.Superponer_Cuadrados.py
```
```bash
python 3.Superponer_Img_Laberinto.py
```
