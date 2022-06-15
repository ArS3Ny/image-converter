import numpy as np
from PIL import Image

for count in range(1, 59):
    try:
        with Image.open(f'images/theory_{count}.png') as im:
            im = im.convert('RGBA')
            data = np.array(im)
            rgba = data[:, :, :4]
            mask = np.all(rgba == [0, 0, 0, 0], axis=-1)  # c какого цвета
            data[mask] = [0, 0, 0, 0]  # на какой цвет
            data[np.logical_not(mask)] = [255, 255, 255, 150]
            new_im = Image.fromarray(data)
            new_im.save(f'new_images/theory_{count}.png')  # вместо theory название конечных файлов
    except:
        pass


