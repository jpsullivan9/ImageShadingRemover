import os
import shutil

#In this case my data has 4 types of rotations and coresponding shadings will group these.

#First smooth.

source_directory_smooth = 'Extracted/Grouped Cropped Corrected Blueberries/classes/Smooth'
source_directory_smooth_0 = 'Extracted/Grouped Cropped Corrected Blueberries/classes/Smooth/0'
source_directory_smooth_1 = 'Extracted/Grouped Cropped Corrected Blueberries/classes/Smooth/1'
source_directory_smooth_2 = 'Extracted/Grouped Cropped Corrected Blueberries/classes/Smooth/2'
source_directory_smooth_3 = 'Extracted/Grouped Cropped Corrected Blueberries/classes/Smooth/3'
source_directory_smooth_4 = 'Extracted/Grouped Cropped Corrected Blueberries/classes/Smooth/4'

source_directory_smooth_categories = []

source_directory_smooth_categories.append(source_directory_smooth_0)
source_directory_smooth_categories.append(source_directory_smooth_1)
source_directory_smooth_categories.append(source_directory_smooth_2)
source_directory_smooth_categories.append(source_directory_smooth_3)
source_directory_smooth_categories.append(source_directory_smooth_4)

smooth_file_list = os.listdir(source_directory_smooth)

for filename in smooth_file_list:
    if filename.endswith(('.jpg', '.jpeg', '.png')):
      berryId = filename[17]

      for i in range(5):
         if not os.path.exists(source_directory_smooth_categories[i]):
            os.makedirs(source_directory_smooth_categories[i])
         if berryId == f'{i}':
            imageFilePath = os.path.join(source_directory_smooth, filename)
            shutil.move(imageFilePath, source_directory_smooth_categories[i])


# Now for textured.
source_directory_textured = 'Extracted/Grouped Cropped Corrected Blueberries/classes/Textured'
source_directory_textured_0 = 'Extracted/Grouped Cropped Corrected Blueberries/classes/Textured/0'
source_directory_textured_1 = 'Extracted/Grouped Cropped Corrected Blueberries/classes/Textured/1'
source_directory_textured_2 = 'Extracted/Grouped Cropped Corrected Blueberries/classes/Textured/2'
source_directory_textured_3 = 'Extracted/Grouped Cropped Corrected Blueberries/classes/Textured/3'
source_directory_textured_4 = 'Extracted/Grouped Cropped Corrected Blueberries/classes/Textured/4'


source_directory_textured_categories = []

source_directory_textured_categories.append(source_directory_textured_0)
source_directory_textured_categories.append(source_directory_textured_1)
source_directory_textured_categories.append(source_directory_textured_2)
source_directory_textured_categories.append(source_directory_textured_3)
source_directory_textured_categories.append(source_directory_textured_4)

textured_file_list = os.listdir(source_directory_textured)


for filename in textured_file_list:
    if filename.endswith(('.jpg', '.jpeg', '.png')):
      berryId = filename[17]

      for i in range(5):
         if not os.path.exists(source_directory_textured_categories[i]):
            os.makedirs(source_directory_textured_categories[i])
         if berryId == f'{i}':
            imageFilePath = os.path.join(source_directory_textured, filename)
            shutil.move(imageFilePath, source_directory_textured_categories[i])