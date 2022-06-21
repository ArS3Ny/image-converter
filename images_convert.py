import numpy as np
from PIL import Image
from PyQt5.QtWidgets import QLabel, QCheckBox

for count in range(1, 59):
    try:
        with Image.open(f'images/img_{count}.png') as im:
            im = im.convert('RGBA')
            data = np.array(im)
            rgba = data[:, :, :4]
            rgb = data[:, :, :3]
            mask = np.all(rgba == [255, 255, 255, 255], axis=-1)  # c какого цвета
            mask2 = np.all(rgb == [255, 196, 128], axis=-1)
            data[mask] = [0, 0, 0, 0]  # на какой цвет
            data[mask2] = [0, 0, 0, 0]
            data[np.logical_not(np.logical_or(mask, mask2))] = [255, 255, 255, 150]
            new_im = Image.fromarray(data)
            new_im.save(f'new_images/exer_{count}.png')  # вместо theory название конечных файлов
    except:
        pass
