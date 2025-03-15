# pip install opencv-python opencv-contrib-python

# https://github.com/Saafke/EDSR_Tensorflow/blob/master/models/EDSR_x3.pb?ysclid=m82p25odgw139265703
# https://blog.mihailgok.ru/images-upscale-sr-opencv/

# zip upscaled.zip EDSR_x3.pb images_superres.py input.jpg upscaled.png 

import cv2
from cv2 import dnn_superres

# Создаём sr-объект
sr = dnn_superres.DnnSuperResImpl_create()

# Считываем изображение
image = cv2.imread('./input.jpg')

# Считываем модель
path = "EDSR_x3.pb"
sr.readModel(path)

# Установите backend CUDA и target, чтобы включить вывод графического процессора
# sr.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
# sr.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

# Устанавливаем модель и масштаб 
sr.setModel("edsr", 3)

# Улучшаем
result = sr.upsample(image)

# Сохраняем
cv2.imwrite("./upscaled.png", result)