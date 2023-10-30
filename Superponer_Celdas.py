"""------------------------------------------------
Created on Wed Oct 29 19:02:57 2023
@author: Santiago Lasso
------------------------------------------------"""
import cv2
import numpy as np

# Crea la captura de video
cap = cv2.VideoCapture(0)

# Ancho y alto de la ventana
width, height = 800, 650

# Configura el tamaño de la ventana
cap.set(3, width)  # 3 corresponde al ancho
cap.set(4, height) # 4 corresponde a la altura

# Matriz de representación del laberinto (0 para espacio libre, 1 para pared)
laberinto = np.array([
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

# Tamaño de las celdas (paredes)
square_size = 50

# Nivel de transparencia para las celdas (paredes)
alpha = 0.2

# Ciclo principal de lectura de la cámara
while True:

    # Leer los fotogramas
    ret, frame = cap.read()

    # Voltea horizontalmente el fotograma
    frame = cv2.flip(frame, 1)

    # Cambia el tamaño del fotograma para que coincida con el tamaño de la ventana
    frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_CUBIC)
    
    # Crear una copia del fotograma para superponer las celdas
    overlay = frame.copy()

    # Obtiene las coordenadas de las paredes
    y_indices, x_indices = np.where(laberinto == 1)

    # Lista que contiene todas las coordenadas (x, y) correspondientes a las paredes
    list_celdas = list(zip(x_indices * square_size, y_indices * square_size))

    # Dibuja las celdas en la imagen de superposición de color rojo
    for x, y in list_celdas:
        cv2.rectangle(overlay, (x, y), (x + square_size, y + square_size), (0, 0, 255), -1)

    # Combina la imagen de superposición con el fotograma original
    frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)

    # Muestra los fotogramas en la ventana
    cv2.imshow('Laberinto Real Time con OpenCV', frame)

    # Si la tecla ESC es presionada, se sale del ciclo
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Libera la captura de video
cap.release()

# Cierra la ventana
cv2.destroyAllWindows()
