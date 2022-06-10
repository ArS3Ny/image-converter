from PIL import Image
import PIL

images = [1, 2]
count = 0
name = input('введите конечное имя файлов ')

while 1:
    try:
        count += 1
        with Image.open(f'images/img ({count}).png') as im:
            pixels = im.load()
            x, y = im.size

            for i in range(x):
                for j in range(y):
                    r, g, b, a = pixels[i, j]
                    if r == g == b == 255:
                        pixels[i, j] = 0, 0, 0, 0
                    elif r == g == b == 222:
                        pass
                    else:
                        pixels[i, j] = 0, 0, 0, 255
            im.save(f'new_images/{name}_{count}.png')
    except:
        break
