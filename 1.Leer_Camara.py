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

# Ciclo principal de lectura de la cámara
while True:

    # Lee los fotogramas
    ret, frame = cap.read()

    # Voltea horizontalmente el fotograma
    frame = cv2.flip(frame, 1)

    # Muestra los fotogramas en la ventana
    cv2.imshow('Laberinto Real Time con OpenCV', frame)

    # Si la tecla ESC es presionada, se sale del ciclo
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Libera la captura de video
cap.release()

# Cierra la ventana
cv2.destroyAllWindows()
