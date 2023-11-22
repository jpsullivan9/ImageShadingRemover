# Extract Zip
import zipfile
import os

#Replace with zip name.
path_to_zip_file = 'Grouped Cropped Corrected Blueberries.zip'
directory_to_extract_to = 'Extracted'

if not os.path.exists(directory_to_extract_to):
    os.makedirs(directory_to_extract_to)

with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    zip_ref.extractall(directory_to_extract_to)