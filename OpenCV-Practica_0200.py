import cv2
# Alejandra Rivera Valenzuela NC = 0200
# Define el nombre de tu imagen (asegúrate de que la extensión sea la correcta, ej. .jpg o .png)
ruta_imagen = 'snoopy_0200_ale.jpg'

# Cargar la imagen original
image = cv2.imread(ruta_imagen)

# Verificar que la imagen se cargó correctamente
if image is None:
    print(f"Error: No se pudo encontrar la imagen '{ruta_imagen}'. Verifica el nombre y la extensión.")
    exit()

# 1. Mostrar la imagen en una ventana
cv2.imshow('Imagen Original', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2. Convertir a escala de grises y guardar
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_image.jpg', gray_image)

# 3. Redimensionar a 300x200 y guardar
resized_image = cv2.resize(image, (300, 200))
cv2.imwrite('resized_image.jpg', resized_image)

# 4. Rotar 90 grados y guardar
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
matrix = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated_image = cv2.warpAffine(image, matrix, (w, h))
cv2.imwrite('rotated_image.jpg', rotated_image)

# 5. Aplicar desenfoque gaussiano (Gaussian Blur) y guardar
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
cv2.imwrite('blurred_image.jpg', blurred_image)

# 6. Detección de bordes con Canny y guardar
edges = cv2.Canny(gray_image, 100, 200)
cv2.imwrite('edges.jpg', edges)

# 7. Dibujar rectángulo, agregar texto y guardar (usamos una copia para no alterar la original)
image_texto = image.copy()
cv2.rectangle(image_texto, (50, 50), (200, 200), (255, 0, 0), 3)
cv2.putText(image_texto, 'OpenCV', (60, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imwrite('output_image.jpg', image_texto)

# 8. Aplicar umbralización (Thresholding) y guardar
_, thresh_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite('threshold_image.jpg', thresh_image)

# 9. Encontrar y dibujar contornos y guardar (usamos otra copia de la original)
image_contornos = image.copy()
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image_contornos, contours, -1, (0, 255, 0), 2)
cv2.imwrite('contours_image.jpg', image_contornos)

print("Alejandra Rivera Valenzuela NC = 0200")