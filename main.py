import glob
from pdf2image import convert_from_path
import easyocr
import numpy as np
import PIL
from PIL import ImageDraw
import spacy
from IPython.display import display, Image
from tqdm import tqdm
import pandas as pd
import os
import time


def draw_boxes(image, bounds, color='red', width=4):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image


def main():

    targets = []
    folder_path = "./files/*.pdf"     # 특정 폴더에 있는 모든 파일 목록1
    lists = glob.glob(folder_path)
    # print(lists)
    for list in lists:
        targets.append(list.split('\\')[-1])
    print(targets)

    reader = easyocr.Reader(['ko', 'en'])

    total_lst = []
    for target in tqdm(targets):
        target = f"./files/{target}"
        # print(target)
        images = convert_from_path(
            target, 500, poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
        lst = []
        for image in tqdm(images):
            bounds = reader.readtext(np.array(image), min_size=0, slope_ths=0.2, ycenter_ths=0.7,
                                     height_ths=0.6, width_ths=0.8, decoder='beamsearch', beamWidth=100)
            # print(bounds)
            draw_boxes(image, bounds)
            display(image)
            text = ""
            for i in range(len(bounds)):
                text = text + bounds[i][1] + '\n'
    #         print(text)
            new_text = text.split('\n')
            # print(new_text)
            lst.extend(new_text)
            # print(lst)
        total_lst.append(lst[0])

    print(total_lst)

    df = pd.DataFrame(total_lst)
    df.to_excel("C:/my_develop2/pdf_ocr/results/test1.xlsx")

    i = 0
    path = "C:/my_develop2/pdf_ocr/files/"
    for filename in os.listdir(path):
        my_source = path + filename
    #     print(total_lst[i])
        new_name = total_lst[i].replace("/", "")
        my_dest = new_name + ".pdf"
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end-start)
