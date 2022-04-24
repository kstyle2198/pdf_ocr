import glob
from pdf2image import convert_from_path
import easyocr
import numpy as np
import PIL
from PIL import ImageDraw
import spacy
from IPython.display import display, Image

################
targets = []
folder_path = "./files/*.pdf"     # 특정 폴더에 있는 모든 파일 목록
lists = glob.glob(folder_path)
print(lists)
for list in lists:
    targets.append(list.split('\\')[-1])
print(targets)

#################
for target in targets:
    target = f"./files/{target}"
    print(target)

    reader = easyocr.Reader(['ko', 'en'])
    images = convert_from_path(
        target, 500, poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
    print(len(images))
    for i in range(len(images)):
        display(images[i])
