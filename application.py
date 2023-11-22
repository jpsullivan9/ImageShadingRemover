import cv2
import os
from numpy.random import seed
from shadingRemover import shadingRemove

seed(1)

source_directory_smooth = 'Extracted/Grouped Cropped Corrected Blueberries/classes/Smooth'
source_directory_textured = 'Extracted/Grouped Cropped Corrected Blueberries/classes/Textured'

smooth_file_list = os.listdir(source_directory_smooth)
textured_file_list = os.listdir(source_directory_textured)

nPoints = 100

for filename in smooth_file_list:
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(source_directory_smooth, filename)
        outputImage = shadingRemove(image_path, nPoints)
        cv2.imwrite(image_path, outputImage)

for filename in textured_file_list:
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(source_directory_textured, filename)
        outputImage = shadingRemove(image_path, nPoints)
        cv2.imwrite(image_path, outputImage)