"""------------------------------------------------
Created on Mon Oct 30 09:06:31 2023
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
alpha = 0.5

# Cargar una imagen para reemplazar los cuadros rojos
image = cv2.imread("Images/pared2.png")

# Redimensionar el tamaño de la imagen
image = cv2.resize(image, (square_size, square_size))

# Ciclo principal de lectura de la cámara
while True:

    # Lee los fotogramas
    ret, frame = cap.read()

    # Voltea horizontalmente el fotograma
    frame = cv2.flip(frame, 1)

    # Cambia el tamaño del fotograma para que coincida con el tamaño de la ventana
    frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_CUBIC)
    
    # Crea una copia del fotograma para superponer las celdas
    overlay = frame.copy()

    # Obtiene las coordenadas de las paredes
    y_indices, x_indices = np.where(laberinto == 1)

    # Dibuja la imagen en las coordenadas de las paredes
    for x, y in zip(x_indices * square_size, y_indices * square_size):
        overlay[y:y + square_size, x:x + square_size] = image

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
