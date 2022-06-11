import numpy as np
from PIL import Image

count = 0
name = input('введите конечное имя файлов ')

while 1:
    count += 1
    with Image.open(f'images/img ({count}).png') as im:
        im = im.convert('RGBA')
        data = np.array(im)
        rgb = data[:, :, :3]
        color = [255, 255, 255]
        color2 = [222, 222, 222]
        black = [0, 0, 0, 255]
        white = [255, 255, 255, 255]
        mask = np.all(rgb == color, axis=-1)
        data[mask] = [0, 0, 0, 0]
        mask2 = np.all(rgb == color2, axis=-1)
        data[mask2] = [221, 221, 221, 221]
        data[np.logical_not(np.logical_or(mask, mask2))] = black
        new_im = Image.fromarray(data)
        new_im.save(f'new_images/{name}_{count}.png')




