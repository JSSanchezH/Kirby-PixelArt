import cv2
import numpy as np
import matplotlib.pyplot as plt

dimX = 36
dimY = 34

negro = (0, 0, 0)
blanco = (255, 255, 255)
rosa = (240, 200, 240)
rosaOscuro = (240, 100, 140)
azul = (40, 60, 255)

img = 255*np.ones((dimY, dimX, 3), np.uint8)
print(img)

# Contorno
#  Columna 4
a1 = 15
a2 = 18
i = 4
for ciclo in range(a1, a2+1):
    img[ciclo, i] = negro
    img[ciclo, dimX-i] = negro

#  Columna 5
a1 = 14
a2 = 27
i += 1
for ciclo in range(a1, a2+1):
    if ciclo >= 15 and ciclo <= 18:
        img[ciclo, i] = rosa
        img[ciclo, dimX-i] = rosa
    elif ciclo >= 20 and ciclo <= 24:
        img[ciclo, i] = blanco
    else:
        img[ciclo, i] = negro
        img[ciclo, dimX-i] = negro

#  Columna 6
a1 = 13
a2 = 28
i += 1
for ciclo in range(a1, a2+1):
    if ciclo >= 14 and ciclo <= 19:
        img[ciclo, i] = rosa
        img[ciclo, dimX-i] = rosa
    elif ciclo >= 21 and ciclo <= 23:
        img[ciclo, i] = blanco
    elif ciclo >= 25 and ciclo <= 27:
        img[ciclo, i] = rosaOscuro
        img[ciclo, dimX-i] = rosaOscuro
    else:
        img[ciclo, i] = negro
        img[ciclo, dimX-i] = negro

#  Columna 7
a1 = 12
a2 = 29
i += 1
for ciclo in range(a1, a2+1):
    if ciclo >= 13 and ciclo <= 19:
        img[ciclo, i] = rosa
        img[ciclo, dimX-i] = rosa
    elif ciclo >= 21 and ciclo <= 22:
        img[ciclo, i] = blanco
    elif ciclo >= 24 and ciclo <= 28:
        img[ciclo, i] = rosaOscuro
        img[ciclo, dimX-i] = rosaOscuro
    else:
        img[ciclo, i] = negro
        img[ciclo, dimX-i] = negro

#  Columna 8
a1 = 10
a2 = 29
i += 1
for ciclo in range(a1, a2+1):
    if ciclo >= 12 and ciclo <= 18:
        img[ciclo, i] = rosa
        img[ciclo, dimX-i] = rosa
    elif ciclo >= 23 and ciclo <= 28:
        img[ciclo, i] = rosaOscuro
        img[ciclo, dimX-i] = rosaOscuro
    else:
        img[ciclo, i] = negro
        img[ciclo, dimX-i] = negro

#  Columna 9
a1 = 8
a2 = 29
i += 1
for ciclo in range(a1, a2+1):
    if ciclo >= 10 and ciclo <= 21:
        img[ciclo, i] = rosa
        img[ciclo, dimX-i] = rosa
    elif ciclo >= 23 and ciclo <= 28:
        img[ciclo, i] = rosaOscuro
        img[ciclo, dimX-i] = rosaOscuro
    else:
        img[ciclo, i] = negro
        img[ciclo, dimX-i] = negro

#  Columna 10
a1 = 7
a2 = 29
i += 1
for ciclo in range(a1, a2+1):
    if ciclo >= 15 and ciclo <= 15:
        img[ciclo, i] = rosaOscuro
        img[ciclo, dimX-i] = rosaOscuro
    elif ciclo >= 8 and ciclo <= 22:
        img[ciclo, i] = rosa
        img[ciclo, dimX-i] = rosa
    elif ciclo >= 24 and ciclo <= 28:
        img[ciclo, i] = rosaOscuro
        img[ciclo, dimX-i] = rosaOscuro
    else:
        img[ciclo, i] = negro
        img[ciclo, dimX-i] = negro

#  Columna 11
a1 = 6
a2 = 29
i += 1
for ciclo in range(a1, a2+1):
    if ciclo >= 14 and ciclo <= 16:
        img[ciclo, i] = rosaOscuro
        img[ciclo, dimX-i] = rosaOscuro
    elif ciclo >= 7 and ciclo <= 23:
        img[ciclo, i] = rosa
        img[ciclo, dimX-i] = rosa
    elif ciclo >= 25 and ciclo <= 28:
        img[ciclo, i] = rosaOscuro
        img[ciclo, dimX-i] = rosaOscuro
    else:
        img[ciclo, i] = negro
        img[ciclo, dimX-i] = negro

#  Columna 12
a1 = 6
a2 = 29
i += 1
for ciclo in range(a1, a2+1):
    if ciclo >= 14 and ciclo <= 16:
        img[ciclo, i] = rosaOscuro
        img[ciclo, dimX-i] = rosaOscuro
    elif ciclo >= 7 and ciclo <= 24:
        img[ciclo, i] = rosa
        img[ciclo, dimX-i] = rosa
    elif ciclo >= 26 and ciclo <= 28:
        img[ciclo, i] = rosaOscuro
        img[ciclo, dimX-i] = rosaOscuro
    else:
        img[ciclo, i] = negro
        img[ciclo, dimX-i] = negro

#  Columna 13
a1 = 5
a2 = 29
i += 1
for ciclo in range(a1, a2+1):
    if ciclo >= 15 and ciclo <= 15:
        img[ciclo, i] = rosaOscuro
        img[ciclo, dimX-i] = rosaOscuro
    elif ciclo >= 6 and ciclo <= 24:
        img[ciclo, i] = rosa
        img[ciclo, dimX-i] = rosa
    elif ciclo >= 26 and ciclo <= 28:
        img[ciclo, i] = rosaOscuro
        img[ciclo, dimX-i] = rosaOscuro
    else:
        img[ciclo, i] = negro
        img[ciclo, dimX-i] = negro

#  Columna 14
a1 = 5
a2 = 29
i += 1
for ciclo in range(a1, a2+1):
    if (ciclo >= 6 and ciclo <= 9) or (ciclo >= 15 and ciclo <= 25):
        img[ciclo, i] = rosa
        img[ciclo, dimX-i] = rosa
    elif ciclo >= 27 and ciclo <= 28:
        img[ciclo, i] = rosaOscuro
        img[ciclo, dimX-i] = rosaOscuro
    else:
        img[ciclo, i] = negro
        img[ciclo, dimX-i] = negro

#  Columna 15
a1 = 4
a2 = 29
i += 1
for ciclo in range(a1, a2+1):
    if (ciclo >= 5 and ciclo <= 8) or (ciclo >= 16 and ciclo <= 25):
        img[ciclo, i] = rosa
        img[ciclo, dimX-i] = rosa
    elif ciclo >= 10 and ciclo <= 11:
        img[ciclo, i] = blanco
        img[ciclo, dimX-i] = blanco
    elif ciclo >= 13 and ciclo <= 14:
        img[ciclo, i] = azul
        img[ciclo, dimX-i] = azul
    elif ciclo >= 27 and ciclo <= 28:
        img[ciclo, i] = rosaOscuro
        img[ciclo, dimX-i] = rosaOscuro

    else:
        img[ciclo, i] = negro
        img[ciclo, dimX-i] = negro

#  Columna 16
a1 = 4
a2 = 29
i += 1
for ciclo in range(a1, a2+1):
    if (ciclo >= 5 and ciclo <= 9) or (ciclo >= 15 and ciclo <= 25):
        img[ciclo, i] = rosa
        img[ciclo, dimX-i] = rosa
    elif ciclo >= 27 and ciclo <= 28:
        img[ciclo, i] = rosaOscuro
        img[ciclo, dimX-i] = rosaOscuro
    else:
        img[ciclo, i] = negro
        img[ciclo, dimX-i] = negro

#  Columna 17
a1 = 4
a2 = 28
i += 1
for ciclo in range(a1, a2+1):
    if (ciclo >= 5 and ciclo <= 15) or (ciclo >= 17 and ciclo <= 25):
        img[ciclo, i] = rosa
        img[ciclo, dimX-i] = rosa
    elif ciclo >= 27 and ciclo <= 27:
        img[ciclo, i] = rosaOscuro
        img[ciclo, dimX-i] = rosaOscuro
    else:
        img[ciclo, i] = negro
        img[ciclo, dimX-i] = negro

#  Columna 18
a1 = 4
a2 = 27
i += 1
for ciclo in range(a1, a2+1):
    if (ciclo >= 5 and ciclo <= 16) or (ciclo >= 18 and ciclo <= 25):
        img[ciclo, i] = rosa
    else:
        img[ciclo, i] = negro


plt.imshow(img)  # mostramos nuestra imagen
plt.show()
