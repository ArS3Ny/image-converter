import numpy as np
from PIL import Image

count = 0
name = input('введите конечное имя файлов ')
for count in range(50):
    try:
        with Image.open(f'images/theory_{count}.png') as im:
            im = im.convert('RGBA')
            data = np.array(im)
            rgb = data[:, :, :3]
            color = [255, 255, 255]
            black = [0, 0, 0, 255]
            white = [255, 255, 255, 255]
            mask = np.all(rgb == color, axis=-1)
            data[mask] = [0, 0, 0, 0]
            data[np.logical_not(mask)] = black
            new_im = Image.fromarray(data)
            new_im.save(f'new_images/{name}_{count}.png')

    except:
        pass


