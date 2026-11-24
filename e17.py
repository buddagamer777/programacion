from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

image= Image.open("Kei.jpg").convert("L")
image= np.array(imagen)
dimensiones= np.shape(imagen)

fil= dimensiones[0]
col= dimensiones[1]

rotado=