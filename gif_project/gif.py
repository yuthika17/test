import imageio.v3 as iio

file_images=[
    'dancing_cat_1.jpeg',
    'dancing_cat_2.jpeg',
    'dancing_cat_3.jpeg',
    'dancing_cat_4.jpeg',
    'dancing_cat_5.jpeg',
    'dancing_cat_6.jpeg',
    'dancing_cat_7.jpeg',
    'dancing_cat_8.jpeg',
    'dancing_cat_9.jpeg',
    'dancing_cat_10.jpeg',
    'dancing_cat_11.jpeg',
    'dancing_cat_12.jpeg',
    'dancing_cat_13.jpeg',
    'dancing_cat_14.jpeg',
    'dancing_cat_15.jpeg',
             ]

images = []

from PIL import Image

import numpy as np  

size = (945,720)

for file in file_images :
    img = Image.open(file).resize(size)
    images.append(np.array(img))



iio.imwrite('dancing_cat.gif', images , duration=200 , loop=0)


